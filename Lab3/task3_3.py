def solve():
    input_string = input('Enter string')
    words = input_string.split()
    result = remove_repeats(words)
    print(result)


def remove_repeats(input_list):
    result = []
    for word in input_list:
        if word not in result:
            result.append(word)
    return result


solve()
