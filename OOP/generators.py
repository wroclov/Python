# big diff in performance between list and generators
from memory_profiler import profile

import random
import time

names = ['Tytus', 'Adrian', 'Max', 'Sylwester', 'Tomasz']
majors = ['Math', 'Biology', 'Engineering', 'Chemistry', 'Art']
@profile
def build_list(num_people: int) -> list:
    result = []
    for i in range(num_people):
        person = {
                'id' : i,
                'name': random.choice(names),
                'major': random.choice(majors)
                }
        result.append(person)
    return result

@profile
def build_generator(num_people: int) :
    for i in range(num_people):
        person = {
                'id' : i,
                'name': random.choice(names),
                'major': random.choice(majors)
                }
        yield person

@profile
def consume_generator(generator):
    for x in generator:
        pass

def measure(func, num_people):
    t1 = time.time()
    people = func(num_people)
    t2 = time.time()
    print(f"{func} executing took {t2-t1} seconds")
    return people

if __name__ == "__main__":
    measure(build_list, 1_000_000)
    gen_people = measure(build_generator, 1_000_000)
    # in fact mem profiling will be calculated only when real usage of generator is made
    # generators are not allocating mem until used, they are more efficient than list
    t1 = time.time()
    consume_generator(gen_people)
    t2 = time.time()
    print(f"{consume_generator} executing took {t2 - t1} seconds")



    # simplistic examples below
    print("\n\n Basics are below:")
    gen_squares =(x*x for x in range(1, 6))
    print(gen_squares)

    list_squares = [x*x for x in range(1, 6)]
    print(list_squares)
    for elem in list_squares:
        print(elem)

    # conversion to list
    print(list(gen_squares), "converted to list")

    def square_numbers(nums):
        for i in nums:
            yield (i * i)

    my_nums = square_numbers([1,2,3,4,5])
    print(my_nums)
    for num in my_nums:
        print(num)

