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
def load_piece_images():
    pieces = ['P', 'p', 'R', 'r', 'N', 'n', 'B', 'b', 'Q', 'q', 'K', 'k']
    images = {}
    for piece in pieces:
        images[piece] = pygame.transform.scale(pygame.image.load(f'pieces/{piece}.png'), (square_size, square_size))
        images[piece.lower()] = pygame.transform.scale(pygame.image.load(f'pieces/{piece}w.png'), (square_size, square_size))
    return images

pieces_images = load_piece_images()

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
    board.turn = chess.BLACK  # Explicitly set the turn to White ? For some reason it acts in opposite way
    print("Initial turn (White=True, Black=False):", board.turn)
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

            # Check for pawn promotion
            if dragging_piece.piece_type == chess.PAWN:
                last_rank = 7 if dragging_piece.color == chess.WHITE else 0
                if chess.square_rank(target_square) == last_rank:
                    promotion_piece = prompt_promotion_piece_ui(dragging_piece.color)
                    move = chess.Move(from_square=selected_square, to_square=target_square, promotion=promotion_piece)

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
                handle_illegal_move(move)

        # Reset dragging state
        dragging_piece = None
        selected_square = None
        dragging_position = None
    return dragging_piece, dragging_position, selected_square

def handle_illegal_move(move):
    print(f"Illegal move attempted: {move}")

def prompt_promotion_piece_ui(dragging_piece_color):
    """Display a UI popup to choose a promotion piece."""
    # Create a semi-transparent overlay
    overlay = pygame.Surface((width, height))
    overlay.set_alpha(150)  # Semi-transparency for focus
    overlay.fill((0, 0, 0))  # Black background
    screen.blit(overlay, (0, 0))

    # Dimensions and positioning for the menu
    menu_width, menu_height = 400, 100
    menu_x = (width - menu_width) // 2
    menu_y = (height - menu_height) // 2

    # Draw the menu background
    pygame.draw.rect(screen, (200, 200, 200), (menu_x, menu_y, menu_width, menu_height), border_radius=10)
    pygame.draw.rect(screen, (0, 0, 0), (menu_x, menu_y, menu_width, menu_height), 2, border_radius=10)

    # Piece options and images
    promotion_pieces = ['q', 'r', 'b', 'n']
    promotion_images = {
        'q': pieces_images['Q' if dragging_piece_color == chess.WHITE else 'q'],
        'r': pieces_images['R' if dragging_piece_color == chess.WHITE else 'r'],
        'b': pieces_images['B' if dragging_piece_color == chess.WHITE else 'b'],
        'n': pieces_images['N' if dragging_piece_color == chess.WHITE else 'n'],
    }

    # Draw promotion piece options
    for i, piece in enumerate(promotion_pieces):
        piece_image = promotion_images[piece]
        x = menu_x + 10 + i * 100  # Position each piece with padding
        y = menu_y + 10
        screen.blit(piece_image, (x, y))

        # Draw border for each option
        pygame.draw.rect(screen, (0, 0, 0), (x, y, square_size, square_size), 2)

    pygame.display.flip()

    # Wait for user input
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for i, piece in enumerate(promotion_pieces):
                    x = menu_x + 25 + i * 100
                    y = menu_y + 25
                    if x <= mouse_x <= x + square_size and y <= mouse_y <= y + square_size:
                        return {'q': chess.QUEEN, 'r': chess.ROOK, 'b': chess.BISHOP, 'n': chess.KNIGHT}[piece]

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
