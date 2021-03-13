import re


input_string = input('Enter word')
if re.match("^[A-Za-z0-9_]*$", input_string):
    print('Is identifier')
else:
    print('Is not identifier')
