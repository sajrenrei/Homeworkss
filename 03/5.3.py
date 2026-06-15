import string

user_input = input("Введіть рядок для хештегу (макс. 140 символів): ")

while len(user_input) > 140:
    print(f"Помилка! Ваш рядок занадто довгий ({len(user_input)} симв.). Дозволено максимум 140.")
    user_input = input("Будь ласка, введіть коротший рядок: ")

processed_text = user_input.title()

hashtag = "#"

for char in processed_text:
    if char != " " and char not in string.punctuation:
        hashtag += char

hashtag = hashtag[:140]

print(hashtag)
