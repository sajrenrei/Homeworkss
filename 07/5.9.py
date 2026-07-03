def my_finc(a, b):
    if a > b:
        return a * b
    else:
        return b * a

print(my_finc(4, 5))

new_func = lambda a, b: (a * b) if a > b else (b * a)
print(new_func(4, 5))


def my_func_2():
    return "Hello"

new_func_2 = lambda: "Hello"

print(my_func_2())
print(new_func_2())
