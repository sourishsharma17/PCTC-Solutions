board = {}

for x in range(1,9):
  for y in range(1,9):
    if (y in (1,3) and x%2 == 1) or (y == 2 and x%2 == 0):
      board[(x,y)] = "w"
    elif (y in (6,8) and x%2 == 0) or (y == 7 and x%2 == 1):
      board[(x,y)] = "b"
    else:
      board[(x,y)] = "."


for turn in range(int(input())):
  move = input()
  
  chars = "abcdefgh"
  x = chars.index(move[0])+1
  y = int(move[1])
  dir = move[2]

  if turn % 2 == 0:
    board[(x,y)] = "."
    y += 1
    x += 1 if dir == "R" else -1
    if board[(x,y)] != ".":
      board[(x,y)] = "."
      y += 1
      x += 1 if dir == "R" else -1
    
    board[(x,y)] = "w"

  else:
    board[(x,y)] = "."
    y -= 1
    x += 1 if dir == "L" else -1
    if board[(x,y)] != ".":
      board[(x,y)] = "."
      y -= 1
      x += 1 if dir == "L" else -1
    
    board[(x,y)] = "b"
    

for y in range(8,0,-1):
  for x in range(1,9):
    print(board[(x,y)], end="")
  print()
  

