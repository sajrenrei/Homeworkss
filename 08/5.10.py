def my_gen(start, end):
    current = start
    while current < end:
        yield current
        current += round((current / 2) + 0.001) + 2

gen = my_gen(1, 1000)

print(next(gen))
print(next(gen))
print(next(gen))
print('-------------')


for i in gen:
    print(i)
