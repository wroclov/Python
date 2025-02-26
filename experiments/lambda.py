from functools import reduce

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = list(map(lambda x, y: x + y, list1, list2))
print(f"Summed Lists {list1} + {list2} -> {result}")  # Output: [5, 7, 9]

# Lists representing different score components
assignments = [80, 90, 85, 70]  # 30% weight
exams = [75, 85, 80, 65]        # 40% weight
projects = [90, 95, 88, 80]     # 20% weight
bonus = [5, 3, 4, 2]            # Extra points (10%)

# Compute final weighted scores using map
final_scores = list(map(lambda a, e, p, b: round(a * 0.3 + e * 0.4 + p * 0.2 + b * 0.1, 2),
                        assignments, exams, projects, bonus))
print(f"Final Scores {final_scores}")  # Output: [72.5, 80.3, 75.5, 63.2]

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared {numbers} -> {squared}")  # Output: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens {numbers} -> {evens}")  # Output: [2, 4, 6]

# Factorial
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"Factorial {numbers} -> {product}")  # Output: 120 (1 * 2 * 3 * 4 * 5)

numbers = [1, 2, 3, 4]
sum_of_squares = reduce(lambda x, y: x + y, map(lambda x: x ** 2, numbers))
print(f"Sum of Squares {numbers} -> {sum_of_squares}")  # Output: 30 (1^2 + 2^2 + 3^2 + 4^2)

words = ["apple", "banana", "cherry", "date"]
sorted_by_length = sorted(words, key=lambda x: len(x))
print(f"Sorted by Length {words} -> {sorted_by_length}")  # Output: ['date', 'apple', 'banana', 'cherry']

words = ["apple", "banana", "cherry", "date"]
sorted_by_second_letter = sorted(words, key=lambda x: x[1])
print(f"Sorted by Second Letter {words} -> {sorted_by_second_letter}")  # Output: ['banana', 'date', 'apple', 'cherry']

students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]
sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
print(f"Sorted Students by Score {students} -> {sorted_students}")
# Output: [{'name': 'Bob', 'score': 92}, {'name': 'Alice', 'score': 85}, {'name': 'Charlie', 'score': 78}]

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
paired = list(map(lambda x: f"{x[0]}: {x[1]}", zip(names, scores)))
print(f"Paired Names & Scores {list(zip(names, scores))} -> {paired}")  # Output: ['Alice: 85', 'Bob: 92', 'Charlie: 78']

numbers = [3, 5, 7, 9]
has_even = any(map(lambda x: x % 2 == 0, numbers))
print(f"Contains Even Number? {numbers} -> {has_even}")  # Output: False (No even numbers)

all_positive = all(map(lambda x: x > 0, numbers))
print(f"All Numbers Positive? {numbers} -> {all_positive}")  # Output: True (All numbers are positive)
