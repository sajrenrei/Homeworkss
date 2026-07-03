# def my_func(a, b, data)
def func(a: (int, float, str), b: int, data: list) -> int:
    a = int(a)
    b += 1
    new_data = []
    for item in data:
        new_data.append(item * 2 + a - b)
    return new_data

numbers = [1, 2, 3, 4, 5]
print(func(3, 5, numbers))
print(func.__annotations__)
