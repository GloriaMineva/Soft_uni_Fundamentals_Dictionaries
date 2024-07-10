words_sequence = [i.lower() for i in input().split(' ')]
word_count = {}
for word in words_sequence:
    key = word.lower()
    if word in word_count:
        word_count[key] += 1
    else:
        word_count[key] = 1

for (key, value) in word_count.items():
    if value % 2 != 0:
        print(key, end=' ')

