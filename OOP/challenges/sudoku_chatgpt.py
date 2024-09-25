# A Python program to solve Sudoku using Backtracking

# Define the size of the grid (9x9)
N = 9

# Function to print the grid
def print_grid(grid):
    for row in grid:
        print(row)

# Check if it's safe to place a number in the cell
def is_safe(grid, row, col, num):
    # Check if 'num' is not in the current row
    if num in grid[row]:
        return False

    # Check if 'num' is not in the current column
    for i in range(N):
        if grid[i][col] == num:
            return False

    # Check if 'num' is not in the current 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False

    return True

# Backtracking function to solve the Sudoku
def solve_sudoku(grid):
    # Find an empty cell
    for row in range(N):
        for col in range(N):
            if grid[row][col] == 0:
                # Try placing digits from 1 to 9
                for num in range(1, 10):
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num  # Place the number

                        # Recursively solve the rest of the grid
                        if solve_sudoku(grid):
                            return True

                        # If placing 'num' doesn't lead to a solution, reset it
                        grid[row][col] = 0

                return False  # Trigger backtracking if no number is valid

    return True  # Sudoku is solved

# Example Sudoku puzzle (0 represents empty cells)
grid = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

# Solve the Sudoku and print the result
if solve_sudoku(grid):
    print_grid(grid)
else:
    print("No solution exists")
