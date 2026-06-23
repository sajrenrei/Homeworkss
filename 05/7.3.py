def second_index(text: str, symbol: str):
    first_index = text.find(symbol)
    if first_index == -1:
        return None
    sec_index = text.find(symbol, first_index + 1)

    if sec_index == -1:
        return None
    else:
        return sec_index

