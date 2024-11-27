from icecream import ic

x = [[j for j in range(5)] for i in range(10)]

# icecream is very good for debugging, it prints not only values, but variables names, and exact structure of data
# icecream increase readablity, less boilerplate code, less debugging needs
# you can easily turn it off, with below disable() call
# but still, logging is far more helpful
#ic.disable()

ic(x)
print(x)
# alternative, similar result to icecream
print(f"{x=}")

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Double each value in the dictionary
squared_dict1 = {k: v * v for (k, v) in dict1.items()}
ic(squared_dict1)
print(squared_dict1)

numbers = range(10)
new_dict_for = {}

# Add values to `new_dict` using for loop
for n in numbers:
    if n % 2 == 0:
        new_dict_for[n] = n ** 2

ic(new_dict_for)
ic(new_dict_for.items(), new_dict_for.keys(), new_dict_for.values())


another_dict = {x: x * 3 for x in range(7)}
ic(another_dict, another_dict.items())

# to print some function documentation
help(print)
