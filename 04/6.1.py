import string

user_input = input("Введіть літери: ").strip()
start_char, end_char = user_input.split("-")
letters = string.ascii_letters
start_index = letters.index(start_char)
end_index = letters.index(end_char)
result = letters[start_index : end_index + 1]
print(result)
