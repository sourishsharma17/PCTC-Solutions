words = []

for i in range(int(input())):
  word = input()

  if word == "hello":
    words.append("ahoy")
  elif word == "friend":
    words.append("matey")
  elif word == "my":
    words.append("me")
  elif word == "you":
    words.append("ye")
  elif word == "yes":
    words.append("aye")
  else:
    words.append(word)

print(*words)

