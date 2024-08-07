grid = [[f"{y}{x}" for x in range(10)] for y in range(10)]

for _ in range(int(input())):
  instruction = input()

  start, end = int(instruction[1]), int(instruction[-1])

  if instruction[0] == "r":
    for _ in range(end - start + 1):
      grid.pop(start)
  else:
    grid = list(zip(*grid))
    for _ in range(end - start + 1):
      grid.pop(start)
    grid = list(zip(*grid))


for row in grid:
  print(*row)

