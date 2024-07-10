count_of_words = int(input())
synonyms_dct = {}
for i in range(count_of_words):
    word = input()
    synonym = input()
    if word not in synonyms_dct:
        synonyms_dct[word] = []
        synonyms_dct[word].append(synonym)
    else:
        synonyms_dct[word].append(synonym)
for (key, value) in synonyms_dct.items():
    print(f'{key} - {", ".join(value)}')
