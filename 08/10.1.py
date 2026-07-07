def sequence_generator(first_term, n, rule_func):
    """
    Генераторна функція для створення числової послідовності.

    :param first_term: Перший член прогресії/послідовності.
    :param n: Кількість членів, яку треба згенерувати.
    :param rule_func: Функція користувача, яка приймає поточний член і повертає наступний.
    """
    current = first_term
    count = 0

    while count < n:
        yield current
        current = rule_func(current)
        count += 1


def arithmetic_rule(x):
    return x + 3


def geometric_rule(x):
    return x * 2


print("Арифметична прогресія:")
for num in sequence_generator(first_term=5, n=6, rule_func=arithmetic_rule):
    print(num, end=" ")
print("\n")

print("Геометрична прогресія:")
for num in sequence_generator(first_term=2, n=5, rule_func=geometric_rule):
    print(num, end=" ")
print()