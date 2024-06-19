from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.classify.util import accuracy
from nltk.metrics import precision, recall, f_measure
from nltk import FreqDist, BigramAssocMeasures, BigramCollocationFinder
from collections import defaultdict
import random
import collections

# recall
# True Positives (TP) / (True Positives (TP) + False Negatives (FN))
# Example data
refset = defaultdict(set)
testset = defaultdict(set)

# Assume refsets and testsets are filled with reference (actual) and test (predicted) labels
# Example:
refset['pos'] = {4, 2, 1, 5}
testset['pos'] = {1, 2, 3, 4, 7}

# Calculate recall for the positive class
pos_recall = recall(refset['pos'], testset['pos'])
print(f'Recall for positive class: {pos_recall:.2f}')

# precision
# True Positives (TP) / (True Positives (TP) + False Positives (FP))
# Calculate precision for the positive class
pos_precision = precision(refset['pos'], testset['pos'])
print(f'Precision for positive class: {pos_precision:.2f}')

# F-measure or F1-score
# The F1-score is the harmonic mean of precision and recall. It is calculated as follows
# F1-Score = 2 x (precision x recall) / (precision + recall)
pos_f1 = f_measure(refset['pos'], testset['pos'])
print(f'F1-score for positive class: {pos_f1:.2f}')


def extract_features(words):
    return dict([(word, True) for word in words])


reviews = [(list(movie_reviews.words(fileid)), category)
           for category in movie_reviews.categories()
           for fileid in movie_reviews.fileids(category)]
random.shuffle(reviews)

featuresets = [(extract_features(d), c) for (d, c) in reviews]
train_set, test_set = featuresets[:1900], featuresets[1900:]
classifier = NaiveBayesClassifier.train(train_set)

# Evaluate the classifier
print(f'Accuracy: {accuracy(classifier, test_set):.3f}')

# classifying new text
new_review = "This movie was amazing with great acting and plot."
new_features = extract_features(new_review.split())
print(classifier.classify(new_features))

# Accuracy
print(f'Accuracy: {accuracy(classifier, test_set):.3f}')

# Precision, Recall, F-measure
refsets = collections.defaultdict(set)
testsets = collections.defaultdict(set)

for i, (feats, label) in enumerate(test_set):
    refsets[label].add(i)
    observed = classifier.classify(feats)
    testsets[observed].add(i)

print(f'Positive Precision: {precision(refsets['pos'], testsets['pos']):.3f}')
print(f'Positive Recall: {recall(refsets['pos'], testsets['pos']):.3f}')
print(f'Positive F-measure: {f_measure(refsets['pos'], testsets['pos']):.3f}')
print(f'Negative Precision: {precision(refsets['neg'], testsets['neg']):.3f}')
print(f'Negative Recall: {recall(refsets['neg'], testsets['neg']):.3f}')


def bigram_word_features(words, score_fn=BigramAssocMeasures.chi_sq, n=200):
    bigram_finder = BigramCollocationFinder.from_words(words)
    bigrams = bigram_finder.nbest(score_fn, n)
    return dict([(ngram, True) for ngram in words + bigrams])


# Use the new feature extraction method
featuresets = [(bigram_word_features(d), c) for (d, c) in reviews]
train_set, test_set = featuresets[:1900], featuresets[1900:]

# Train the classifier with the new features
classifier = NaiveBayesClassifier.train(train_set)
print(f'Accuracy with bigrams: {accuracy(classifier, test_set):.3f}')
