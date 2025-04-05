n = int(input())
square = [input() for i in range(n-1)]

row = ""
invalid = False
all_nums = {str(i) for i in range(1, n+1)}

for col in range(n):
  col_nums = {square[row][col] for row in range(len(square))}

  remaining = list(all_nums - col_nums)

  if len(remaining) != 1:
    invalid = True

  row += remaining[0]

square.append(row)

for row in square:
  if len(set(row)) != n:
    invalid = True

if invalid:
  print("invalid")
else:
  print(square[-1])
  
