
import json
import pickle

# it can be done also with pickle
def save_dictionary(dict, path):
    with open(path, 'w') as file:
        json.dump(dict, file, indent=4)

def read_dictionary(path):
    with open(path, 'r') as file:
        result = file.read()
    return result

d1 = {
    'auto': 'bmw',
    'driver': 'Tobiasz',
    'name': 'Alice',
    'age': 30,
    'city': 'Wonderland',
    'hobbies': ['reading', 'hiking', 'painting']}



path = r'C:\python_tmp\dictionary_json_dump.txt'

save_dictionary(d1, path)
print(read_dictionary(path))

d2 = {1 : "a", 2: "b", 3: "c"}

def save_pickle(dict, path):
    with open(path, 'wb') as file:
        pickle.dump(dict, path)

def read_pickle(path):
    with open(path, 'rb') as file:
        return pickle.load(dict, path)


path = r'C:\python_tmp\dictionary_pickle.pickle'

save_dictionary(d2,path)
print(read_dictionary(path))