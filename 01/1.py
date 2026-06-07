num1 = float(input("Введіть перше число: "))
operation = input("Введіть дію (+, -, *, /): ")
num2 = float(input("Введіть друге число: "))

if operation == '+':
    print(num1 + num2)

elif operation == '-':
    print(num1 - num2)

elif operation == '*':
    print(num1 * num2)

elif operation == '/':
    if num2 == 0:
        print("Помилка! Ділити на нуль не можна!")
    else:
        print(num1 / num2)
else:
    print("Невідома операція! Будь ласка, використовуйте тільки +, -, * або /.")