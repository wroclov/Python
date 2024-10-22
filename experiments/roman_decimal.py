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

    def from_roman(roman_num: str) -> int:
        roman_to_int_map = RomanNumerals.roman_to_int_map
        final_number = 0
        prev_value = 0

        # Iterate over the Roman numeral from left to right
        for i, char in enumerate(roman_num):
            if char not in roman_to_int_map:
                raise ValueError(f"Invalid Roman numeral character: {char}")

            current_value = roman_to_int_map[char]

            if i > 0 and current_value > roman_to_int_map[roman_num[i - 1]]:
                # Ensure this is a valid subtractive combination
                if roman_num[i - 1] + char not in ["IV", "IX", "XL", "XC", "CD", "CM"]:
                    raise ValueError(f"Invalid subtractive combination: {roman_num[i - 1]}{char}")
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
