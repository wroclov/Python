
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("TicTacToe")

# Board positions:
# 0 | 1 | 2
# ---------
# 3 | 4 | 5
# ---------
# 6 | 7 | 8

game = {
    "board": [" "] * 9,
    "current_player": "X",
    "status": "not_started",
}


def get_snapshot():
    """Return a copy of the current game state."""
    return {
        "board": game["board"].copy(),
        "current_player": game["current_player"],
        "status": game["status"],
    }


def check_winner():
    """Return the winning symbol, or None if there is no winner."""
    board = game["board"]

    winning_lines = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]

    for a, b, c in winning_lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]

    return None


@mcp.tool()
def start_game() -> dict:
    """Start or reset a Tic-Tac-Toe game. X plays first."""
    game["board"] = [" "] * 9
    game["current_player"] = "X"
    game["status"] = "in_progress"

    return get_snapshot()


@mcp.tool()
def get_game_state() -> dict:
    """Get the current board, current player, and game status."""
    return get_snapshot()


@mcp.tool()
def make_move(position: int) -> dict:
    """Place the current player's mark at position 0-8."""
    if game["status"] != "in_progress":
        return {
            "error": "No game is in progress. Call start_game first.",
            **get_snapshot(),
        }

    if isinstance(position, bool) or not isinstance(position, int):
        return {
            "error": "Position must be an integer from 0 to 8.",
            **get_snapshot(),
        }

    if position < 0 or position > 8:
        return {
            "error": "Position must be between 0 and 8.",
            **get_snapshot(),
        }

    if game["board"][position] != " ":
        return {
            "error": "That position is already occupied.",
            **get_snapshot(),
        }

    player = game["current_player"]
    game["board"][position] = player

    winner = check_winner()

    if winner:
        game["status"] = f"{winner}_wins"
    elif " " not in game["board"]:
        game["status"] = "draw"
    else:
        game["current_player"] = "O" if player == "X" else "X"

    return get_snapshot()


if __name__ == "__main__":
    mcp.run(transport="stdio")
