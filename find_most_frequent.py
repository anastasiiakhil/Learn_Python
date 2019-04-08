def find_most_frequent(text):
    symbols = [',', '.', ':', ';', '!', '?', '-']
    text = text.lower()
    for symbol in symbols:
        text = text.replace(symbol, ' ')
    clean_text = text.split()
    count_words = []
    result = []
    for i in clean_text:
        count_words.append(clean_text.count(i))
    for k in range(len(count_words)):
        if count_words[k] == max(count_words):
            result.append(clean_text[k])
    return sorted(list(set(result)))
