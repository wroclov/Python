#!/usr/bin/env python3

import string
from collections import Counter

import nltk
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.chunk import ne_chunk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import bigrams


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
print("Entities written to file.")



tokens = nltk.word_tokenize(text)
bigram_measures = BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(tokens)
finder.apply_freq_filter(3)  # Only consider bigrams that occur at least 3 times
# Score bigrams by their frequency
scored = finder.score_ngrams(bigram_measures.raw_freq)

# Write the bigrams and their scores
with open('bigrams_nlp_stats.txt', 'w') as file:
    for bigram, score in scored:
        file.write(f'{bigram}: {score}\n')


# Pointwise Mutual Information (PMI) is a statistical measure used to evaluate the association between two words in a
# bigram. It measures how much more often the two words co-occur than would be expected by chance.
# common bigrams
bigrams= finder.nbest(bigram_measures.pmi, 10)
print(f"10 most frequent bigrams by PMI")
print(bigrams)

pmi_bigrams = finder.score_ngrams(bigram_measures.pmi)

# Get the top 10 bigrams by PMI score
top_10_pmi_bigrams = sorted(pmi_bigrams, key=lambda x: x[1], reverse=True)[:10]

# Print the top 10 bigrams with their PMI scores
print("Top 10 bigrams by PMI with scores:")
for bigram, score in top_10_pmi_bigrams:
    print(f"Bigram: {bigram}, Score: {score}")

# Get the top 10 bigrams by Student's t-test
t_test_bigrams = finder.nbest(bigram_measures.student_t, 10)
print("Top 10 bigrams by Student's t-test:", t_test_bigrams)

t_test_bigrams = finder.score_ngrams(bigram_measures.student_t)

# Get the top 10 bigrams by t-test score
top_10_t_test_bigrams = sorted(t_test_bigrams, key=lambda x: x[1], reverse=True)[:10]

# Print the top 10 bigrams with their t-test scores
print("Top 10 bigrams by Student's t-test with scores:")
for bigram, score in top_10_t_test_bigrams:
    print(f"Bigram: {bigram}, Score: {score}")

# The Chi-squared test helps identify pairs of words that occur together more frequently than would be expected by
# chance. This is useful for various NLP tasks, such as identifying collocations, improving language models,
# and enhancing text analysis. Get the top 10 bigrams by Chi-squared test
chi_sq_bigrams = finder.nbest(bigram_measures.chi_sq, 10)
print("Top 10 bigrams by Chi-squared test:", chi_sq_bigrams)

# Get the scored bigrams by Chi-squared test
scored_bigrams = finder.score_ngrams(bigram_measures.chi_sq)

# Get the top 10 bigrams by Chi-squared score
top_10_bigrams = sorted(scored_bigrams, key=lambda x: x[1], reverse=True)[:10]

# Interpretation Each bigram is listed with its Chi-squared score, which reflects the strength of association between
# the words in the bigram. Higher scores indicate a stronger association. This metric can be used to make informed
# decisions about which bigrams are more significant in the text, aiding in tasks such as keyword extraction,
# language modeling, and text analysis. Print the top 10 bigrams with their Chi-squared scores
print("Top 10 bigrams by Chi-squared test with scores:")
for bigram, score in top_10_bigrams:
    print(f"Bigram: {bigram}, Score: {score}")

# Get the top 10 bigrams by Likelihood Ratio
likelihood_bigrams = finder.nbest(bigram_measures.likelihood_ratio, 10)
print("Top 10 bigrams by Likelihood Ratio:", likelihood_bigrams)

likelihood_bigrams = finder.score_ngrams(bigram_measures.likelihood_ratio)

# Get the top 10 bigrams by Likelihood Ratio score
top_10_likelihood_bigrams = sorted(likelihood_bigrams, key=lambda x: x[1], reverse=True)[:10]

# Print the top 10 bigrams with their Likelihood Ratio scores
print("Top 10 bigrams by Likelihood Ratio with scores:")
for bigram, score in top_10_likelihood_bigrams:
    print(f"Bigram: {bigram}, Score: {score}")

# Get the top 10 bigrams by Jaccard Index
jaccard_bigrams = finder.nbest(bigram_measures.jaccard, 10)
print("Top 10 bigrams by Jaccard Index:", jaccard_bigrams)

jaccard_bigrams = finder.score_ngrams(bigram_measures.jaccard)

# Get the top 10 bigrams by Jaccard score
top_10_jaccard_bigrams = sorted(jaccard_bigrams, key=lambda x: x[1], reverse=True)[:10]

