def common_elements():
    list_3 = [x for x in range(100) if x % 3 == 0]
    list_5 = [x for x in range(100) if x % 5 == 0]

    set_3 = set(list_3)
    set_5 = set(list_5)

    result_set = set_3 & set_5

    return result_set
