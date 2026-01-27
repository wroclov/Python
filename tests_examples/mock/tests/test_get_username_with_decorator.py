from unittest.mock import patch
from app.service import get_username


@patch("app.service.fetch_user")
def test_get_username_with_decorator(mock_fetch):
    mock_fetch.return_value = {"name": "Alice"}

    result = get_username(1)

    assert result == "Alice"
