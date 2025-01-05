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
        for row in range(9):
            for col in range(9):
                entry = self.create_cell(frame, row, col)
                self.entries[row][col] = entry
                if self.grid[row][col] != 0:
                    self.fill_cell(entry, self.grid[row][col])

    def create_cell(self, frame, row, col):
        """Create a single cell in the Sudoku grid."""
        bg_color = "#d1e7dd" if (row // 3 + col // 3) % 2 == 0 else "#f8d7da"
        entry = tk.Entry(
            frame,
            width=2,
            font=("Arial", 16),
            justify="center",
            bg=bg_color,
            relief=tk.RIDGE,
        )
        entry.grid(row=row, column=col, padx=2, pady=2)
        return entry

    def create_buttons(self):
        """Create action buttons for the Sudoku game."""
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        buttons = [
            ("Check Solution", self.check_solution),
            ("Reveal Solution", self.reveal_solution),
            ("Reset", self.reset_puzzle),
            ("Quit", self.root.quit),
        ]
        for text, command in buttons:
            tk.Button(button_frame, text=text, command=command).pack(side=tk.LEFT, padx=5)

    def fill_cell(self, entry, value):
        """Fill a cell with a given value and disable it."""
        entry.insert(0, str(value))
        entry.config(state="disabled", disabledforeground="black")

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
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if self.solve(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True

    def check_solution(self):
        """Check if the user's solution matches the actual solution."""
        has_errors = False
        for row in range(9):
            for col in range(9):
                user_input = self.entries[row][col].get()
                correct_value = self.solution[row][col]
                if not user_input.isdigit() or int(user_input) != correct_value:
                    self.entries[row][col].config(bg="red")
                    has_errors = True
                else:
                    self.entries[row][col].config(bg="white")
        return not has_errors

    def get_cell_value(self, row, col):
        """Get the integer value of a cell, or return 0 if invalid."""
        value = self.entries[row][col].get()
        return int(value) if value.isdigit() else 0

    def mark_cell(self, row, col, is_correct):
        """Mark a cell as correct or incorrect."""
        color = "black" if is_correct else "red"
        self.entries[row][col].config(fg=color)

    def reveal_solution(self):
        """Reveal the correct solution in the grid."""
        for row in range(9):
            for col in range(9):
                self.entries[row][col].config(state="normal", fg="black")
                self.entries[row][col].delete(0, tk.END)
                self.entries[row][col].insert(0, str(self.solution[row][col]))
                if self.grid[row][col] != 0:
                    self.entries[row][col].config(state="disabled", disabledforeground="black")

    def reset_puzzle(self):
        """Reset the grid to its original state."""
        for row in range(9):
            for col in range(9):
                entry = self.entries[row][col]
                if self.grid[row][col] == 0:
                    entry.config(state="normal", fg="black")
                    entry.delete(0, tk.END)
                else:
                    entry.delete(0, tk.END)
                    entry.insert(0, str(self.grid[row][col]))
                    entry.config(state="disabled", disabledforeground="black")


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
