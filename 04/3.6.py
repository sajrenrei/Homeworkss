my_list = [1, 2, 3, "God", True, 748, "Hello", '0', 0, 99, 99, 1]

my_set = {1, 2, 3, 4, 'World', '0', 77, 99, 5, 6, 7, 8, 9, "df"}
print(my_set)
print(id(my_set))
my_set_2 = set((1, 2, 3, 4, 5, 6, 7, 8, 9, "df"))
print(my_set_2)
print(id(my_set_2))

new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)
print(new_list)

new_list_2 = list(set(my_list))
print(new_list_2)

my_set_3 = {3, 4, 'World', '0', 77, 99, 5, 101, 102, 103}

new_set = my_set.union(my_set_3)
print(new_set)

new_set_2 = my_set.intersection(my_set_3)
print(new_set_2)

new_set_3 = my_set.difference(my_set_3)
print(new_set_3)

my_set_4 = frozenset((1, 2, 3, 4, 5, 6, 7, 8, 9, "df"))