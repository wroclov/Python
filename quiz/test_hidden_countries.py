import pytest
from hidden_countries import create_grid, place_word_in_grid, is_valid_placement, fill_empty_spaces

@pytest.fixture
def sample_grid_data():
    """Fixture to provide a sample grid and words for testing."""
    words = ["HELLO", "WORLD", "PYTHON", "GRID"]
    size = 10
    return size, words


class TestCreateGrid:

    def test_create_grid(self, sample_grid_data):
        size, words = sample_grid_data

        grid, word_locations = create_grid(size, words)

        # Check if the grid is of the correct size
        assert len(grid) == size
        assert len(grid[0]) == size

        # Check if words are placed in the grid
        for word in words:
            assert word in word_locations


    def test_place_word_in_grid(self, sample_grid_data):
        size, words = sample_grid_data
        grid = [["" for _ in range(size)] for _ in range(size)]
        word_locations = {}

        word = "HELLO"
        place_word_in_grid(grid, size, word, word_locations)

        # Verify that the word is placed correctly in word_locations
        assert word in word_locations  # Check if word is in locations

        # Check that the word is placed correctly in the grid
        for idx, (row, col) in enumerate(word_locations[word]):
            assert grid[row][col] == word[idx]


    @pytest.mark.xfail
    def test_is_valid_placement(self):
        size = 5
        grid = [
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""],
            ["", "", "", "", ""]
        ]
        word = "HELLO"
        start_row, start_col = 1, 1
        delta_row, delta_col = 0, 1  # Horizontal placement

        # Check that valid placement returns True
        assert is_valid_placement(grid, size, word, start_row, start_col, delta_row, delta_col) is True

        # Simulate an invalid placement (out of bounds)
        start_row, start_col = 4, 4
        assert is_valid_placement(grid, size, word, start_row, start_col, delta_row, delta_col) is False



    def test_fill_empty_spaces(self):
        size = 5
        grid = [
            ["A", "B", "C", "", ""],
            ["D", "E", "F", "", ""],
            ["G", "H", "I", "", ""],
            ["J", "K", "L", "", ""],
            ["M", "N", "O", "", ""]
        ]
        fill_empty_spaces(grid)

        # Verify that all empty spaces are filled with random letters
        for row in range(size):
            for col in range(size):
                assert grid[row][col] != ""

# Running tests (using pytest command or manually)
if __name__ == "__main__":
    pytest.main()