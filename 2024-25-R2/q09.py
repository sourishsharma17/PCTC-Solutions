from collections import deque

grid = [list(input()) for i in range(10)]

total = 0

q = deque([(0,0)])
visited = set()

while q:
  x, y = q.popleft()

  if (x,y) in visited:
    continue
  visited.add((x,y))

  new_y = y - 1
  if 10 > new_y >= 0:
    if grid[new_y][x] == "1":
      total += 1
    else:
      q.append((x, new_y))

  new_y = y + 1
  if 10 > new_y >= 0:
    if grid[new_y][x] == "1":
      total += 1
    else:
      q.append((x, new_y))

  new_x = x - 1
  if 10 > new_x >= 0:
    if grid[y][new_x] == "1":
      total += 1
    else:
      q.append((new_x, y))

  new_x = x + 1
  if 10 > new_x >= 0:
    if grid[y][new_x] == "1":
      total += 1
    else:
      q.append((new_x, y))

print(total)
