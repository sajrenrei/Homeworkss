# Функції


def calculate(a, b, c):
    d = ((a + b) * 2) / (c - 50)
    if d > 10:
        d += 10
    elif d < 10:
        d += 100
    return d, 100, "Hello"


...


def my_func():
    print("Hello world")


... #якийсь код
a = 34
b = 12
c = 56
d, m, n = calculate(a, b, c)
my_func()
print(d)
print(m)
print(n)
... #якийсь код
result = calculate(23, 12, c)
my_func()
... #якийсь код
z = 10
f = 45
r = 55
w = calculate(z, f, r)
my_func()
my_rez = [d, result, w]
... #якийсь код
print(my_rez)

