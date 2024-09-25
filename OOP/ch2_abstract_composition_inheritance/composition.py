


class Book:
    def __init__(self, title, price, author = None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result

class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"

class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount


auth = Author("Henryk", "Sienkiewicz")
b1 = Book('Quo Vadis', 56.9, auth)
b1.addchapter(Chapter("Poczatek", 57))
b1.addchapter(Chapter("Rzym", 37))
b1.addchapter(Chapter("Pozar", 24))

print(b1.title)
print(b1.author)
print(b1.getbookpagecount())