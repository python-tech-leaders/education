import collections

def count_char(texts):
    #text = text.replace(' ', '').replace('\n', '')

    all_texts = ''.join(texts)
    return collections.Counter(all_texts)
