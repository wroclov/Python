

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

# we can use getattribute for instance to calculate automatic discount
    def __getattribute__(self, name):
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(name)

# we can
    def __setattr__(self, name, value):
        if name == "price":
            if type(value) is not float:
                raise ValueError("The 'price' attr must be a float")
        return super().__setattr__(name, value)

    # __getattr__ is called when __getatributte__ lookup fails
    # you can pretty much generate attributes on the fly with this method
    def __getattr__(self, name):
        return name + " is not here"

b1 = Book("Peace and War", "Leo Tolstoy", 44.54)
b2 = Book("Quo Vadis", "Henry Sienkiewicz ", 36.75)

print(b1)
#b1.price = 57

b1.price = 57.8
print(b1)

print(b1.randomprop)


