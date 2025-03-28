width = int(input())
height = int(input())

for row in range(height):
  line = ""

  if row % 2 == 0:
    order = "@#"
  else:
    order = "#@"

  for column in range(width):
    line += 3*order[column%2]

  print(line)
  print(line)
  print(line)
