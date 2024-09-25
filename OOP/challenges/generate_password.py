import random
import secrets

# Sample Diceware word list (replace with a complete list for actual use)
DICEWARE_WORDS = [
    "apple", "banana", "cherry", "date", "elderberry",
    "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "quince",
    "raspberry", "strawberry", "tangerine", "watermelon", "zucchini",
    "jablko", "pomarancza", 'gruszka', "szczaw", "malina",
    "baklazan", "pomidor", "marchew", "wisnia", "agrest"
]


def generate_passphrase(num_words):
    """Generate a passphrase with a specified number of words."""
    if num_words < 1:
        raise ValueError("Number of words must be at least 1.")

    # Randomly select words from the Diceware list
    passphrase_random = random.sample(DICEWARE_WORDS, num_words)
    passphrase_choice = [secrets.choice(DICEWARE_WORDS) for _ in range(num_words)]

    # Join the words with a space
    return ' '.join(passphrase_random),' '.join(passphrase_choice)


# Example usage
num_words = 6  # Specify the number of words in the passphrase
passphrase = generate_passphrase(num_words)
print(f"Generated passphrase: {passphrase}")
