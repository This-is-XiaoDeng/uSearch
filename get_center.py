def get(text, start, end, find_start = 0):
    text_start = text.find(start, find_start) + start.__len__()
    text_end = text.find(end, text_start)
    return text[text_start:text_end]
