
from typing import Optional, TypedDict

from mcp.server.fastmcp import FastMCP


# ---------------------------------------------------------
# MCP server configuration
# ---------------------------------------------------------

mcp = FastMCP("TicTacToe")


# ---------------------------------------------------------
# Game configuration
# ---------------------------------------------------------

BOARD_SIZE = 9

# All possible winning combinations.
WINNING_LINES = [
    (0, 1, 2),  # Horizontal
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),  # Vertical
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),  # Diagonal
    (2, 4, 6),
]


class GameState(TypedDict):
    """Structure representing the current game state."""

    board: list[str]
    current_player: str
    status: str


# Centralized game state.
game: GameState = {
    "board": [" "] * BOARD_SIZE,
    "current_player": "X",
    "status": "not_started",
}


# ---------------------------------------------------------
# Game state utilities
# ---------------------------------------------------------

def get_snapshot() -> GameState:
    """
    Return a snapshot of the current game state.

    A copy of the board is returned to prevent external
    modifications to the internal game state.
    """

    return {
        "board": game["board"].copy(),
        "current_player": game["current_player"],
        "status": game["status"],
    }


def check_winner(board: list[str]) -> Optional[str]:
    """
    Check whether a player has won.

    Returns:
        "X" if X wins.
        "O" if O wins.
        None if there is no winner yet.
    """

    for a, b, c in WINNING_LINES:

        if (
            board[a] != " "
            and board[a] == board[b] == board[c]
        ):
            return board[a]

    return None


# ---------------------------------------------------------
# MCP tools
# ---------------------------------------------------------

@mcp.tool()
def start_game() -> GameState:
    """
    Start a new Tic-Tac-Toe game or reset an existing game.

    X always makes the first move.

    Returns:
        The initial game board and game status.
    """

    game["board"] = [" "] * BOARD_SIZE
    game["current_player"] = "X"
    game["status"] = "in_progress"

    return get_snapshot()


@mcp.tool()
def get_game_state() -> GameState:
    """
    Retrieve the current game state.

    Returns:
        The board, current player and game status.
    """

    return get_snapshot()


@mcp.tool()
def make_move(position: int) -> dict:
    """
    Make a move for the current player.

    Args:
        position: Board position between 0 and 8.

    Board layout:

        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8

    Returns:
        Updated game state if successful.
        An error message if the move is invalid.
    """

    # Ensure a game has been started.
    if game["status"] != "in_progress":
        return {
            "error": (
                "No game is currently in progress. "
                "Call start_game first."
            ),
            **get_snapshot(),
        }

    # Validate the position type.
    # Boolean values are explicitly rejected because
    # bool is a subclass of int in Python.
    if isinstance(position, bool) or not isinstance(position, int):
        return {
            "error": "Position must be an integer from 0 to 8.",
            **get_snapshot(),
        }

    # Validate the board boundaries.
    if not 0 <= position < BOARD_SIZE:
        return {
            "error": "Position must be between 0 and 8.",
            **get_snapshot(),
        }

    # Prevent a player from overwriting an occupied cell.
    if game["board"][position] != " ":
        return {
            "error": "That position is already occupied.",
            **get_snapshot(),
        }

    # Apply the move for the current player.
    player = game["current_player"]
    game["board"][position] = player

    # Check whether the move resulted in a win.
    winner = check_winner(game["board"])

    if winner:
        game["status"] = f"{winner}_wins"

    # Check whether all positions are occupied.
    elif " " not in game["board"]:
        game["status"] = "draw"

    # Switch to the other player if the game continues.
    else:
        game["current_player"] = (
            "O" if player == "X" else "X"
        )

    return get_snapshot()


# ---------------------------------------------------------
# Server entry point
# ---------------------------------------------------------

if __name__ == "__main__":

    # Use standard input/output transport for communication
    # between the MCP server and the LangChain application.
    mcp.run(transport="stdio")
