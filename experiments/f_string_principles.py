from datetime import datetime
name: str = ('Wroclaw')
age: int = 67

print('Name: ' + name, 'Age: ' + str(age))

print(f'Name: {name} Age: {age}, you can also calculate 2+3: {2+3}')

var: int = 100

#good for quick debugging
print(f'{var=}')
print(f'{isinstance(var, int)=}')
print(f'{6*7=}')
print(f'{6 * 7 = }')

decimal: float = 1234.5678
percent: float = .56789
print(f'{decimal:.2f}')
print(f'{percent:.2%}')

big_number: int = 1_000_000_000
print(big_number)

#only 2 options for distinguishing thousands
print(f'{big_number:,}')
print(f'{big_number:_}')

f_big_number: int = 1_000_000_000.89432
print(f'{f_big_number:,.2f}')

now: datetime = datetime.now()
print(f'{now}')
print(f'{now:%x}')
print(f'{now:%c}')
print(f'{now:%H:%M:%S}')

something: str = 'text\boółdjks\t'
something_raw: str = r'text\boółdjks\t'
# in fact fr string not so useful for path, but might be good for writing regular expressions
path: str = fr'\User\{name}\Documents'

print(something)
print(something_raw)
print(path)

#nested f strings, no idea real use case?
print(f'{1 + 1} {f'{2+ 2}'}')

n: int = 20
#for formatting
print(f'{name:_>20}')
print(f'{name:_^{n}}')
print(f'{name:_<{n}}')

#default is space
print(f'{name:>{n}}')
print(f'{name:.^{n}}')
print(f'{name:,<{n}}')

class Text:
    def __init__(self, text: str) -> None:
        self.text = text

    def __format__(self, format_spec: str) -> str:
        match format_spec:
            case 'upper':
                return self.text.upper()
            case 'lower':
                return self.text.lower()
            case 'count':
                return str(len(self.text))
            case _:
                raise ValueError(f'Format specifier "{format_spec}" does not exist.')

# we can define and use own format specifiers
my_text: Text = Text('Wrocław')
print(f'{my_text:upper}')
print(f'{my_text:lower}')
print(f'{my_text:count}')
# below will provide ValueError as specified
print(f'{my_text:xyz}')
