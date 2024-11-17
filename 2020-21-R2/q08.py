canvas = {}

for i in range(int(input())):
  x, y, c = input().split()
  x = int(x)
  y = int(y)

  canvas[(x,y)] = c

minx = min(coords[0] for coords in canvas.keys())
maxx = max(coords[0] for coords in canvas.keys())
miny = min(coords[1] for coords in canvas.keys())
maxy = max(coords[1] for coords in canvas.keys())

for row in range(maxy, miny-1, -1):
  curr_row = ""
  for col in range(minx, maxx+1):
    curr_row += canvas.get((col,row), ".")
  print(curr_row)
