from Lab2.task2_1 import solve as generate_list


def solve_without_generation():
    input_list = [1, 2, 2, 2, 3, 4]
    print(input_list)
    n = int(input('Enter value of "n"'))
    while n in input_list:
        input_list.remove(n)
    print(input_list)


def solve_with_generation():
    generated_list = generate_list()
    print(generated_list)
    n = int(input('Enter value of "n"'))
    while n in generated_list:
        generated_list.remove(n)
    print(generated_list)


solve_with_generation()
