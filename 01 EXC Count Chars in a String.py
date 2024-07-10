phrase = input()
occurrences_dct = {}
for letter in phrase:
    if letter != ' ':
        key = letter
        if key not in occurrences_dct:
            occurrences_dct[key] = 1
        else:
            occurrences_dct[key] += 1
[print(f'{word} -> {occurrences}') for (word, occurrences) in occurrences_dct.items()]
