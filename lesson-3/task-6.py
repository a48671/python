def int_func(string):
    return string[0].upper() + string[1: len(string)]

words = input('Input words: ').split()

for index, word in enumerate(words):
    words[index] = int_func(word)

string = ' '.join(words)

print(string)
