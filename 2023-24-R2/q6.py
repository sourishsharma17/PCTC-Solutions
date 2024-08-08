side = int(input())

picture = []

for i in range(side):
  picture.append(input())


for i in range(side):
  if picture[i].count(".") != side:
    startrow = i
    break

for i in range(side-1, -1, -1):
  if picture[i].count(".") != side:
    endrow = i
    break

picture = list(zip(*picture))

for i in range(side):
  if picture[i].count(".") != side:
    startcolumn = i
    break

for i in range(side-1, -1, -1):
  if picture[i].count(".") != side:
    endcolumn = i
    break

picture = list(zip(*picture))

for i in range(startrow, endrow+1):
  print(*picture[i][startcolumn : endcolumn+1], sep="")



