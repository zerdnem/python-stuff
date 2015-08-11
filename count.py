from collections import Counter

def count_letters(words):
    counter = Counter()
    for word in words.split():
        counter.update(word)
    return sum(counter.itervalues())

words = "The grey old fox is an idiot"
print count_letters(words)  # 22