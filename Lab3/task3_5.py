input_string = 'asdfab00000bb35'
characters = ['a', 'b', 'c', '3', '5']
most_frequent = ['', 0]

for char in characters:
    frequency = 0
    for input_char in input_string:
        if input_char == char:
            frequency = frequency + 1
    if frequency > most_frequent[1]:
        most_frequent = [char, frequency]

print(most_frequent[0])


