

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # it can be used to call objects as a function
    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price



b1 = Book("Peace and War", "Leo Tolstoy", 44.54)
b2 = Book("Quo Vadis", "Henry Sienkiewicz ", 36.75)

print(b1)

# with defined __call__ you can call objects as a function, diff style
b1("Anna Karenina", "Leo Tolstoy", 44.54)
print(b1)