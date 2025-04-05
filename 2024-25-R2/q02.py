x, y = int(input()), int(input())

a, b = 0, 0

for i in range(4):
  temp = a*a - b*b + x
  b = 2*a*b + y
  a = temp

print(a*a + b*b)
