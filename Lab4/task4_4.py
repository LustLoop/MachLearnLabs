import numpy as np


def solve():
    first_array = input('Enter first array')
    first_array_of_ints = convert_to_list_of_ints(first_array)
    matrix = np.asarray(first_array_of_ints)
    threshold = int(input('Enter threshold'))
    more_than_threshold = matrix[matrix > threshold]
    print('{} - values more than threshold'.format(more_than_threshold))
    less_than_threshold = matrix[matrix < threshold]
    print('{} - values less than threshold'.format(less_than_threshold))


def convert_to_list_of_ints(string_list):
    result = []
    for string in string_list.split(' '):
        result.append(int(string))
    return result


solve()
