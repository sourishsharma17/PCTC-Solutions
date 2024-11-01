word = input()

word = list(word)

centreR = len(word)//2
centreL = centreR - 1

for i in range(len(word)//2):
    letter = word.pop(centreL)
    word.insert(0, letter)

    letter = word.pop(centreR)
    word.append(letter)

    print("".join(word))
