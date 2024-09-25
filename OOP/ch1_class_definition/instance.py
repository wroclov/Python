
class Book:
    def __init__ (self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is secret attribute"
    def getPrice(self):
        if hasattr(self,"_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setDiscount(self,amount):
        self._discount = amount




book1 =  Book('W pustyni i w puszczy' ,'Sienkiewicz' ,250 ,55.8)
book2 =  Book('Quo Vadis' ,'Zeromski' ,100 ,44.78)

print(book1)
print(book1.title)
print(book1.getPrice())
book1.setDiscount(0.25)
print(book1.getPrice())

## not perfect to hide it, because ...
print(book1._Book__secret)

print(book1.__secret)
