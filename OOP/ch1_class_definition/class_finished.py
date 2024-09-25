

class Book:
    # properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    # double underscore properties are hidden from other classes
    __booklist = None

    # create a class method
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES
    # create a static method
    def getBooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist


    def setTitle(self,newtitle):
        self.title = newtitle

    def __init__(self,title, booktype):
        self.title = title
        if not booktype in Book.BOOK_TYPES:
            raise ValueError("Book type is not valid book type")
        else:
            self.booktype = booktype

print("Book types", Book.get_book_types())
b1 = Book('Title1','HARDCOVER')
b2 = Book('Title2','EBOOK')

#b3 = Book('Title3','Comic')

theBooks = Book.getBooklist()
theBooks.append(b1)
theBooks.append(b2)
print(theBooks)