# Print the top 10 bigrams with their Jaccard scores
print("Top 10 bigrams by Jaccard Index with scores:")
for bigram, score in top_10_jaccard_bigrams:
    print(f"Bigram: {bigram}, Score: {score}")


# Calculate top 10 bigrams for each measure
chi_sq_bigrams = sorted(finder.score_ngrams(bigram_measures.chi_sq),key=lambda x: x[1], reverse=True)[:10]
pmi_bigrams = sorted(finder.score_ngrams(bigram_measures.pmi),key=lambda x: x[1], reverse=True)[:10]
t_test_bigrams = sorted(finder.score_ngrams(bigram_measures.student_t),key=lambda x: x[1], reverse=True)[:10]
likelihood_bigrams = sorted(finder.score_ngrams(bigram_measures.likelihood_ratio),key=lambda x: x[1], reverse=True)[:10]
jaccard_bigrams = sorted(finder.score_ngrams(bigram_measures.jaccard),key=lambda x: x[1], reverse=True)[:10]

# Helper function to print the top 10 bigrams with scores
def print_top_bigrams(title, bigrams):
    print(f"\nTop 10 bigrams by {title} with scores:")
    for bigram, score in bigrams:
        print(f"Bigram: {bigram}, Score: {score}")

# Print results
print_top_bigrams("Chi-squared test", chi_sq_bigrams)
print_top_bigrams("PMI", pmi_bigrams)
print_top_bigrams("Student's t-test", t_test_bigrams)
print_top_bigrams("Likelihood Ratio", likelihood_bigrams)
print_top_bigrams("Jaccard Index", jaccard_bigrams)





# Function to calculate scores for top 10 bigrams
def calculate_top_bigrams_scores(finder, measure):
    # Calculate scores for the measure
    scores = finder.score_ngrams(measure)
    # Sort scores by score value in descending order
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    # Return only the top 10 bigrams with their scores
    return sorted_scores[:10]


# Function to collect occurrence count and rank for top 10 bigrams
def collect_occurrence_and_rank(top_bigrams):
    # Dictionary to store occurrence count
    bigram_occurrences = {}

    # Count occurrences
    for bigram, score in top_bigrams:
        if bigram not in bigram_occurrences:
            # Initialize occurrence count to 0
            bigram_occurrences[bigram] = 0
        # Get the frequency of the bigram in the original text
        bigram_occurrences[bigram] += finder.ngram_fd[bigram]

    # Rank bigrams by score
    ranked_bigrams = sorted(top_bigrams, key=lambda x: x[1], reverse=True)

    # Return ranked bigrams with occurrence count
    ranked_bigrams_with_occurrence = []
    for rank, (bigram, score) in enumerate(ranked_bigrams, start=1):
        ranked_bigrams_with_occurrence.append({
            'Rank': rank,
            'Bigram': bigram,
            'Score': score,
            'Occurrences': bigram_occurrences.get(bigram, 0)
        })

    return ranked_bigrams_with_occurrence


# Calculate top 10 bigrams for each measure
top_chi_sq_bigrams = calculate_top_bigrams_scores(finder, bigram_measures.chi_sq)
top_pmi_bigrams = calculate_top_bigrams_scores(finder, bigram_measures.pmi)
top_t_test_bigrams = calculate_top_bigrams_scores(finder, bigram_measures.student_t)
top_likelihood_bigrams = calculate_top_bigrams_scores(finder, bigram_measures.likelihood_ratio)
top_jaccard_bigrams = calculate_top_bigrams_scores(finder, bigram_measures.jaccard)

# Collect occurrence count and ranking for each measure
chi_sq_ranked = collect_occurrence_and_rank(top_chi_sq_bigrams)
pmi_ranked = collect_occurrence_and_rank(top_pmi_bigrams)
t_test_ranked = collect_occurrence_and_rank(top_t_test_bigrams)
likelihood_ranked = collect_occurrence_and_rank(top_likelihood_bigrams)
jaccard_ranked = collect_occurrence_and_rank(top_jaccard_bigrams)


def print_ranked_bigram_stats(title, measure_ranked):
    print(f"Ranking based on "+title+":")
    for entry in measure_ranked:
        print(entry)

# Print results for each measure
print_ranked_bigram_stats("Chi-squared test",chi_sq_ranked)
print_ranked_bigram_stats("PMI",pmi_ranked)
print_ranked_bigram_stats("Student's t-test",t_test_ranked)
print_ranked_bigram_stats("Likelihood Ratio",likelihood_ranked)
print_ranked_bigram_stats("Jaccard Index",jaccard_ranked)


with open('Jaccard_Index.txt', 'w') as file:
    for entry in jaccard_ranked:
        file.write(f'{entry}\n')
