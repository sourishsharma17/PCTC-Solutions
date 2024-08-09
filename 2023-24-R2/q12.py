from heapq import *

side = int(input())

grid = []
for i in range(side):
  grid.append(input())


# walls broken, steps taken, x, y
states = [(0, 0, 0, 0)]
visited = set()

while states:
  walls, steps, x, y = heappop(states)

  if (x,y) in visited:
    continue

  visited.add((x, y))

  if (x, y) == (side-1, side-1):
    print(steps)
    break

  for xchange, ychange in ((0,1), (1,0), (-1,0), (0,-1)):
    newx = x + xchange
    newy = y + ychange

    if side > newx >= 0 and side > newy >= 0:
      if grid[newy][newx] == "0":
        heappush(states, (walls, steps+1, newx, newy))
      else:
        newx += xchange
        newy += ychange
        
        if side > newx >= 0 and side > newy >= 0:
          if grid[newy][newx] == "0":
            heappush(states, (walls+1, steps+1, newx, newy))
          
      

