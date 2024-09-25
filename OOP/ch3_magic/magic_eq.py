

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Can't compare book to non-book object")

        return (self.title == other.title and
                self.author == other.author and
                self.price == other.price)

    def __ge__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Can't compare book to non-book object")

        return self.price >= other.price

    def __lt__(self, other):
        if not isinstance(other, Book):
            raise ValueError("Can't compare book to non-book object")

        return self.price < other.price

b1 = Book("Peace and War", "Leo Tolstoy", 44.4)
b2 = Book("Quo Vadis", "Henry Sienkiewicz ", 36.7)
b3 = Book("Quo Vadis", "Henry Sienkiewicz ", 36.7)
b4 = Book("Czarnoksiężnik z Krainy Oz", "Lyman Frank Baum", 39)

print(b3 == b4)
print(b3 == b2)

print(b3 >= b2)
print(b3 < b2)

## with gt, lt we can sort objects !! 

books = [b1, b2, b3, b4]
books.sort()
print([book.title for book in books])

#print(b3==43)