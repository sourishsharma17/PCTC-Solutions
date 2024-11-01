board = [[""]*4 for i in range(4)]

for i in range(16):
  inp = input().replace("a","0").replace("b","1").replace("c","2").replace("d","3")

  if i % 2 == 0:
    symbol = "O"
  else:
    symbol = "X"

  board[4-int(inp[1])][int(inp[0])] = symbol



ans = ""

for symbol in "OX":
  score = 0
  
  for _ in range(2):
    for line in board:
      if line.count(symbol) == 4:
        score += 2
      else:
        if symbol*3 in "".join(line):
          score += 1
    
    board = list(zip(*board))
  
  for _ in range(2):
    diag = [board[i][i] for i in range(4)]
    if diag.count(symbol) == 4:
      score += 2
    else:
      if symbol*3 in "".join(diag):
        score += 1
    
    diag = [board[i][i+1] for i in range(3)]
    if diag.count(symbol) == 3:
      score += 1
    
    diag = [board[i+1][i] for i in range(3)]
    if diag.count(symbol) == 3:
      score += 1
    
    board = [line[::-1] for line in board]

  ans += str(score)
  ans += "-"



print(ans[:-1])
   
