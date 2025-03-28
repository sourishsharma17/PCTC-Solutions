nums = [input() for i in range(10)]

happy = 0
prev = 0

for num in nums:
  if len(num) >= 3:
    happy += 1
    prev = 1
  elif len(num) == 2:
    if prev:
      happy += 1
  else:
    prev = 0

print(happy)
