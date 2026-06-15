a = int(input("Введіть число:"))
# a = 20
new_list = []
for i in range(a): # Введене вичсло буде роскладене на послідовність від 0 до числа
    new_list.append(i) # не включаючи його (a = 20) = 0, 1, 2, 3, ..., 19.

print(new_list)

a = 20
new_list = []
for i in range(1, a + 1): # Введене вичсло буде роскладене на послідовність від 0 до числа
    new_list.append(i) # не включаючи його (a = 20) = 0, 1, 2, 3, ..., 19.

b = 15
my_list = []
for i in range(5, b + 1, 3): # крок 3, кожен 3 елемент
    my_list.append(i)

print(new_list)
print(my_list)