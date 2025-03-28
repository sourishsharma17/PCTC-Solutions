a = 0
b = 0
ans = 0

while 1:
  point = input()

  if point == "A":
    if b == 4:
      b -= 1
    else:
      a += 1
  else:
    if a == 4:
      a -= 1
    else:
      b += 1

  if (a,b) == (3,3):
    ans += 1

  if (2,4) in ((a,b), (b,a)) or 5 in (a,b):
    break

print(ans)
