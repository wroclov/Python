
from dataclass import dataclass

# the 'frozen' parameter makes the class immutable
@dataclass(frozen=True)
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def some_func(self, newval):
        self.value2 = newval


obj = ImmutableClass()
print(obj.value1, obj.value2)

# trying updating immutable object
# obj.value1 = "Other String"
# print(obj.value1, obj.value2)

# however you can modify/assign new values for parameters in instantization

obj2 = ImmutableClass("Weird string", 77)

print(obj2.value1, obj2.value2)


# trying modification within class functions won't work also --> exception
obj.some_func(22)
print(obj.value1, obj.value2)