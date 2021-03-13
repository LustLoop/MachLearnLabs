input_string = input('Enter string')
input_substring = input('Enter input_substring')
result = 0
sub_len = len(input_substring)
for i in range(len(input_string)):
    if input_string[i:i + sub_len] == input_substring:
        result += 1
print(result)
