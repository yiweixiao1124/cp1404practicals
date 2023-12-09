"""
Word Occurrences
Estimate: 20 minutes
Actual:  21  minutes
"""

text = input("Text: ")
words = text.split()
word_to_counts = {}
for word in words:
    word_to_counts[word] = word_to_counts.get(word, 0) + 1

length = max(len(word) for word in word_to_counts.keys())

for word, count in sorted(word_to_counts.items()):
    print(f"{word:<{length}} : {count}")
