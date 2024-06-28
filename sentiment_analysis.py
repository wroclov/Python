# Importing necessary libraries
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy
import random

# Download necessary NLTK data
nltk.download('vader_lexicon')
nltk.download('movie_reviews')

def analyze_sentiment(text):
    """Analyzes the sentiment of a given text using VADER."""
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    print(f"Sentiment for '{text}': {sentiment}")

def train_naive_bayes_classifier():
    """Trains a Naive Bayes classifier on the movie reviews dataset."""
    documents = [(list(movie_reviews.words(fileid)), category)
                 for category in movie_reviews.categories()
                 for fileid in movie_reviews.fileids(category)]
    random.shuffle(documents)
    all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
    word_features = list(all_words)[:2000]

    def document_features(document):
        document_words = set(document)
        features = {}
        for word in word_features:
            features[f'contains({word})'] = (word in document_words)
        return features

    featuresets = [(document_features(d), c) for (d, c) in documents]
    train_set, test_set = featuresets[100:], featuresets[:100]
    classifier = NaiveBayesClassifier.train(train_set)

    print(f"Naive Bayes Classifier Accuracy: {accuracy(classifier, test_set):.2f}")
    classifier.show_most_informative_features(5)

def main():
    """Main function to run sentiment analysis and train Naive Bayes classifier."""
    test_sentences = [
        "NLTK is a great library for Natural Language Processing",
        "NLTK is a chaotic and weak library for Natural Language Processing",
        "Today's weather is ok",
        "Today's weather is awesome"
    ]

    for sentence in test_sentences:
        analyze_sentiment(sentence)

    train_naive_bayes_classifier()

if __name__ == "__main__":
    main()
