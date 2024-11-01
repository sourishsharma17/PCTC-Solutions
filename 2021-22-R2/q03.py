n = int(input())
m = int(input())
char1 = input()
char2 = input()

centre = n//2
m = m//2

mat = [[" " for i in range(n)] for i in range(n)]

for y in range(n):
  for x in range(n):
    if x == 0 or x == n-1 or y == 0 or y == n-1:
      mat[y][x] = char1
    if centre + m >= x >= centre - m and centre + m >= y >= centre - m:
      mat[y][x] = char2
    
for row in mat:
  print(*row, sep="")

