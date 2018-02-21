import string
import grammar_check

file = open("exampleText.txt", "r")

text = file.read()
file.close()

for char in '/-.,!?\n':
    text=text.replace(char, ' ')

text=text.lower()
wordList = text.split()
dictionary = {}

for w in wordList:
    dictionary[w] = dictionary.get(w, 0) + 1

frequency = []
for key, value in dictionary.items():
    frequency.append((value, key))

frequency.sort(reverse=True)

# frequency = []
# for w in wordList:
#     frequency.append(wordList.count(w))

# print(str(zip(wordList, frequency)))

print('Word frequency:')
for v in frequency:
    print(str(v).strip('[]'))