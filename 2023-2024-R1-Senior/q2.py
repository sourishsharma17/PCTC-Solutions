fish = int(input())
chips = int(input())

total = fish*5 + chips*2

if total > 20:
  ans = input()
  if ans == "y":
    total += 1
    
print(total)


