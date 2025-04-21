def count_words(text):
    words = text.split()
    count = len(words)
    return count

def count_chars(text):
    clean_text = text.lower()
    counts = {}
    for char in clean_text:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts

def sort_chars(text):
    char_counts = count_chars(text)
    result = []
    for char, count in sorted(char_counts.items(), key=lambda item: item[1], reverse=True):
        result.append({'char': char, 'count': count})
    return result
