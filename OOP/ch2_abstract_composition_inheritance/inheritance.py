
class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Periodical(Publication):
    def __init__(self, title, publisher, price,  period):
        super().__init__(title,price)
        self.period = period
        self.publisher = publisher


class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title,price)
        self.author = author
        self.pages = pages


class Magazine(Periodical ):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price,  period)


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price,  period)

b1 = Book('Quo Vadis', 'Zerosmki', 300, 55.4)
n1 = Newspaper("Wyborcza", 'Agora', 5.50, 'Daily')
m1 = Magazine('Samochody', 'Pegasus', 22.0,'Monthly')

print(b1.author)
print(n1.publisher)
print(b1.price, n1.price, m1.price)