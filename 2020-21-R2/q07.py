n = int(input())
m = int(input())

grid = []

for i in range(m):
  grid.append([int(element) for element in input().split()])

ans = 0

for row in range(m):
  for col in range(n):
    for row_delta in [-1, 1]:
      for col_delta in [-1, 1]:
        new_row = row + row_delta
        new_col = col + col_delta
        if m > new_row >= 0 and n > new_col >= 0:
          ans = max(ans, grid[row][col] * grid[new_row][new_col])
        
print(ans)
