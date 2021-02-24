import math


def calc_by_while_cycle(x, n):
    sum_of_elements = 0
    i = 1
    while i < n:
        sum_of_elements = math.sqrt((arithmetical_progression(n - i) + x) + sum_of_elements)
        i += 1
    return sum_of_elements


def calc_by_for_cycle(x, n):
    sum_of_elements = 0
    for i in range(1, n):
        sum_of_elements = math.sqrt((arithmetical_progression(n - i) + x) + sum_of_elements)
    return sum_of_elements


def calc_by_recursion(x, n, i):
    if i <= n:
        return math.sqrt(arithmetical_progression(i) + x + calc_by_recursion(x, n, i + 1))
    else:
        return 0


def arithmetical_progression(x):
    if x == 1:
        return 1
    else:
        return x + arithmetical_progression(x - 1)


if __name__ == '__main__':
    print('Enter x value')
    input_x_value = float(input())
    print('Enter n value')
    input_n_value = int(input())

    result_by_recursion = calc_by_recursion(input_x_value, input_n_value, 1)
    print(result_by_recursion)

    result_by_for_cycle = calc_by_for_cycle(input_x_value, input_n_value + 1)
    print(result_by_for_cycle)

    calc_by_while_cycle = calc_by_while_cycle(input_x_value, input_n_value + 1)
    print(calc_by_while_cycle)