my_list = [1, 2, 3, 4, 90, 74, 5, 6, 99, 102, -102, 1000]

number = None
index_number = None
index_1 = 0
for item in my_list:
    if number is None or item > number:
        number = item
        index_number = index_1
    index_1 += 1

print("Maximum number is:", number, "and its index is :", index_number)




