import re
class RomanNumerals:
    # Static dictionary to map single Roman numerals to their integer values
    roman_to_int_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    @staticmethod
    def to_roman(val: int) -> str:
        nums = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        thousands = ['', 'M', 'MM', 'MMM', 'MMMM']

        # Building the roman numeral using list to join later
        result = [
            thousands[val // 1000],
            hundreds[val // 100 % 10],
            tens[val // 10 % 10],
            nums[val % 10]
        ]
        return ''.join(result)

    @staticmethod
    def from_roman(roman_num: str) -> int:
        # Regular expression for valid Roman numerals
        valid_roman_regex = re.compile(
                r"^M{0,4}"  # Thousands: 0-4 M's
                r"(CM|CD|D?C{0,3})"  # Hundreds: 900 (CM), 400 (CD), 0-300 (C, CC, CCC), or 500 (D)
                r"(XC|XL|L?X{0,3})"  # Tens: 90 (XC), 40 (XL), 0-30 (X, XX, XXX), or 50 (L)
                r"(IX|IV|V?I{0,3})$"  # Units: 9 (IX), 4 (IV), 0-3 (I, II, III), or 5 (V)
            )

        # Validate the Roman numeral
        if not valid_roman_regex.match(roman_num):
            raise ValueError(f"Invalid Roman numeral: {roman_num}")

        # Convert valid Roman numeral to integer
        final_number = 0
        prev_value = 0

        for char in roman_num:
            current_value = RomanNumerals.roman_to_int_map[char]
            if current_value > prev_value:
                final_number += current_value - 2 * prev_value
            else:
                final_number += current_value
            prev_value = current_value

        return final_number


def main():
    # Test cases for to_roman method
    print("Testing to_roman method:")
    print("3549 ->", RomanNumerals.to_roman(3549))  # Expected: MMMDXLIX
    print("1994 ->", RomanNumerals.to_roman(1994))  # Expected: MCMXCIV
    print("58 ->", RomanNumerals.to_roman(58))  # Expected: LVIII
    print("9 ->", RomanNumerals.to_roman(9))  # Expected: IX
    print("4 ->", RomanNumerals.to_roman(4))  # Expected: IV

    # Test cases for from_roman method
    print("\nTesting from_roman method:")
    print("MMMDXLIX ->", RomanNumerals.from_roman("MMMDXLIX"))  # Expected: 3549
    print("MCMXCIV ->", RomanNumerals.from_roman("MCMXCIV"))  # Expected: 1994
    print("LVIII ->", RomanNumerals.from_roman("LVIII"))  # Expected: 58
    print("IX ->", RomanNumerals.from_roman("IX"))  # Expected: 9
    print("IV ->", RomanNumerals.from_roman("IV"))  # Expected: 4


if __name__ == "__main__":
    main()
