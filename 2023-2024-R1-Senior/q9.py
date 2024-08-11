row = int(input()) - 1
col = int(input()) - 1

grid = []

for i in range(10):
  a = [int(num) for num in input()]
  grid.append(a)

total = 0

total += sum(grid[row])

grid = list(zip(*grid))

total += sum(grid[col])

total -= grid[col][row]

print(total)


