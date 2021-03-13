groups_dictionary = {
    "A-17": [12, 'Liam'],
    "B-13": [7, 'Noah'],
    "C-7": [9, 'Oliver'],
    "D-22": [22, 'William'],
    "E-67": [4, 'Elijah']
}


def get_name_of_group():
    return input('Enter group name')


def get_number_of_students_in_group():
    group_data = groups_dictionary.get(get_name_of_group())
    students = group_data[0]
    print(students)


def get_headman_of_group():
    group_data = groups_dictionary.get(get_name_of_group())
    headman = group_data[1]
    print(headman)


def get_all_groups_within_threshold():
    threshold = int(input('Enter threshold'))
    result = []
    for key, value in groups_dictionary.items():
        if value[0] < threshold:
            result.append(key)
    print(tuple(result))


def get_all_groups_greater_than_threshold():
    threshold = int(input('Enter threshold'))
    result = []
    for key, value in groups_dictionary.items():
        if value[0] > threshold:
            result.append(key)
    print(tuple(result))


def change_students_number_in_group():
    new_number = int(input('Enter new number of students'))
    group_data = groups_dictionary.get(get_name_of_group())
    group_data[0] = new_number
    print(group_data)


def change_headman_in_group():
    new_headman = input('Enter new headman')
    group_data = groups_dictionary.get(get_name_of_group())
    group_data[1] = new_headman
    print(group_data)


def add_new_group():
    new_group_students_number = int(input('Enter number of students'))
    new_headman = input('Enter headman')
    groups_dictionary[get_name_of_group()] = [new_group_students_number, new_headman]
    print(groups_dictionary)


def remove_group():
    groups_dictionary.pop(get_name_of_group())
    print(groups_dictionary)


def get_array_of_headmen():
    result = []
    while True:
        name_of_group = get_name_of_group()
        if not name_of_group:
            break
        group_data = groups_dictionary.get(name_of_group)
        headman = group_data[1]
        result.append(headman)
    print(result)


menu = """

Change your option:
    1 - Get number of students in group
    2 - Get headman of group
    3 - Get groups within threshold
    4 - Get groups greater than threshold
    5 - Change students number in group
    6 - Change headman in group
    7 - Add new group
    8 - Remove group
    9 - Get array of headman
    0 - Exit

"""


actions = {
    1: get_number_of_students_in_group,
    2: get_headman_of_group,
    3: get_all_groups_within_threshold,
    4: get_all_groups_greater_than_threshold,
    5: change_headman_in_group,
    6: change_headman_in_group,
    7: add_new_group,
    8: remove_group,
    9: get_array_of_headmen
}


while True:
    print(menu)
    active_option = int(input())
    if active_option == 0:
        print('Bye')
        break
    option = actions.get(active_option)
    option()
