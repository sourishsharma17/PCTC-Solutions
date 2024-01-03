horse0 = 0
horse1 = 0

while 1:
  num = int(input())

  if num:
    horse1 += 1
  else:
    horse0 += 1

  if horse1 == 11 or horse0 == 11:
    break

top = list("|..........|")
top[horse0] = "H"
bottom = list("|..........|")
bottom[horse1] = "H"

print("".join(top))
print("".join(bottom))
