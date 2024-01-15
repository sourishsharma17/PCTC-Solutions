hat = int(input())
scarf = int(input())
glove = int(input())

total = 0

if hat > 0:
  hat -= 1
  total += 1

if scarf > 0:
  scarf -= 1
  total += 1

if glove >= 2:
  glove -= 2
  total += 1
elif glove > 0:
  glove -= 1

if total >= 2:
  print("toasty")
else:
  print("cold")

print(hat + scarf + glove)
