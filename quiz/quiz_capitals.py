import json
import random


# Load country data from a JSON file
def load_country_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        countries = json.load(file)
    return {country["name"]: country["capital"] for country in countries}


def ask_question(country_capitals):
    country = random.choice(list(country_capitals.keys()))
    capital = country_capitals[country]

    print(f"What is the capital of {country}?")
    answer = input("Your answer: ").strip()

    if answer.lower() == capital.lower():
        print("Correct!")
    else:
        print(f"Incorrect. The capital of {country} is {capital}.")


def main():
    country_capitals = load_country_data('countries.json')

    print("Welcome to the Capitals Game!")
    while True:
        ask_question(country_capitals)
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != "y":
            break
    print("Thanks for playing!")


if __name__ == "__main__":
    main()


