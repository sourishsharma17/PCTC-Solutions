length = int(input())
coins = list(input())

turns = 0

for i in range(length-1):
  if coins[i] == "T":
    coins[i] = "H"
    coins[i+1] = "H" if coins[i+1] == "T" else "T"
    turns += 1

print(turns)



