

print(range(1,5))
print(*range(1,5))

lista = (1, 2, 3, 4)
head, *tail = lista
print(head)
print(tail)

mydict = {'a': 1, 'b': 2, 'c': 3}
print(*mydict)
# print(**mydict) # error
# To use the ** unpacking properly, it must be used with a function that accepts keyword arguments

def myfunc(a, b, c):
    print(a, b, c)

mydict = {'a': 1, 'b': 2, 'c': 3}
myfunc(*mydict)
myfunc(**mydict)