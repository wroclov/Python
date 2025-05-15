import pytest
from decimal import Decimal
from math_operations import add, subtract, multiply, divide, power

@pytest.mark.parametrize("a, b ,expected", [
    (2, 3, 5),
    (5, 3, 8),
    (-7, -4, -11)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# Test Subtraction
@pytest.mark.parametrize("a, b, expected", [
    (7, 3, 4),
    (0, 0, 0),
    (-1, -1, 0),
    (100, 350, -250)
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected",[
    (0, 1, 0,),
    (1, -5, -5),
    (-4, -7, 28),
    (3.2, 2.1, 6.72)
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == pytest.approx(expected, rel=1e-9)  # Adding a tolerance for comparison

@pytest.mark.parametrize("a, b, expected",[
    (0, 21, 0),
    (1, 44, 1),
    (10, 0, 1),
    (2, 3, 8),
    (81, 0.5, 9),
    (-2, 5, -32),
    (2, -3, 0.125),
    (0, 0, 1)
])
def test_power(a, b, expected):
    assert power(a, b) == expected

@pytest.mark.divide
@pytest.mark.parametrize("a, b, expected",[
    (10, 2, 5),
    (99999, -9, -11111),
    (5, 0.01, 500),
])
def test_divide_valid(a, b, expected):
    assert pytest.approx(divide(a, b), abs=0.0001) == expected

@pytest.mark.divide
def test_divide_zero_division():
    with pytest.raises(ValueError):
        divide(10, 0)

@pytest.mark.divide
@pytest.mark.parametrize("a, b, expected",[
    (10, 4, Decimal(2.5)),
    (7.5, -1.1, Decimal('-6.818')),
])
def test_divide_float(a, b, expected):

    result = Decimal(divide(a, b))

    # Set a tolerance for the comparison using Decimal's comparison features
    assert abs(result - expected) < Decimal('0.001'), f"Expected: {expected}, but got {result}"

@pytest.mark.divide
def test_divide_edge_cases():
    assert divide(0, 1) == 0
    assert divide(0, -1) == 0

@pytest.mark.divide
@pytest.mark.parametrize("a, b",[
        ('g', 2),
        ("some text", "other text"),
])
def test_divide_invalid_strings(a, b):
    with pytest.raises(TypeError):
        divide(a, b)

@pytest.mark.divide
@pytest.mark.parametrize("a, b",[
        ([1, 2, 3], 4),
        (None, -1),
        (True, True),
        (False, 1),
])
def test_divide_mixed_invalid_types(a, b):
    with pytest.raises(TypeError):
        divide(a, b)


@pytest.mark.divide
def test_divide_large_numbers():
    large_number = Decimal(10 ** 100)  # A number with 100 zeros as Decimal
    assert divide(large_number, Decimal(10)) == Decimal(10 ** 99)  # Expected result should be large_number divided by 10

    # Testing negative large integers
    assert divide(-large_number, Decimal(10)) == Decimal(-10 ** 99)

    large_float = Decimal('1.5e308')  # Close to the maximum value for a double-precision float, directly as Decimal
    assert divide(large_float, Decimal(1.5)) == Decimal('1e308')  # Use Decimal for both the expected and actual value

    # Testing division by a huge number
    expected_result = Decimal(1) / Decimal(10 ** 100)  # Expected result
    actual_result = divide(Decimal(1), large_number)

    # Normalize both expected and actual result to match the precision you care about (e.g., 100 significant digits)
    precision = Decimal('1e-100')
    assert actual_result.quantize(precision) == expected_result.quantize(precision)


