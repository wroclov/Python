import pygame
import chess

# Initialize Pygame
pygame.init()

# Constants
width, height = 800, 800
board_size = 600  # Size of the board
square_size = board_size // 8  # Size of each square
margin = 50  # Margin around the chessboard
background_color = (255, 255, 255)
board_color_1 = (238, 238, 210)
board_color_2 = (118, 150, 86)

# Load piece images
pieces_images = {
    'P': pygame.transform.scale(pygame.image.load('pieces/p.png'), (square_size, square_size)),
    'p': pygame.transform.scale(pygame.image.load('pieces/Pw.png'), (square_size, square_size)),
    'R': pygame.transform.scale(pygame.image.load('pieces/r.png'), (square_size, square_size)),
    'r': pygame.transform.scale(pygame.image.load('pieces/Rw.png'), (square_size, square_size)),
    'N': pygame.transform.scale(pygame.image.load('pieces/n.png'), (square_size, square_size)),
    'n': pygame.transform.scale(pygame.image.load('pieces/Nw.png'), (square_size, square_size)),
    'B': pygame.transform.scale(pygame.image.load('pieces/b.png'), (square_size, square_size)),
    'b': pygame.transform.scale(pygame.image.load('pieces/Bw.png'), (square_size, square_size)),
    'Q': pygame.transform.scale(pygame.image.load('pieces/q.png'), (square_size, square_size)),
    'q': pygame.transform.scale(pygame.image.load('pieces/Qw.png'), (square_size, square_size)),
    'K': pygame.transform.scale(pygame.image.load('pieces/k.png'), (square_size, square_size)),
    'k': pygame.transform.scale(pygame.image.load('pieces/Kw.png'), (square_size, square_size)),
}

# Create the display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chess Game")

def draw_board():
    """Draw the chessboard with alternating colors and labels."""
    for row in range(8):
        for col in range(8):
            color = board_color_1 if (row + col) % 2 == 0 else board_color_2
            pygame.draw.rect(screen, color, (margin + col * square_size, margin + row * square_size, square_size, square_size))

    # Draw column labels
    font = pygame.font.SysFont("Arial", 36)
    for col in range(8):
        label = chr(col + 97)  # 'a' to 'h'
        text = font.render(label, True, (0, 0, 0))
        screen.blit(text, (margin + col * square_size + square_size // 2 - text.get_width() // 2, height - margin // 2 - text.get_height() // 2))

    # Draw row labels
    for row in range(8):
        label = str(row + 1)  # 1 to 8
        text = font.render(label, True, (0, 0, 0))
        screen.blit(text, (margin // 2 - text.get_width() // 2, margin + (7 - row) * square_size + square_size // 2 - text.get_height() // 2))

def draw_pieces(board, dragging_piece=None, dragging_position=None):
    """Draw the pieces on the board."""
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            piece_image = pieces_images[piece.symbol()]
            col = chess.square_file(square)
            row = chess.square_rank(square)
            screen.blit(piece_image, (margin + col * square_size, margin + (row) * square_size))  # Remove the '7 -' to flip the board

    # Draw the piece being dragged
    if dragging_piece and dragging_position:
        piece_image = pieces_images[dragging_piece.symbol()]
        screen.blit(piece_image, (dragging_position[0] - square_size // 2, dragging_position[1] - square_size // 2))
def show_message(message):
    """Display a message on the screen."""
    font = pygame.font.SysFont("Arial", 48)
    text = font.render(message, True, (0, 0, 0))
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)

def get_square_under_mouse(mouse_x, mouse_y):
    """Get the square under the mouse cursor."""
    adjusted_x = mouse_x - margin
    adjusted_y = mouse_y - margin

    if 0 <= adjusted_x < board_size and 0 <= adjusted_y < board_size:
        col = adjusted_x // square_size
        row = adjusted_y // square_size  # Remove the '7 -' to flip the row calculation
        return chess.square(col, row)
    return None

def check_draw_conditions(board):
    """Check for stalemate, fivefold repetition, and 50-move rule."""
    if board.is_stalemate():
        show_message("It's a draw!")
    elif board.is_fifty_moves():
        show_message("Draw by 50-move rule!")
    elif board.is_fivefold_repetition():
        show_message("Draw by fivefold repetition!")

def main():
    board = chess.Board()
    board.turn = chess.WHITE  # Explicitly set the turn to White
    dragging_piece = None
    selected_square = None
    dragging_position = None

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("it was quit by user")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                dragging_piece, selected_square = mouse_button_down_handling(
                    board,
                    dragging_piece,
                    event,
                    selected_square)
            elif event.type == pygame.MOUSEMOTION:
                if dragging_piece:
                    dragging_position = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging_piece, dragging_position, selected_square = mouse_down_up_handling(
                    board,
                    dragging_piece,
                    dragging_position,
                    event,
                    selected_square)

        # Draw everything
        screen.fill(background_color)  # Clear the screen
        draw_board()
        draw_pieces(board, dragging_piece, dragging_position)

        # Update the display
        pygame.display.flip()

    pygame.quit()

def mouse_down_up_handling(board, dragging_piece, dragging_position, event, selected_square):
    if dragging_piece:
        target_square = get_square_under_mouse(event.pos[0], event.pos[1])
        if target_square is not None:
            move = chess.Move(from_square=selected_square, to_square=target_square)
            if move in board.legal_moves:
                board.push(move)
                try:
                    print(board.san(move))  # Log the move in standard chess notation
                except Exception as e:
                    print(f"Error logging move: {e}")

                # Check for checkmate or draw conditions
                if board.is_checkmate():
                    winner = "White" if board.turn else "Black"
                    show_message(f"{winner} wins!")
                else:
                    check_draw_conditions(board)

            else:
                print(f"Illegal move attempted: {move}")

        # Reset dragging state
        dragging_piece = None
        selected_square = None
        dragging_position = None
    return dragging_piece, dragging_position, selected_square

def mouse_button_down_handling(board, dragging_piece, event, selected_square):
    square = get_square_under_mouse(event.pos[0], event.pos[1])
    if square is not None:
        piece = board.piece_at(square)
        if piece and (piece.color == board.turn):
            dragging_piece = piece
            selected_square = square
    return dragging_piece, selected_square

if __name__ == "__main__":
    main()