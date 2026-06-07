list = [1, 2, 3, 4, 5]
if len(list) > 1:
    last_element = list.pop()
    list.insert(0, last_element)
    print(list)
