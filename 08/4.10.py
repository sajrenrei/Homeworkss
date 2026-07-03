def my_current(start, end):
    current = start
    while current < end:
        yield current
        current += round((current / 2) + 0.001) + 2

gen = my_current(1, 100)
for i in gen:
    print(i)