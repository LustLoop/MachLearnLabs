import random


def solve():
    random_list = []

    n = int(input('Enter value of "n"'))
    a = int(input('Enter value of "a"'))
    b = int(input('Enter value of "b"'))

    for i in range(0, n):
        x = random.randint(a, b)
        random_list.append(x)

    return random_list

