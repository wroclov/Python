
def sort_words(text: str):
    return " ".join(sorted(text.split(),key=str.casefold))

# poniewaz orginalny sort priorytetyzuje capital letters,
# dodalem kopie przed, posortowalem, odjalem kopie
def sort_word_hack(text: str):
    words = text.split()
    words = [w.lower() + w for w in words]
    words.sort()
    words = [w[len(w)//2:] for w in words]
    return " ".join(words)

print(sort_words('rzeka koala Choinka arbuz'))

print(sort_word_hack('rzeka koala Choinka arbuz'))