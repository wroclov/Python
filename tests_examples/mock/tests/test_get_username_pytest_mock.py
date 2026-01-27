from app.service import get_username


def test_get_username_pytest_mock(mocker):
    mocker.patch(
        "app.service.fetch_user",
        return_value={"name": "Alice"}
    )

    assert get_username(1) == "Alice"
