from collections.abc import Callable


def gen_args(func: Callable) -> None:
    func()


def run(func: Callable[[int], None], n: int) -> None:
    func(n)


def print_int(n: int) -> None:
    print(f"Printing: {n}")


run(print_int, 6)


def two_arg(func: Callable[[int, int], None], a: int, b: int) -> None:
    func(a, b)


def add(a: int, b: int) -> None:
    print(a + b)


two_arg(add, 7, 55)

def no_arg(func: Callable[[], bool]) -> None:
    result: bool = func()
    print(result)

def is_online() -> bool:
    return True

no_arg(is_online)

def mixed(func: Callable[[str, int], str], n: int) -> None:
    char: str = 'x_'
    result: str = func(char, n)
    print(result)

def multiply_text(text: str, amount: int) -> str:
    return text * amount

mixed(multiply_text, 10)


def mixed(func: Callable[..., None], *args: int) -> None:
    func(*args)

mixed(print, 2, 3 , 4 ,7)

multiply: Callable[[int, str], str] = lambda n, text: n * text

print(multiply( 4, "jane"))
