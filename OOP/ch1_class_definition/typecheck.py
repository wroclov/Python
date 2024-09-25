

class Book:
    def __init__(self,title):
        self.title = title

class Newspaper:
    def  __init__(self,name):
        self.name = name

b1 = Book('Ogniem i mieczem')
b2 = Book('Programming for newbies')
n1 = Newspaper('Wyborcza')
n2 = Newspaper('Rzeczpospolita')

# check type of object
print(type(b1))
print(type(n1))

# compare two diff types
print(type(b1) == type(b2))
print(type(b1) == type(n2))

# check if object is of particular type

print(isinstance(b1,Book))
print(isinstance(n1,Newspaper))
print(isinstance(n2,Book))

# we can even check if n2 belongs to generic, yes it always inherits
print(isinstance(n2, object))