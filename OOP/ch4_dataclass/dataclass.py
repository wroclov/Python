from dataclasses import dataclass

#dataclass is new feature, you don't need to provide __init__ function explicitly anymore
@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def bookinfo(self):
        return f"{self.title} by {self.author}"


b1 = Book("Peace and War", "Leo Tolstoy", 1225, 44.54)
b2 = Book("Quo Vadis", "Henry Sienkiewicz ", 700, 36.75)
b3 = Book("Quo Vadis", "Henry Sienkiewicz ", 700, 36.75)

print(b1.title)
print(b1.author)

#dataclass provides automatic __eq__ and __str__ and __repr__ functions
print(b1)

print(b1 == b2)
print(b3 == b2)

b1.title = "War and peace"
b1.pages = 229
print(b1.bookinfo())