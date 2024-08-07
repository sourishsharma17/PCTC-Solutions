pages = [0]

for i in range(int(input())):
  pages.append(int(input()))


ans = {}
calculated = set()

for page in range(len(pages)):

  if page in calculated:
    continue
    
  visitedlst = []
  visited = set()
  next = page
  
  while next not in visited:
    visited.add(next)
    visitedlst.append(next)
    next = pages[next]

    if next in calculated:
      length = ans[next]
      for i in range(len(visited)):
        ans[visitedlst[i]] = length + (len(visited)-i)
        calculated.add(visitedlst[i])
      break
      
  else:
    first = visitedlst.index(next)
    length = len(visited) - first
  
    for i in range(first, len(visited)):
      ans[visitedlst[i]] = length
      calculated.add(visitedlst[i])
  
    for i in range(first):
      ans[visitedlst[i]] = length + (first-i)
      calculated.add(visitedlst[i])

finalans1 = max(ans.values())
finalans2 = list(ans.values()).count(finalans1)

print(finalans1)
print(finalans2)










