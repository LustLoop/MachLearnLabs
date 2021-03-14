import numpy as np


def solve():
    m = int(input('Enter M'))
    n = int(input('Enter N'))

    new_matrix = np.empty([m, n])

    new_matrix.fill(0.5)
    np.fill_diagonal(new_matrix, -1)

    print(new_matrix)

    coordinate1 = convert_to_coordinates(input('Enter left-top corner'))
    coordinate2 = convert_to_coordinates(input('Enter right-bottom corner'))

    print(new_matrix[np.ix_(coordinate1, coordinate2)])


def convert_to_coordinates(string):
    result = []
    list_of_strings = string.split(' ')
    for string in list_of_strings:
        result.append(int(string))
    print(result)
    return result


solve()
