import math


def calc_by_while_cycle(x, n):
    sum_of_elements = 0
    i = 1
    while i < n:
        sum_of_elements = math.sqrt((calc_sum_of_arithmetical_progression(n - i) + x) + sum_of_elements)
        i += 1
    return sum_of_elements


def calc_by_for_cycle(x, n):
    sum_of_elements = 0
    for i in range(1, n):
        sum_of_elements = math.sqrt((calc_sum_of_arithmetical_progression(n - i) + x) + sum_of_elements)
    return sum_of_elements


def calc_by_recursion(x, n, i):
    if i <= n:
        return math.sqrt(calc_sum_of_arithmetical_progression(i) + x + calc_by_recursion(x, n, i + 1))
    else:
        return 0


def calc_sum_of_arithmetical_progression(x):
    if x == 1:
        return 1
    else:
        return x + calc_sum_of_arithmetical_progression(x - 1)


def solve_by_recursion():
    input_x_value = float(input('Enter x value'))
    input_n_value = int(input('Enter n value'))

    result_by_recursion = calc_by_recursion(input_x_value, input_n_value, 1)
    print(result_by_recursion)


def solve_by_for_cycle():
    input_x_value = float(input('Enter x value'))
    input_n_value = int(input('Enter n value'))

    result_by_for_cycle = calc_by_for_cycle(input_x_value, input_n_value + 1)
    print(result_by_for_cycle)


def solve_by_while_cycle():
    input_x_value = float(input('Enter x value'))
    input_n_value = int(input('Enter n value'))

    result_by_while_cycle = calc_by_while_cycle(input_x_value, input_n_value + 1)
    print(result_by_while_cycle)
