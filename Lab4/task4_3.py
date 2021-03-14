import numpy as np


def solve():
    first_array = input('Enter first array')
    indexes_array = input('Enter second array')
    first_array_of_ints = convert_to_list_of_ints(first_array)
    indexes_array_of_ints = convert_to_list_of_ints(indexes_array)
    matrix = np.asarray(first_array_of_ints)
    print(matrix)
    result = matrix[indexes_array_of_ints]
    print(result)


def convert_to_list_of_ints(string_list):
    result = []
    for string in string_list.split(' '):
        result.append(int(string))
    return result


solve()
