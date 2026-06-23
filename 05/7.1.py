# name = (input("Введи своє ім'я:"))
# age = int(input("Введи свій вік:"))
#
#
# def say_hi_ua(name, age):
#     if age % 10 == 1 and age % 100 != 11:
#         years_word = "рік"
#     elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
#         years_word = "роки"
#     else:
#         years_word = "років"
#
#     return f"Привіт, мене звати {name}, мені {age} {years_word}."
# print(say_hi_ua(name, age))


# print(("-") * 20)


def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"

assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('OK')


