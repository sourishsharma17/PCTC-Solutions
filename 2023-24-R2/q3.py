from string import ascii_lowercase 

sentence = input()

for letter in ascii_lowercase:
  if letter not in sentence:
    print(letter, end="")



