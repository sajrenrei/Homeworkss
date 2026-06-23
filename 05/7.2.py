

def correct_sentence(text:str) -> str:
    text = text.capitalize()
    if not text.endswith("."):
        text += "."
    return text



assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
print("OK")
