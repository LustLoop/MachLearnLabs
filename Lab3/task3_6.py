input_number = int(input('Enter n'))
print(input_number * ' ___   ')
print(input_number * '|   \  ')
line_with_number = ''
for number in range(input_number):
    line_with_number += '| {}  | '.format(number + 1)
print(line_with_number)
print(input_number * '|___/  ')
print(input_number * '|      ')
print(input_number * '|      ')
