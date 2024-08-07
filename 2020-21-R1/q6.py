chairs = [int(input()) for i in range(20)]

chairs.insert(0,0)
chairs.append(0)

total = 0

for i in range(1, 21):
  if sum(chairs[i-1:i+2]) == 0:
    chairs[i] = 1
    total += 1

print(total)
