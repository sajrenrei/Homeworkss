import random

list = random.randint(3, 10)
print(list)
start_list = [random.randint(1, 100) for _ in range(list)]
print("Початковий список:", start_list)
final_list = [start_list[0], start_list[2], start_list[-2]]
print(final_list)
