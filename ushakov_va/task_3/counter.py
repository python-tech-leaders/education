def count_char(text):
    text = text.replace(' ', '').replace('\n', '')

    result = {}
    for c in text:
        if c not in result:
            result[c] = 1
        else:
            result[c] += 1

    return result
