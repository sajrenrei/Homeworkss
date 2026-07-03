def dn(x):
    return x > 0

my_list = [1, 2, 3, 4, 5, -10, 33, 0, -5, -12]
print(list(filter(dn, my_list)))

print(list(filter(lambda x: x > 0, my_list)))


print(("-") * 20)


def fn(x):
    return x + 2

new_list = [1, 2, 3, 4, 5, -10, 33, 0, -5, -12]

print(list(filter(fn, new_list)))
print(list(filter(lambda x: x + 2, new_list)))

