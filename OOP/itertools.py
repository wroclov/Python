from itertools import (
    product, permutations, combinations, combinations_with_replacement,
    accumulate, groupby, count, cycle, repeat
)
import operator


def demo_product():
    a = [1, 2]
    b = [3, 4]
    print("Product Example:")
    print(f"Product of {a} and {b}: {list(product(a, b))}")

    c = [1, 2]
    d = [3]
    print(f"Product of {c} and {d}, with 2 repeat: {list(product(c, d, repeat=2))}")
    print("-" * 30)


def demo_permutations():
    a = [1, 2, 3]
    print("Permutations Example:")
    print(f"Permutations of {a}: {list(permutations(a))}")
    print(f"Permutations of {a} with 2 repeats: {list(permutations(a, 2))}")
    print("-" * 30)


def demo_combinations():
    a = [1, 2, 3, 4]
    print("Combinations Example:")
    print(f"Combinations of {a}: {list(combinations(a, 2))}")
    print(f"Combinations of {a}, with replacement: {list(combinations_with_replacement(a, 2))}")
    print("-" * 30)


def demo_accumulate():
    a = [1, 2, 3, 4, 5, 3, 2]
    print("Accumulate Example:")
    print(f"Original List: {a}")
    print(f"Sum Accumulate: {list(accumulate(a))}")
    print(f"Multiplication Accumulate: {list(accumulate(a, func=operator.mul))}")
    print(f"Max Accumulate: {list(accumulate(a, func=max))}")
    print("-" * 30)


def demo_groupby():
    def is_smaller_than_three(x):
        return x < 3

    lst = [1, 2, 3, 4, 5, 3, 2]
    print(f"groupby example for {lst}, grouping by is_smaller_than_three:")
    group_obj = groupby(lst, key=is_smaller_than_three)
    for key, value in group_obj:
        print(f"Key: {key}, Values: {list(value)}")

    print(f"groupby example for {lst}, grouping by key=lambda x: x < 4:")
    group_obj2 = groupby(lst, key=lambda x: x < 4)
    for key, value in group_obj2:
        print(f"Key: {key}, Values: {list(value)}")

    persons = [
        {'name': 'Tim', 'age': 25}, {'name': 'Max', 'age': 27},
        {'name': 'Adam', 'age': 41}, {'name': 'Tom', 'age': 30},
        {'name': 'Ray', 'age': 27}, {'name': 'Aga', 'age': 25}
    ]
    print(f"groupby example for {persons}, grouping by key=lambda x: x['age']:")
    # Sort the list by age before grouping
    sorted_persons = sorted(persons, key=lambda x: x['age'])
    group_obj3 = groupby(sorted_persons, key=lambda x: x['age'])
    for key, value in group_obj3:
        print(f"Age: {key}, Persons: {list(value)}")
    print("-" * 30)


def demo_count():
    print("Count Example:")
    for i in count(10):
        print(i)
        if i == 15:
            break
    print("-" * 30)


def demo_repeat_cycle():
    print("Repeat and Cycle Example:")
    for i in repeat(7, 4):
        print(i)

    a = [1, 22, 3]
    for i, elem in enumerate(cycle(a)):
        print(elem)
        if i >= 5:  # Limit to avoid infinite loop
            break
    print("-" * 30)


if __name__ == "__main__":
    demo_product()
    demo_permutations()
    demo_combinations()
    demo_accumulate()
    demo_groupby()
    demo_count()
    demo_repeat_cycle()
