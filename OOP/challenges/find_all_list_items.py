


def traverse_list(nested_list, target):
    result = []
    for element in nested_list:
        if isinstance(element, list):
            result.append(traverse_list(element, target))  # Recursively call the function if the element is a list
        else:
            #print(element)
            if element == 2:
                result.append(1)
            else:
                result.append(0)
    return result

# test

l1 = [[[1,2,44], [4,2], [33,4]], [2,6,7,99,2]]
#traverse_list(l1,2)
print(traverse_list(l1,2))
print([[[0,1,0], [0,1], [0,0]], [1,0,0,0,1]] == traverse_list(l1,2))


# solves original issue
def search_for_value(nested_list, target, current_path=[]):
    indices = []
    for i, element in enumerate(nested_list):
        new_path = current_path + [i]  # Update the current path with the current index
        if isinstance(element, list):
            # Recursively search in the nested list
            indices.extend(search_for_value(element, target, new_path))
        else:
            # If element matches the target, append the path to indices
            if element == target:
                indices.append(new_path)
    return indices

# Call the function to search for '2'
indices_of_2 = search_for_value(l1, 2)
print(indices_of_2)

l2 = [[[1,2,3], 2, [1,3]], [1,2,3]]
print(search_for_value(l2,2))
# final test
print([[0, 0, 1], [0, 1], [1, 1]] == search_for_value(l2,2) )