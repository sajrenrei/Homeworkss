my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = []
for item in my_list:
    new_list.append(item * 3)

print(new_list)

new_list_2 = [item * 3 for item in my_list] #генератор списку
print(new_list_2)


new_list_4 = []
for item in my_list:
    if item > 0:
        new_list_4.append(item * 3)
print(new_list_4)


new_list_3 = [item * 3 for item in my_list if item > 0]
print(new_list_3)