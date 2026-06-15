user_choice = "yes"

while user_choice == "yes" or user_choice == "y":
    print("\n--- Нове обчислення ---")

    num1 = float(input("Введіть перше число: "))
    operator = input("Введіть операцію (+, -, *, /): ")
    num2 = float(input("Введіть друге число: "))

    if operator == "+":
        result = num1 + num2
        print(f"Результат: {num1} + {num2} = {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"Результат: {num1} - {num2} = {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"Результат: {num1} * {num2} = {result}")
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"Результат: {num1} / {num2} = {result}")
        else:
            print("Помилка: ділення на нуль!")
    else:
        print("Невідома операція!")

    user_choice = input("\nБажаєте продовжити роботу? (yes/y або no): ").lower()

print("\nДякуємо, що користувалися калькулятором! Роботу завершено.")