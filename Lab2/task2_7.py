# 5 var

list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 7, 8]

list_of_same = []
list_of_different = []

for element in list1:
    if element in list2:
        list_of_same.append(element)
    else:
        list_of_different.append(element)

for element in list2:
    if not(element in list1) and not(element in list_of_different):
        list_of_different.append(element)

print(list_of_same)
print(list_of_different)
