from Lab2.task2_1 import solve as generate_list


def solve_without_generation():
    input_list = [5, -5, 3, 7, -7, 10]
    result = []
    for x in input_list:
        if x < 0:
            result.append(x)
    print(result)


def solve_with_generation():
    generated_list = generate_list()
    print(generated_list)
    result = []

    for x in generated_list:
        if x < 0:
            result.append(x)
    print(result)


solve_with_generation()

