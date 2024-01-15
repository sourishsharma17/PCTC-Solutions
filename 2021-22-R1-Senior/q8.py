time = int(input())
prev = int(input())

a = 0
d = 0

for i in range(time):
  new = int(input())

  if new > prev:
    a += (new - prev)
  else:
    d += (prev - new)

  prev = new

print(a)
print(d)
