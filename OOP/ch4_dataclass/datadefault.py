
from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20,40))

# you can use also default_factory which will take function to generate
# value of your parameters
@dataclass
class Book:
    title: str = "No Title"
    author: str = "No Author"
    pages: int = field(default = 0)
    price: float = field(default_factory = price_func)

b1=Book()
print(b1)
b2 = Book("Peace and War", "Leo Tolstoy", 1225)
b3 = Book("Quo Vadis", "Henry Sienkiewicz ", 700)

print(b2)
print(b3)