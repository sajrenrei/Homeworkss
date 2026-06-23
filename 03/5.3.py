import string

user_input = input("Введіть рядок для хештегу: ")

cleaned_text = ""
for char in user_input:
    if char not in string.punctuation:
        cleaned_text += char
    else:
        cleaned_text += " "

words = cleaned_text.split()
hashtag = "#" + "".join(word.capitalize() for word in words)
hashtag = hashtag[:140]
print(hashtag)