import pytest


#fixture for setup
@pytest.fixture
def test_data():
    return [1, 2, 3, 4, 5]


# parameterized test function
@pytest.mark.include
@pytest.mark.parametrize("number, expected", [
    (2, True),
    (7, False),
    (1, True)
])
def test_number_in_data(test_data, number, expected):
    assert (number in test_data) == expected


@pytest.mark.math
@pytest.mark.parametrize("input,expected", [
    (2 + 3, 5),
    (5 - 3, 2),
    (10 * 2, 20)
])
def test_operations(input, expected):
    assert input == expected


@pytest.fixture
def sample_data():
    return {"key": "value"}


@pytest.mark.dict
def test_sample_data(sample_data):
    assert sample_data["key"] == "value"


def capital_case(x):
    return x.capitalize()


@pytest.mark.capital
def test_capital_case():
    assert capital_case('monday') == 'Monday'


@pytest.mark.reversed
def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]


@pytest.mark.reversed
def test_reversed_fixture(test_data):
    assert list(reversed(test_data)) == [5, 4, 3, 2, 1]
