word = input()

words = []

words.append(word)
words.append(word[::-1])

words.sort()

print(words[0])
print(words[1])
