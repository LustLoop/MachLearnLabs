coordinates = [0, 0]
while True:
    input_string = input()
    if input_string == 'Treasure!':
        break
    step = input_string.split()
    if step[0] == 'North' or step[0] == 'South':
        coordinates[1] += int(step[1])
    if step[0] == 'East' or step[0] == 'West':
        coordinates[0] += int(step[1])
print('{} {}'.format(coordinates[0], coordinates[1]))
