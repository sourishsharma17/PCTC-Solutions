w = int(input())
h = int(input())

grid = [input() for i in range(h)]

curr = 0 + 0j
dir = 1 + 0j

fuel = 0
maxfuel = 0
visited = set()

while 1:
  if curr + dir in visited or not(w > curr.real + dir.real >= 0) or not(h > curr.imag + dir.imag >= 0):
    dir *= 1j

  visited.add(curr)
  maxfuel = max(maxfuel, fuel)
  
  if grid[int(curr.imag)][int(curr.real)] == "@":
    fuel = 0
    
  curr += dir
  fuel += 1

  if len(visited) == w * h:
    break
  
print(maxfuel)
  
  
    
  


