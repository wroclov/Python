

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    def __repr__(self):
        return f"title={self.title},author={self.author},price={self.price}"


b1 = Book("Peace and War", "Leo Tolstoy", 44.4)
b2 = Book("Ogniem i mieczem", "Henry Sienkiewicz", 36)

print(b1)
print(b2)

print(str(b1))
print(repr(b1))