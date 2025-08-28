def word_count(text):
    words = text.split()
    return len(words)

def char_counts(text):
    text = text.lower()
    chars = list(text)
    counts = {}
    for char in chars:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_counts(counts):
    sort_on = lambda item: item["num"]

    sorted_counts = []
    for char, count in counts.items():
        sorted_counts.append({"char":char, "num":count})

    sorted_counts.sort(reverse=True, key=sort_on)
    return sorted_counts
