def find_inside(text: str):
    start_index = text.find("(")
    if start_index == -1:
        return None

    end_index = text.find(")", start_index + 1)

    if end_index == -1:
        return None

    if end_index - start_index <= 2 and text[start_index + 1 : end_index].strip() == "":
        return None

    return start_index + 1
