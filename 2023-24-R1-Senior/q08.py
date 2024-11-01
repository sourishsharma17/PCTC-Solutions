word = list(input())

for i in range(3):
  instruction = input()
  a, b = instruction.split(",")
  a = int(a) - 1
  b = int(b) - 1

  word[a], word[b] = word[b], word[a]

print("".join(word))
