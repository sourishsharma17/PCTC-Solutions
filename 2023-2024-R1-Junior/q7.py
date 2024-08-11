n = int(input())

trib = [0, 0, 1]

for i in range(35):
  trib.append(trib[-1]+trib[-2]+trib[-3])

print(trib[n-1])

