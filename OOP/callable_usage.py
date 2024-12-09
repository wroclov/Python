'''

Why Use Callable Objects?
Callable objects offer a blend of functionality and data encapsulation that is hard to achieve through functions alone.
They enable:

* Stateful Functions: By using callable class instances, you can create functions that remember state across calls.
* Customizable Behavior: Callable objects can be customized upon creation through constructor arguments,
allowing similar functions to behave differently based on those arguments.
* Object-Oriented Callbacks: Callable objects can be passed as callbacks to functions or event handlers,
providing a way to include context or state in the callback action.
'''
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return  x * self.factor

double = Multiplier(2)
print(double(7))
triple = Multiplier(3)
print(triple("Hallo_"))

# checking callability
print(callable(double))
print(callable("string"))

# you can call various types in python

# Regular function
def add(x ,y):
    return x + y

# Lambda function
power = lambda x, y: x ** y

# class with an Instance method
class Greeter:
    def greet(self, name):
        return f"Hello, {name}!"

# Callable Class (Using the initializer)
class Counter:
    def __init__(self, start = 0):
        self.value = start
# Instance with __call__ Method
class Repeater:
    def __call__(self, message, times=1):
        return (message + ' ') * times

# using build-in function (e.g. len)
# len is a callable object that returns the length of an object

# Generator Function
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Demonstrating each callable
print(add(2, 3))
print(power(2, 3))

greeter = Greeter()

print(greeter.greet("World"))

counter = Counter(12)
print(counter.value)

repeater = Repeater()
print(repeater("Echoing", 4))

print(len("Czesc"))

# using a generator function
for number in countdown(4):
    print(number)