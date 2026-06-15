my_list = [1, 2, 3, 4, 90, 74, 5, 6, 99, 102, -102, 1000]

number = None
index_number = None
for index_2, item in enumerate(my_list):
    if number is None or item > number:
        number = item
        index_number = index_2

print("Maximum number is:", number, "and its index is :", index_number)



my_list = [1, 2, 3, 4, 90, 74, 5, 6, 99, 102, -102, 1000]
number = None
index_number = None
for value in enumerate(my_list):
    print(value)

    print(value[0])
    print(value[1])


