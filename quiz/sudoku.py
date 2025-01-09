import random
import tkinter as tk


class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.solution = None
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.generate_puzzle()
        self.create_widgets()

    def create_widgets(self):
        """Create and arrange widgets for the Sudoku game."""
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        """Create the 9x9 Sudoku grid."""
        frame = tk.Frame(self.root)
        frame.pack()
        self.traverse_grid(lambda r, c: self.init_cell(frame, r, c))

    def init_cell(self, frame, row, col):
        """Initialize a single cell in the Sudoku grid."""
        bg_color = "#d1e7dd" if (row // 3 + col // 3) % 2 == 0 else "#f8d7da"
        entry = tk.Entry(frame, width=2, font=("Arial", 16), justify="center", bg=bg_color, relief=tk.RIDGE)
        entry.grid(row=row, column=col, padx=2, pady=2)
        self.entries[row][col] = entry
        if self.grid[row][col] != 0:
            self.set_cell_value(row, col, self.grid[row][col], is_readonly=True)

    def create_buttons(self):
        """Create action buttons for the Sudoku game."""
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        buttons = [
            ("New Game", self.new_game),
            ("Check Solution", self.check_solution),
            ("Reveal Solution", self.reveal_solution),
            ("Reset", self.reset_puzzle),
            ("Quit", self.root.quit),
        ]
        for text, command in buttons:
            tk.Button(button_frame, text=text, command=command).pack(side=tk.LEFT, padx=5)

    def set_cell_value(self, row, col, value, is_readonly=False, color="black"):
        """Set a cell's value, state, and color."""
        entry = self.entries[row][col]
        entry.config(state="normal", fg=color)
        entry.delete(0, tk.END)
        entry.insert(0, str(value))
        if is_readonly:
            entry.config(state="disabled", disabledforeground="black")

    def traverse_grid(self, func):
        """Traverse the grid and apply a function to each cell."""
        for row in range(9):
            for col in range(9):
                if func(row, col):  # Allow early exit if the function returns True
                    return row, col
        return None

    def generate_puzzle(self):
        """Generate a Sudoku puzzle with a valid solution."""
        self.solve(self.grid)
        self.solution = [row[:] for row in self.grid]
        self.remove_cells()

    def remove_cells(self, cells_to_remove=50):
        """Remove random cells to create a Sudoku puzzle."""
        for _ in range(cells_to_remove):
            row, col = random.randint(0, 8), random.randint(0, 8)
            self.grid[row][col] = 0

    def is_valid(self, grid, row, col, num):
        """Check if placing a number is valid."""
        if num in grid[row] or num in [grid[i][col] for i in range(9)]:
            return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        return num not in [grid[i][j] for i in range(start_row, start_row + 3) for j in range(start_col, start_col + 3)]

    def solve(self, grid):
        """Solve the Sudoku puzzle using backtracking."""

        def find_empty_cell(row, col):
            """Check if the current cell is empty."""
            return grid[row][col] == 0

        empty_cell = self.traverse_grid(find_empty_cell)
        if not empty_cell:
            return True  # Puzzle solved

        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid(grid, row, col, num):
                grid[row][col] = num
                if self.solve(grid):
                    return True
                grid[row][col] = 0

        return False

    def check_solution(self):
        """Check if the user's solution matches the actual solution."""
        has_errors = False

        def validate(row, col):
            nonlocal has_errors
            if not self.validate_and_mark_cell(row, col):
                has_errors = True

        self.traverse_grid(validate)
        return not has_errors

    def validate_and_mark_cell(self, row, col):
        """Validate a cell's input against the solution and mark errors."""
        user_input = self.entries[row][col].get()
        correct_value = self.solution[row][col]
        if not user_input.isdigit() or int(user_input) != correct_value:
            self.entries[row][col].config(bg="red")
            return False
        self.entries[row][col].config(bg="white")
        return True

    def reveal_solution(self):
        """Reveal the correct solution in the grid."""
        self.traverse_grid(lambda r, c: self.set_cell_value(r, c, self.solution[r][c], is_readonly=(self.grid[r][c] != 0)))

    def reset_puzzle(self):
        """Reset the grid to its original state and restore original cell colors."""

        def reset_cell(row, col):
            entry = self.entries[row][col]
            # Determine the original background color
            bg_color = "#d1e7dd" if (row // 3 + col // 3) % 2 == 0 else "#f8d7da"
            # Reset the cell content and colors
            if self.grid[row][col] == 0:
                entry.config(state="normal", fg="black", bg=bg_color)
                entry.delete(0, tk.END)  # Clear the cell
            else:
                entry.delete(0, tk.END)  # Reset the cell to its original value
                entry.insert(0, str(self.grid[row][col]))
                entry.config(state="disabled", disabledforeground="black", bg=bg_color)

        self.traverse_grid(reset_cell)

    def new_game(self):
        """Start a new Sudoku game with a fresh puzzle."""
        self.grid = [[0 for _ in range(9)] for _ in range(9)]  # Reset the grid
        self.generate_puzzle()  # Generate a new puzzle
        self.solution = [row[:] for row in self.grid]  # Update the solution

        def reset_to_new_game(row, col):
            entry = self.entries[row][col]
            bg_color = "#d1e7dd" if (row // 3 + col // 3) % 2 == 0 else "#f8d7da"
            if self.grid[row][col] == 0:
                entry.config(state="normal", fg="black", bg=bg_color)
                entry.delete(0, tk.END)  # Clear editable cells
            else:
                entry.delete(0, tk.END)  # Set the new puzzle value
                entry.insert(0, str(self.grid[row][col]))
                entry.config(state="disabled", disabledforeground="black", bg=bg_color)

        self.traverse_grid(reset_to_new_game)


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
