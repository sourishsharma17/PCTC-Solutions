a = int(input())
b = int(input())
c = int(input())

total = 0

total += a//2
a -= a//2

b += a
b -= b//2

c += b
c -= c//2

total += c

print(total)
