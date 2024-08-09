from collections import defaultdict

grid = []

for i in range(int(input())):
  grid.append(eval(input()))

while 1:

  new_coords = defaultdict(list)
  
  for sheep in grid:
    x,y = sheep
    new = (x-(x//max(1,abs(x))), y-(y//max(1,abs(y))))
    new_coords[new].append(sheep)

  new_grid = []

  for new_coord, old_coords in new_coords.items():
    if len(old_coords) == 1 and not(new_coord in grid):
      new_grid.append(new_coord)
    else:
      new_grid += old_coords    

  if grid == new_grid:
    break
    
  grid = new_grid.copy()


totaldistance = 0

for coord in grid:
  totaldistance += abs(coord[0])
  totaldistance += abs(coord[1])

print(totaldistance)
  



