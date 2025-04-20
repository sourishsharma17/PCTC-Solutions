size, start, end = [int(input()) for i in range(3)]

def coords(target):
  row = 0
  cells = 1
  
  for diff in range(2, size+1):
    if cells >= target:
      current = (cells - (diff - 1)) + 1
      y = 0
      x = row
      while current != target:
        current += 1
        x -= 1
        y += 1
      break
  
    cells += diff
    row += 1
    
  else:
    for diff in range(size-1, 0, -1):
      if cells >= target:
        current = cells - diff
        x = size - 1
        y = row - size + 1
        while current != target:
          current += 1
          x -= 1
          y += 1
        break
  
      cells += diff
      row += 1

  return (x, y)
    
x1, y1 = coords(start)
x2, y2 = coords(end)

diffx = x2 - x1
diffy = y2 - y1

total = 1

if diffx>0 and diffy<0:
  right_steps = min(diffx, -diffy)
  total += right_steps
  diffx -= right_steps
  diffy += right_steps
if diffx<0 and diffy>0:
  left_steps = min(-diffx, diffy)
  total + left_steps
  diffx += left_steps
  diffy -= left_steps

total += abs(diffx) + abs(diffy)

print(total)


  
