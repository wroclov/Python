import string


from nltk.probability import FreqDist
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize

# Load a sample text from the Gutenberg corpus
text = gutenberg.raw('austen-emma.txt')

# Tokenize the text
tokens = word_tokenize(text.lower())


def freqDist_plot(tokens):
    fdist = FreqDist(tokens)
    # Print the frequency of the word 'emma'
    print(f"Frequency of 'emma': {fdist['emma']}")
    # Print the 10 most common words
    print("10 most common words:", fdist.most_common(10))
    # Plot the 30 most common words
    fdist.plot(30, cumulative=False)


# Create a frequency distribution
freqDist_plot(tokens)

# Load and preprocess the text
with open('1984.txt', 'r', encoding='utf-8') as file:
    text = file.read()

text = text.lower()  # Convert to lowercase
text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation

# Tokenize the text
tokens = word_tokenize(text)

freqDist_plot(tokens)
