list = [0, 1, 0, 12, 3]
zeros = [x for x in list if x != 0]
zeros_count = list.count(0)
my_zeros = [0] * zeros_count
result = zeros + my_zeros
print(result)
