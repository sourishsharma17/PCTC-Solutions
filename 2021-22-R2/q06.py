columns = int(input())
rows = int(input())

grid = []
for i in range(rows):
  grid.append([int(thing) for thing in input()])

centre_c = columns // 2
centre_r = rows // 2

total = 0

for c in range(centre_c):
  for r in range(centre_r):
    if all((grid[r][c], grid[r][c+centre_c], grid[r+centre_r][c], grid[r+centre_r][c+centre_c])):
      total += 1

print(total)
    

