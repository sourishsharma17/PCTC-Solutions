### efficient solution (10/10) ###
from math import ceil

x, t, y = [int(input()) for i in range(3)]

r = x * t
diff = y-x

print(t + ceil(r/diff))


### inefficent solution (8/10) ###
r = 0
a = 0

time = 0
while 1:
  r += x
  if time >= t:
    a += y

  time += 1

  if a >= r:
    print(time)
    break
