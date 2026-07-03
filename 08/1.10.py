# def dn(x):
#     if x <= 0:
#         return x + 10
#     else:
#         return x * 2



def dn(x):
    if x < 0:
        return x + 10
    elif x == 0:
        return x + 100

my_list = [1, 2, 3, 4, 5, -10, 33, 0, -5, -12]

print(list(map(dn, my_list)))        # dn буде повертати None бо функція нічого їй не повертає

print(list(map(lambda x: x + 10 if x <= 0 else x * 2, my_list)))

dn_new = lambda x: x + 10 if x <= 0 else x * 2
print(list(map(dn_new, my_list)))


print(list(map(lambda x: x > 0, my_list)))