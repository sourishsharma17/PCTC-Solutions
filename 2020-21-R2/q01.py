from math import ceil

num = int(input())
total = int(input())

res = ceil(total / num)
left = (res*num) - total

print(left)
