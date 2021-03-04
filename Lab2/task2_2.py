from Lab2 import task2_1


def solve_without_generation():
    input_list = [5, -5, 3, 7, -7, 10]
    result = []
    for x in input_list:
        if x < 0:
            result.append(x)
    print(result)


def solve_with_generation():
    generated_list = task2_1.solve()
    result = []

    for x in generated_list:
        if x < 0:
            result.append(x)
    print(result)
