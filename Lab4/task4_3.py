import numpy as np


def solve():
    first_array_of_ints = input('Enter first array').split(' ')
    indexes_array = input('Enter second array')
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
