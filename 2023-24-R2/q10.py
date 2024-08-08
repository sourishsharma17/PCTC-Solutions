from collections import defaultdict

grid = []
y = defaultdict(list)

for i in range(12):
  row = input()
  grid.append(row)
  for char in range(12):
    if row[char] == ".":continue
    y[row[char]].append((char,i))


for char, coords in y.items():
  minx = min(coord[0] for coord in coords)
  maxx = max(coord[0] for coord in coords)
  miny = min(coord[1] for coord in coords)
  maxy = max(coord[1] for coord in coords)

  width = maxx - minx + 1
  height = maxy - miny + 1
  area = width * height

  if len(coords) == area:
    break


for row in grid:
  print(row.replace(char, "."))


