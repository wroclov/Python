import nltk
from nltk.corpus import wordnet as wn


# Find synsets for the word 'car'
synsets = wn.synsets('horse')
print("Synsets for 'horse':", synsets)

# Get definitions and examples for each synset
for synset in synsets:
    print(f"\nSynset: {synset.name()}")
    print(f"Definition: {synset.definition()}")
    print(f"Examples: {synset.examples()}")

# Accessing semantic relationships
car = wn.synset('horse.n.01')

# Hypernyms
print("\nHypernyms:", car.hypernyms())

# Hyponyms
print("\nHyponyms:", car.hyponyms())

# Meronyms
print("\nMeronyms:", car.part_meronyms())

# Holonyms
print("\nHolonyms:", car.member_holonyms())

# Synonyms and antonyms for 'good'
good = wn.synset('good.a.01')
synonyms = [lemma.name() for lemma in good.lemmas()]
antonyms = [lemma.antonyms()[0].name() for lemma in good.lemmas() if lemma.antonyms()]

print("\nSynonyms for 'good':", synonyms)
print("Antonyms for 'good':", antonyms)
