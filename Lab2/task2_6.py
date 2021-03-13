def solve():
    n = int(input('Input n'))
    array_of_possible_values = list(range(1, n+1))
    while True:
        new_array_of_possible_values = array_of_possible_values.copy()
        user_input = input('Input numbers')

        if user_input == 'End':
            break

        strings_array = user_input.split(' ')
        nums_array = []
        for value in strings_array:
            nums_array.append(int(value))

        if len(find_repeating_values(nums_array, array_of_possible_values)) <= len(array_of_possible_values) / 2:
            print('No')
            for number in nums_array:
                if number in array_of_possible_values:
                    new_array_of_possible_values.remove(number)
        else:
            print('Yes')
            for number in array_of_possible_values:
                if not (number in nums_array):
                    new_array_of_possible_values.remove(number)

        array_of_possible_values = new_array_of_possible_values.copy()

    print(array_of_possible_values)


def find_repeating_values(target_arr, comparable_arr):
    result = target_arr.copy()
    for number in target_arr:
        if not (number in comparable_arr):
            result.remove(number)
    return result


solve()
