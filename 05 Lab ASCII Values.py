characters = input().split(', ')
represented_chr = {}
# for letter in characters:
#     value = ord(letter)
#     represented_chr[letter] = value
# print(represented_chr)


represented_chr = {letter: ord(letter) for letter in characters}
print(represented_chr)