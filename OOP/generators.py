from memory_profiler import profile
from typing import Generator, Dict, Callable, Any

import random
import time

names = ['Tytus', 'Adrian', 'Max', 'Sylwester', 'Tomasz']
majors = ['Math', 'Biology', 'Engineering', 'Chemistry', 'Art']

@profile
def build_list(num_people: int) -> list:
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result

@profile
def build_generator(num_people: int) -> Generator[Dict[str, str], None, None]:
    for i in range(num_people):
        yield {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }

@profile
def consume_generator(generator: Generator[Dict[str, str], None, None]) -> None:
    for _ in generator:
        pass

def measure(func: Callable[..., Any], *args: Any) -> Any:
    """
    Measures the execution time of a given function.

    :param func: The function to measure.
    :param args: Positional arguments to pass to the function.
    :return: The result of the function execution.
    """
    t1 = time.time()
    people = func(*args)
    t2 = time.time()
    print(f"{func.__name__} executing took {t2 - t1:.2f} seconds")
    return people

if __name__ == "__main__":
    # Profile list creation
    measure(build_list, 1_000_000)

    # Profile generator creation and consumption
    gen_people = measure(build_generator, 1_000_000)
    measure(consume_generator, gen_people)

    # Demonstrating generator vs list
    print("\n\n### Basics are below:")

    # Generator expression
    gen_squares = (x * x for x in range(1, 6))
    print(f"Generator example: {list(gen_squares)} converted to list")

    # List comprehension
    list_squares = [x * x for x in range(1, 6)]
    print(f"List comprehension example: {list_squares}")

    # Generator function
    def square_numbers(nums):
        for i in nums:
            yield i * i

    my_nums = square_numbers([1, 2, 3, 4, 5])
    print(f"Square numbers using generator: {list(my_nums)}")
