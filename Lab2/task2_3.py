def solve():
    input_list = [5, -5, 3, 7, -7, 10]
    print(input_list)
    x = int(input('Enter value of "x"'))
    n = int(input('Enter value of "n"'))
    result = input_list[:n] + [x] + input_list[n:]
    print(result)


solve()
