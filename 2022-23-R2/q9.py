for i in range(int(input())):
  x,y,w,h = [int(r) for r in input().split()]

  if i == 0:
    ax, ay, bx, by = x, y, x+w, y+h
    continue

  ax = max(x, ax)
  ay = max(y, ay)
  bx = min(bx, x+w)
  by = min(by, y+h)

print((bx-ax) * (by-ay))



