import unittest
import chess
from chess_game import get_square_under_mouse  # Adjust based on your actual function locations

class TestChessBoard(unittest.TestCase):

    def setUp(self):
        """Set up a new chess board for testing."""
        self.board = chess.Board()

    def test_initial_board(self):
        """Test if the initial board position is correct."""
        initial_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
        self.assertEqual(self.board.fen(), initial_fen)

    def test_square_under_mouse(self):
        """Test the square under mouse function."""
        # Simulating mouse position for center of a1 square
        mouse_x = 50 + (0 * 75) + 37.5  # margin + square_size * col + half square size
        mouse_y = 50 + (7 * 75) + 37.5  # margin + square_size * (7 - row) + half square size
        square = get_square_under_mouse(mouse_x, mouse_y)  # Now matches the updated function signature
        self.assertEqual(square, chess.square(0, 7))  # Should return a1

    def test_check_draw_conditions(self):
        """Test draw conditions."""
        # Example scenario: stalemate
        self.board.set_fen("k7/8/8/8/8/8/8/6K1 w - - 0 1")  # Black king is on a8, White king on h2

        self.assertTrue(self.board.is_stalemate())

        # Example scenario: fifty moves
        self.board.set_fen("8/8/8/8/8/8/8/7K w - - 0 100")
        self.assertTrue(self.board.is_fifty_moves())

        # Example scenario: fivefold repetition
        self.board.set_fen("8/8/8/8/8/8/8/7K w - - 0 1")
        self.board.push(chess.Move.from_uci("h7h8=Q"))
        self.board.push(chess.Move.from_uci("g7g8=Q"))
        self.board.push(chess.Move.from_uci("h8h7"))
        self.board.push(chess.Move.from_uci("g8g7"))
        self.assertTrue(self.board.is_fivefold_repetition())

if __name__ == "__main__":
    unittest.main()
