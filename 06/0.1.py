def add_one(some_list):
    full_number = int("".join([str(num) for num in some_list]))
    result_number = full_number + 1

    return [int(char) for char in str(result_number)]

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("OK")