import tkinter as tk
from random import choice, randint, shuffle
import random
import string

# Extended list of country names
COUNTRIES = [
    "CANADA", "BRAZIL", "GERMANY", "FRANCE", "JAPAN",
    "INDIA", "CHINA", "RUSSIA", "SPAIN", "ITALY",
    "MEXICO", "EGYPT", "TURKEY", "GREECE", "NORWAY",
    "SWEDEN", "POLAND", "FINLAND", "AUSTRALIA", "ARGENTINA",
    "HUNGARY", "THAILAND", "VENEZUELA", "ICELAND", "SINGAPORE"
]

GRID_SIZE = 20


def create_grid(size, words):
    """Generates a grid with hidden words placed randomly."""
    grid = [["" for _ in range(size)] for _ in range(size)]
    word_locations = {}

    for word in words:
        place_word_in_grid(grid, size, word, word_locations)

    fill_empty_spaces(grid)

    return grid, word_locations


def place_word_in_grid(grid, size, word, word_locations):
    """Attempts to place a single word in the grid."""
    directions = {
        "H": (0, 1),   # Horizontal
        "V": (1, 0),   # Vertical
        "D": (1, 1),   # Diagonal
        "HR": (0, -1), # Horizontal Reverse
        "VR": (-1, 0), # Vertical Reverse
        "DR": (-1, -1) # Diagonal Reverse
    }

    attempts = 0
    original_word = word

    while attempts < 100:
        direction = choice(list(directions.keys()))
        word = word[::-1] if direction.endswith("R") else original_word
        delta_row, delta_col = directions[direction]

        start_row = randint(0, size - 1)
        start_col = randint(0, size - 1)

        if is_valid_placement(grid, size, word, start_row, start_col, delta_row, delta_col):
            place_word(grid, word, start_row, start_col, delta_row, delta_col, word_locations, original_word)
            return  # Word placed successfully

        attempts += 1

    # If no placement was found after 100 attempts, raise an error or handle it gracefully
    raise ValueError(f"Unable to place word '{word}' in the grid after 100 attempts.")



def is_valid_placement(grid, size, word, start_row, start_col, delta_row, delta_col):
    """Checks if a word can be placed at the starting position with the given direction."""
    for i, char in enumerate(word):
        row = start_row + i * delta_row
        col = start_col + i * delta_col

        # Check if the position is out of bounds
        if not (0 <= row < size and 0 <= col < size):
            return False

        # Check if the position is either empty or already contains the correct character
        if grid[row][col] not in ["", char]:
            return False

    return True


def place_word(grid, word, start_row, start_col, delta_row, delta_col, word_locations, original_word):
    """Places the word in the grid."""
    locations = []
    for i, char in enumerate(word):
        row = start_row + i * delta_row
        col = start_col + i * delta_col
        grid[row][col] = char
        locations.append((row, col))

    word_locations[original_word] = locations


def fill_empty_spaces(grid):
    """Fills empty spaces in the grid with random letters."""
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "":
                #grid[row][col] = choice(string.ascii_uppercase)
                pass



class WordSearchGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Search Game")
        self.grid_size = GRID_SIZE
        self.words = random.sample(COUNTRIES, 20)
        print(self.words)
        shuffle(self.words)
        self.grid, self.word_locations = create_grid(self.grid_size, self.words)
        self.remaining_words = set(self.words)
        self.start_coords = None
        self.found_words = set()

        self.create_widgets()

    def create_widgets(self):
        """Create the game UI."""
        self.info_label = tk.Label(self.root, text=f"Words left: {len(self.remaining_words)}", font=("Arial", 14))
        self.info_label.pack()

        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack()

        self.buttons = []
        for row in range(self.grid_size):
            button_row = []
            for col in range(self.grid_size):
                btn = tk.Button(self.grid_frame, text=self.grid[row][col], width=3, height=1,
                                font=("Courier", 12), command=lambda r=row, c=col: self.cell_clicked(r, c))
                btn.grid(row=row, column=col)
                button_row.append(btn)
            self.buttons.append(button_row)

        self.control_frame = tk.Frame(self.root)
        self.control_frame.pack(pady=10)

        self.reset_button = tk.Button(self.control_frame, text="Reset", command=self.reset_game, font=("Arial", 12))
        self.reset_button.grid(row=0, column=0, padx=5)

        self.give_up_button = tk.Button(self.control_frame, text="Give Up", command=self.reveal_remaining, font=("Arial", 12))
        self.give_up_button.grid(row=0, column=1, padx=5)

    def cell_clicked(self, row, col):
        """Handle cell click."""
        if not self.start_coords:
            self.start_coords = (row, col)
            self.buttons[row][col].config(bg="yellow")
        else:
            end_coords = (row, col)
            self.check_word(self.start_coords, end_coords)
            self.start_coords = None

    def check_word(self, start, end):
        """Check if the selection matches any hidden word."""
        row1, col1 = start
        row2, col2 = end

        selected_word = self.get_selected_word(row1, col1, row2, col2)

        if not selected_word:
            self.reset_highlights()
            return

        reversed_word = selected_word[::-1]
        found_word = next(
            (word for word in (selected_word, reversed_word) if word in self.remaining_words), None
        )

        if found_word:
            self.handle_found_word(found_word, start, end)
        else:
            self.reset_highlights()

    def get_selected_word(self, row1, col1, row2, col2):
        """Extracts the selected word from the grid."""
        if row1 == row2:  # Horizontal
            print("Horizontal")
            return "".join(self.grid[row1][min(col1, col2):max(col1, col2) + 1])

        if col1 == col2:  # Vertical
            print("Vertical")
            return "".join(self.grid[row][col1] for row in range(min(row1, row2), max(row1, row2) + 1))

        if abs(row1 - row2) == abs(col1 - col2):  # Diagonal
            print("Diagonal")
            step = range(abs(row1 - row2) + 1)
            return "".join(
                self.grid[row1 + (i if row1 < row2 else -i)][col1 + (i if col1 < col2 else -i)] for i in step
            )

        return ""

    def handle_found_word(self, word, start, end):
        """Handles actions for when a word is found."""
        print("Found:", word)
        self.remaining_words.remove(word)
        self.found_words.add(word)
        self.info_label.config(text=f"Words left: {len(self.remaining_words)}")
        self.mark_word(start, end, "green")
        print(self.remaining_words)
        if len(self.remaining_words) == 0:
            self.info_label.config(text="You Won! All words found.")

    def mark_word(self, start, end, color):
        """Highlight the selected word."""
        row1, col1 = start
        row2, col2 = end

        # Helper function to mark the word in the grid
        def highlight_cells(rows, cols):
            for row, col in zip(rows, cols):
                self.buttons[row][col].config(bg=color)

        if row1 == row2:  # Horizontal
            cols = range(min(col1, col2), max(col1, col2) + 1)
            highlight_cells([row1] * len(cols), cols)
        elif col1 == col2:  # Vertical
            rows = range(min(row1, row2), max(row1, row2) + 1)
            highlight_cells(rows, [col1] * len(rows))
        elif abs(row1 - row2) == abs(col1 - col2):  # Diagonal
            rows = range(row1, row2 + (1 if row2 > row1 else -1), (1 if row2 > row1 else -1))
            cols = range(col1, col2 + (1 if col2 > col1 else -1), (1 if col2 > col1 else -1))
            highlight_cells(rows, cols)

    def reset_highlights(self):
        """Reset highlights for incorrectly guessed words."""
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if self.buttons[row][col].cget("bg") in ["yellow", "SystemButtonFace"]:
                    self.buttons[row][col].config(bg="SystemButtonFace")

    def reset_game(self):
        """Reset the game."""
        self.grid, self.word_locations = create_grid(self.grid_size, self.words)
        self.remaining_words = set(self.words)
        self.found_words = set()
        self.info_label.config(text=f"Words left: {len(self.remaining_words)}")
        self.start_coords = None

        for row in range(self.grid_size):
            for col in range(self.grid_size):
                self.buttons[row][col].config(text=self.grid[row][col], bg="SystemButtonFace")

    def reveal_remaining(self):
        """Reveal the locations of all remaining words."""
        print("Remaining" , self.remaining_words)
        for word in self.remaining_words:
            if word in self.word_locations:
                locations = self.word_locations[word]
            elif word[::-1] in self.word_locations:  # Check reversed word
                locations = self.word_locations[word[::-1]]
            else:
                continue  # Skip if not found (should not happen)

            for row, col in locations:
                self.buttons[row][col].config(bg="orange")

        self.remaining_words.clear()
        self.info_label.config(text="Game Over! All words revealed.")


# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = WordSearchGame(root)
    root.mainloop()
