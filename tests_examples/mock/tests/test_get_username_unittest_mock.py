from unittest.mock import patch
from app.service import get_username


def test_get_username_unittest_mock():
    with patch("app.service.fetch_user") as mock_fetch:
        mock_fetch.return_value = {"name": "Alice"}

        result = get_username(1)

        assert result == "Alice"
        mock_fetch.assert_called_once_with(1)
