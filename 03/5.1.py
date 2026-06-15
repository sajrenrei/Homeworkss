import keyword
import string

user_input = input("Введіть ім'я змінної для перевірки: ")

is_valid = True
if user_input[0].isdigit():
    is_valid = False
elif any(char.isupper() for char in user_input):
    is_valid = False
else:
    forbidden_chars = string.punctuation + " "
    forbidden_chars = forbidden_chars.replace("_", "")
    for char in user_input:
        if char in forbidden_chars:
            is_valid = False
            break
if "__" in user_input:
    is_valid = False
if user_input in keyword.kwlist:
    is_valid = False
print(is_valid)
