

class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name = 'Class A'

class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name = "Class B"

class C(B, A):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.prop1)
        print(self.prop2)
        print(self.name)

c = C()

#for self.name there might be confusion, because order matters in inheritance
c.showprops()
print(C.__mro__)