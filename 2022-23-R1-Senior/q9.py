x = int(input())
y = int(input())

grid = [list("#"*10) for i in range(10)]

grid[y][x] = "X"

for row in grid:
    print("".join(row))
