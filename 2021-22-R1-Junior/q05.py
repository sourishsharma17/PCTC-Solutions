temp = input()
dist = int(input())

total = dist * 2

if temp == "warm":
  if total <= 10:
    total += dist

print(total)
