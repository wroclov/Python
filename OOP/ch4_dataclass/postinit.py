
from dataclasses import dataclass

#dataclass is new feature, you don't need to provide __init__ function explicitly anymore
@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"


b1 = Book("Peace and War", "Leo Tolstoy", 1225, 44.54)
b2 = Book("Quo Vadis", "Henry Sienkiewicz ", 700, 36.75)
b3 = Book("Quo Vadis", "Henry Sienkiewicz ", 700, 36.75)

print(b1.description)
print(b2.description)