from nltk.corpus import wordnet as wn


def get_synsets(word):
    """Retrieve and print synsets for a given word."""
    synsets = wn.synsets(word)
    print(f"Synsets for '{word}':", synsets)
    return synsets


def print_synset_details(synset):
    """Print the details of a given synset."""
    print(f"\nSynset: {synset.name()}")
    print(f"Definition: {synset.definition()}")
    print(f"Examples: {synset.examples()}")


def print_semantic_relationships(synset):
    """Print semantic relationships of a given synset."""
    print(f"\nHypernyms of {synset.name()}: {synset.hypernyms()}")
    print(f"Hyponyms of {synset.name()}: {synset.hyponyms()}")
    print(f"Meronyms of {synset.name()}: {synset.part_meronyms()}")
    print(f"Holonyms of {synset.name()}: {synset.member_holonyms()}")


def provide_synsets(word):
    """Provide synset details and semantic relationships for a given word."""
    synsets = get_synsets(word)
    for synset in synsets:
        print_synset_details(synset)
    if synsets:
        first_synset = synsets[0]
        print_semantic_relationships(first_synset)


def get_synonyms_antonyms(word):
    """Get synonyms and antonyms for a given word."""
    synset = wn.synset(word)
    synonyms = [lemma.name() for lemma in synset.lemmas()]
    antonyms = [lemma.antonyms()[0].name() for lemma in synset.lemmas() if lemma.antonyms()]
    return synonyms, antonyms


def main():
    provide_synsets("horse")
    provide_synsets("car")

    synonyms, antonyms = get_synonyms_antonyms('good.a.01')
    print("\nSynonyms for 'good':", synonyms)
    print("Antonyms for 'good':", antonyms)


if __name__ == "__main__":
    main()
