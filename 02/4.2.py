my_list = [0, 1, 7, 2, 4, 8]
if not my_list:
    result = 0
else:
    even_indexed_sum = sum(my_list[::2])
    last_element = my_list[-1]
    result = even_indexed_sum * last_element
    print(result)
