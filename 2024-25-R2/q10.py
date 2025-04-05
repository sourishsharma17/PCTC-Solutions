from math import gcd
from collections import defaultdict

stars = [tuple(map(int, input().split(","))) for i in range(int(input()))]

combs = defaultdict(int)

for anchor in stars:
  for other_star in stars:
    if anchor == other_star:
      continue

    x_slope = other_star[0] - anchor[0]
    y_slope = other_star[1] - anchor[1]

    divisor = gcd(x_slope, y_slope)

    x_slope //= divisor
    y_slope //= divisor

    combs[(anchor, x_slope, y_slope)] += 1

print(max(combs.values())+1)
    
