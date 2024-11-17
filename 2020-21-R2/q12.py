from collections import defaultdict
from heapq import *

trains = defaultdict(list)

n = input()
for i in range(int(input())):
  line = input().replace(":"," ").split()
  start = line[0]
  end = line[1]
  depart = int(line[2])*60 + int(line[3])
  arrival = int(line[4])*60 + int(line[5])

  trains[start].append((end, depart, arrival))


heap = [(5*60-3, "1")]
visited = set()

while heap:
  time, town = heappop(heap)

  if town == n:
    print(f"{time//60:02}:{time%60:02}")
    break
  
  if town in visited:
    continue

  visited.add(town)

  for train in trains[town]:
    if train[1] >= time+3:
      heappush(heap,(train[2], train[0]))




