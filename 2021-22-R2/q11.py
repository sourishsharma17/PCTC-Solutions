nums = [int(i) for i in input()]

freq = [0]*10
ans = ""

for index, value in enumerate(nums):
  for i in range(value, 10):
    freq[i] += 1

  for index1, value1 in enumerate(freq):
    if value1 >= (index//2)+1:
      ans += str(index1)
      break


print(ans)

