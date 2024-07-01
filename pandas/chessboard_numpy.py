import numpy as np
import matplotlib.pyplot as plt

# Unicode chess pieces with filled symbols
pieces = {
    'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
    'R': '♜', 'N': '♞', 'B': '♝', 'Q': '♛', 'K': '♚', 'P': '♟', '': ' '
}
#'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙',

# Initialize the chessboard
def initialize_chessboard():
    chessboard = np.array([
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
    ])
    return chessboard

# Plot the chessboard with pieces
def plot_chessboard(chessboard):
    fig, ax = plt.subplots()
    chessboard_pattern = generate_chessboard(8)
    ax.imshow(chessboard_pattern, cmap='Greys', interpolation='nearest')

    # Place the pieces on the chessboard
    for i in range(8):
        for j in range(8):
            piece = chessboard[i, j]
            # Choose red or green color for text based on the background
            text_color = 'grey' if i < 2 else 'green'
            ax.text(j, i, pieces[piece], ha='center', va='center', fontsize=20, color=text_color)

    # Remove the ticks
    ax.set_xticks([])
    ax.set_yticks([])

    # Set the title
    plt.title('Chessboard with Pieces')
    plt.show()

# Function to generate the empty chessboard pattern
def generate_chessboard(size):
    chessboard = np.zeros((size, size), dtype=int)
    chessboard[1::2, ::2] = 1
    chessboard[::2, 1::2] = 1
    return chessboard

# Main function
if __name__ == "__main__":
    chessboard = initialize_chessboard()
    plot_chessboard(chessboard)
