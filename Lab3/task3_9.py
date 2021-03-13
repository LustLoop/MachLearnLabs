# var5

def remove_repeats():
    result_list = []
    repeated_chars_list = []

    input_line = input('Enter line')
    list_of_chars = list(input_line)
    previous_char = ''
    for char in list_of_chars:
        if char == previous_char:
            if not (char in repeated_chars_list):
                repeated_chars_list.append(char)
        else:
            result_list.append(char)
        previous_char = char

    print(convert_to_string(result_list))
    print(convert_to_string(repeated_chars_list))


def convert_to_string(input_list):
    result = ''
    return result.join(input_list)


remove_repeats()
