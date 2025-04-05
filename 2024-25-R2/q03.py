num = int(input())
n = int(input())

for i in range(n-1):
  num *= 5
  num = int(str(num).rstrip("0"))

print(num)
