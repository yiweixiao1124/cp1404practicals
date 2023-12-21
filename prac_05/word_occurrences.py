"""
Word Occurrences
Estimate: 20 minutes
Actual:  21  minutes
"""
from operator import itemgetter
word_to_counts = {}
word_count = 0
word_length = 0

texts = input("Text: ").split()
text = sorted(texts)

for word in text:
    word_count = text.count(word)
    word_to_counts[word] = word_count

print(word_to_counts)
word_to_counts = sorted(word_to_counts.items(), key=itemgetter(0, 1))
word_to_counts = dict(word_to_counts)

for word in word_to_counts:
    if len(word) > word_length:
        word_length = len(word)

for word, count in word_to_counts.items():
    print(f"{word:<{word_length}} : {count}")
