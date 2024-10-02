#!/usr/bin/env python3

import string
from collections import Counter
import nltk
from nltk import bigrams
from nltk.chunk import ne_chunk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

# Load and preprocess the text
with open('1984.txt', 'r', encoding='utf-8') as file:
    text = file.read()

text = text.lower()  # Convert to lowercase
text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation

# Tokenize the text
words = word_tokenize(text)

# Remove stopwords
stopwords_en = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stopwords_en]

# Calculate word frequencies
word_counts = Counter(filtered_words)
total_words = sum(word_counts.values())

# Calculate the percentage for the most frequent words
most_common_words = word_counts.most_common(10)
most_common_words_percentage = [(word, count / total_words * 100, count) for word, count in most_common_words]

# Display the results
print("Total words:", total_words)
print("10 most common words")
for word, percentage, count in most_common_words_percentage:
    print(f"{word}: {percentage:.3f}% : {count}")

# Perform POS tagging
tagged = nltk.pos_tag(words)

# Perform Named Entity Recognition (NER)
entities = ne_chunk(tagged)

# Write named entities to a file
with open('entities_nlp_example.txt', 'w') as file:
    for chunk in entities:
        if hasattr(chunk, 'label'):  # Check if the chunk is a named entity
            entity_name = ' '.join(c[0] for c in chunk.leaves())  # Join words to form the entity name
            entity_type = chunk.label()  # Get the entity type
            file.write(f'{entity_name}: {entity_type}\n')
print("Entities written to file.\n")

# Bigram analysis
finder = BigramCollocationFinder.from_words(filtered_words)
finder.apply_freq_filter(3)  # Only consider bigrams that occur at least 3 times

# Pointwise Mutual Information (PMI) is a statistical measure used to evaluate the association between two words in a
# bigram. It measures how much more often the two words co-occur than would be expected by chance.

bigram_measures = BigramAssocMeasures()
scored_bigrams = {
    "PMI": finder.score_ngrams(bigram_measures.pmi),
    "Chi-squared": finder.score_ngrams(bigram_measures.chi_sq),
    "Student's t-test": finder.score_ngrams(bigram_measures.student_t),
    "Likelihood Ratio": finder.score_ngrams(bigram_measures.likelihood_ratio),
    "Jaccard": finder.score_ngrams(bigram_measures.jaccard)
}


# Function to print top 10 bigrams with scores
def print_top_bigrams(title, bigrams):
    print(f"\nTop 10 bigrams by {title} with scores:")
    for bigram, score in bigrams[:10]:
        print(f"Bigram: {bigram}, Score: {score}")


# Print and save top bigrams
for measure, scored in scored_bigrams.items():
    scored_sorted = sorted(scored, key=lambda x: x[1], reverse=True)
    print_top_bigrams(measure, scored_sorted)
    with open(f'{measure}_bigrams.txt', 'w') as file:
        for bigram, score in scored_sorted[:10]:
            file.write(f"Bigram: {bigram}, Score: {score}\n")


# Function to collect occurrence count and rank for top 10 bigrams
def collect_occurrence_and_rank(top_bigrams, finder):
    bigram_occurrences = {bigram: finder.ngram_fd[bigram] for bigram, _ in top_bigrams}
    ranked_bigrams_with_occurrence = [
        {'Rank': rank, 'Bigram': bigram, 'Score': score, 'Occurrences': bigram_occurrences[bigram]}
        for rank, (bigram, score) in enumerate(top_bigrams, start=1)
    ]
    return ranked_bigrams_with_occurrence


# Collect and print occurrence count and ranking for each measure
for measure, scored in scored_bigrams.items():
    top_bigrams = sorted(scored, key=lambda x: x[1], reverse=True)[:10]
    ranked_bigrams = collect_occurrence_and_rank(top_bigrams, finder)
    print(f"\nRanking based on {measure}:")
    for entry in ranked_bigrams:
        print(entry)
