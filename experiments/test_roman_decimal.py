import pytest
from roman_decimal import RomanNumerals

@pytest.mark.parametrize("input_val, expected", [
    (3549, "MMMDXLIX"),
    (1994, "MCMXCIV"),
    (58, "LVIII"),
    (9, "IX"),
    (4, "IV"),
    (3999, "MMMCMXCIX"),
    (1, "I"),
    (4000, "MMMM")
])
def test_to_roman(input_val, expected):
    assert RomanNumerals.to_roman(input_val) == expected

@pytest.mark.parametrize("input_val, expected", [
    ("MMMDXLIX", 3549),
    ("MCMXCIV", 1994),
    ("LVIII", 58),
    ("IX", 9),
    ("IV", 4),
    ("MMMCMXCIX", 3999),
    ("I", 1),
    ("MMMM", 4000),
])
def test_from_roman(input_val, expected):
    assert RomanNumerals.from_roman(input_val) == expected

@pytest.mark.parametrize("input_val", [
    ("MMMMM"),
    ("IIII"),
    ("VX"),
    ("ABC")
])
def test_invalid_roman_numerals(input_val):
    with pytest.raises(ValueError, match=r"Invalid Roman numeral"):
        RomanNumerals.from_roman(input_val)  # Invalid numeral

def test_large_numbers():
    assert RomanNumerals.to_roman(4000) == "MMMM"

def test_small_numbers():
    assert RomanNumerals.to_roman(0) == ""
