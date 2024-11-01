from string import ascii_uppercase as au

message = input()
message = message.replace(" ", "")

pi = "31415926535897932384626433832795028841971693993751"

ans = ""

for i in range(len(message)):
  if i%2 == 0:
    ans += au[(au.index(message[i]) + int(pi[i]))%26]
  else:
    ans += au[(au.index(message[i]) - int(pi[i]))%26]

print(ans)
    



