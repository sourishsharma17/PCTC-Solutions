nums = [input() for i in range(8)]

total = 0

for num in nums:
  if sum(int(digit) for digit in num) % 2 == 1:
    total += 1

print(total)
