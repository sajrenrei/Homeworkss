def correct_sentence(text:str) -> str:
    if text:
        text = text[0].upper() + text[1:]
    if not text.endswith("."):
        text += "."

    return text


assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, Friends") == "Greetings, Friends."
print("OK")