nums = input()
row = int(input())

top = nums[0]
tree = {top: [-1, -1]}

ans = []

for i in range(1, 10):
  num = nums[i]

  current = top
  rowcurrent = 1

  while 1:
    if num > current:
      newcurrent = tree[current][1]
      if newcurrent == -1:
        tree[current][1] = num
        tree[num] = [-1, -1]
        if rowcurrent + 1 == row:
          ans.append(num)
        break
        
    else:
      newcurrent = tree[current][0]
      if newcurrent == -1:
        tree[current][0] = num
        tree[num] = [-1, -1]
        if rowcurrent + 1 == row:
          ans.append(num)
        break
      
    current = newcurrent
    rowcurrent += 1

if row == 1:
  print(top)
else:
  print(*sorted(ans))

