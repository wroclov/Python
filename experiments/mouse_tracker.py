import numpy as np
import matplotlib.pyplot as plt
from pynput import mouse
from PIL import ImageGrab
import threading
import time


class MouseHeatmapTracker:
    def __init__(self, resolution=(1920, 1080), grid_size=20):
        """
        Initialize the mouse heatmap tracker.

        Args:
            resolution: Screen resolution (width, height)
            grid_size: Size of each grid cell for heatmap
        """
        self.resolution = resolution
        self.grid_size = grid_size
        self.grid_shape = (resolution[1] // grid_size, resolution[0] // grid_size)
        self.heatmap = np.zeros(self.grid_shape)
        self.tracking = False
        self.listener = None

    def on_move(self, x, y):
        """Callback for mouse movement."""
        if self.tracking:
            # Convert mouse position to grid coordinates
            grid_x = min(x // self.grid_size, self.grid_shape[1] - 1)
            grid_y = min(y // self.grid_size, self.grid_shape[0] - 1)

            # Ensure coordinates are within bounds
            if 0 <= grid_x < self.grid_shape[1] and 0 <= grid_y < self.grid_shape[0]:
                self.heatmap[grid_y, grid_x] += 1

    def start_tracking(self, duration=60):
        """
        Start tracking mouse movement.

        Args:
            duration: How long to track in seconds
        """
        print(f"Starting mouse tracking for {duration} seconds...")
        print("Move your mouse around normally. Press Ctrl+C to stop early.")

        self.tracking = True
        self.heatmap = np.zeros(self.grid_shape)

        # Start mouse listener
        self.listener = mouse.Listener(on_move=self.on_move)
        self.listener.start()

        # Track for specified duration
        try:
            time.sleep(duration)
        except KeyboardInterrupt:
            print("\nTracking stopped by user.")

        self.tracking = False
        self.listener.stop()
        print("Tracking complete!")

    def generate_heatmap(self, output_file='mouse_heatmap.png', colormap='hot'):
        """
        Generate and save the heatmap visualization.

        Args:
            output_file: Path to save the heatmap image
            colormap: Matplotlib colormap to use ('hot', 'viridis', 'plasma', etc.)
        """
        if np.max(self.heatmap) == 0:
            print("No mouse movement data recorded!")
            return

        # Create figure
        fig, ax = plt.subplots(figsize=(16, 9))

        # Apply log scale for better visualization
        heatmap_display = np.log1p(self.heatmap)

        # Create heatmap
        im = ax.imshow(heatmap_display, cmap=colormap, aspect='auto',
                       interpolation='bilinear', origin='upper')

        # Add colorbar
        cbar = plt.colorbar(im, ax=ax)
        cbar.set_label('Mouse Activity (log scale)', rotation=270, labelpad=20)

        # Set title and labels
        ax.set_title('Mouse Movement Heatmap', fontsize=16, fontweight='bold')
        ax.set_xlabel('Screen Width', fontsize=12)
        ax.set_ylabel('Screen Height', fontsize=12)

        # Remove tick labels for cleaner look
        ax.set_xticks([])
        ax.set_yticks([])

        # Add statistics text
        total_points = np.sum(self.heatmap)
        max_activity = np.max(self.heatmap)
        stats_text = f'Total Points: {int(total_points):,}\nMax Activity: {int(max_activity):,}'
        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes,
                fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

        plt.tight_layout()
        plt.savefig(output_file, dpi=150, bbox_inches='tight')
        print(f"Heatmap saved to {output_file}")
        plt.show()

    def get_hotspots(self, top_n=5):
        """
        Get the top N hotspots (most active areas).

        Args:
            top_n: Number of hotspots to return
        """
        flat_indices = np.argsort(self.heatmap.ravel())[-top_n:][::-1]
        hotspots = []

        for idx in flat_indices:
            y, x = np.unravel_index(idx, self.grid_shape)
            screen_x = x * self.grid_size + self.grid_size // 2
            screen_y = y * self.grid_size + self.grid_size // 2
            activity = self.heatmap[y, x]
            hotspots.append({
                'screen_pos': (screen_x, screen_y),
                'activity': int(activity)
            })

        return hotspots


def main():
    # Get screen resolution (you can adjust this to your screen)
    screen = ImageGrab.grab()
    resolution = screen.size
    print(f"Detected screen resolution: {resolution}")

    # Create tracker
    tracker = MouseHeatmapTracker(resolution=resolution, grid_size=20)

    # Track mouse for 60 seconds (adjust as needed)
    tracker.start_tracking(duration=60)

    # Generate heatmap
    tracker.generate_heatmap('mouse_heatmap.png', colormap='hot')

    # Show hotspots
    print("\nTop 5 Hotspots:")
    hotspots = tracker.get_hotspots(top_n=5)
    for i, spot in enumerate(hotspots, 1):
        print(f"{i}. Position: {spot['screen_pos']}, Activity: {spot['activity']}")


if __name__ == "__main__":
    main()