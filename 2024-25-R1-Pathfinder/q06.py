nums = [int(input()) for i in range(4)]
nums.append(nums[0])

ans = ""

for i in range(4):
  ans += str((nums[0] + nums[1]) % 10)
  nums = nums[1:]

print(ans)
