import math
import numpy


def solve():
    while True:
        print('Enter value')
        input_string = input()
        if input_string == 'q':
            break
        input_value = float(input_string)
        x = math.radians(input_value)
        if check_is_valid(x):
            if input_value < 1:
                print(calc_first_option(x))
            elif input_value > 10:
                print(calc_second_option(x))
            else:
                print('Try again with appropriate value')


def calc_first_option(x):
    return math.log(math.sin(x) + 0.5)


def calc_second_option(x):
    return find_cotangent(math.pow(x, 2)) / math.sqrt(1 - numpy.arcsin(x // 360))


def find_cotangent(x):
    return math.cos(x) / math.sin(x)


def check_is_valid(x):
    if 1 - numpy.arcsin(x) < 0:
        print('Square root value is less than zero')
        return False
    if 1 - numpy.arcsin(x) == 0:
        print('Denominator is zero')
        return False
    return True
