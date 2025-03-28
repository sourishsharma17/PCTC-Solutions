map = [list(input()) for i in range(int(input()))]

current = map[0].index("#")
gate = 0

for line in range(len(map)):
  map[line][current] = "#"

  if gate == 1:
    pos = map[line-1].index("@")
    if current < pos:
      for col in range(current+1, pos+2):
        map[line][col] = "#"
    else:
      for col in range(current-1, pos-2, -1):
        map[line][col] = "#"
        
    gate += 1
    current = col
  
  if "@" in map[line]:
    gate += 1
    gate %= 3

  print(*map[line], sep="")
  
