track = []

for i in range(6):
  row = input()
  if "#" in row:
    pos = (i, row.index("#"))
  track.append(list(row))

track[pos[0]][pos[1]] = "0"

vis = {pos}

while 1:
  y, x = pos

  flag = 0

  for yy in range(y-1, y+2):
    for xx in range(x-1, x+2):
      xx %= 6
      yy %= 6
      if (yy,xx) != (y,x) and (yy == y or xx == x):
        if track[yy][xx] == "0" and (yy, xx) not in vis:
          pos = (yy, xx)
          vis.add(pos)
          flag = 1

  if flag == 0:
    break


track[pos[0]][pos[1]] = "#"

for row in track:
  print(*row, sep="")
          




