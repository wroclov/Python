import functools

def calculate_sum(num_list):
    result = functools.reduce(lambda a, b: a+b, num_list)
    return result

lis = [1, 14, 22, -8]

print(calculate_sum(lis))

def square_it(num_list):
    result = map(lambda a: a**2, num_list)
    return result

print(square_it(lis))
for elem in square_it(lis):
    print(elem)

def filter_negative(num_list):
    result = list(filter(lambda a: (a >= 0), num_list))
    return result

print(filter_negative(lis))