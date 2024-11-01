n = int(input())
p = int(input())
letter = input()

n /= p

if letter == "d":
  n /= 2

if n % 1 == 0:
  print(int(n))
else:
  print(int(n)+1)
