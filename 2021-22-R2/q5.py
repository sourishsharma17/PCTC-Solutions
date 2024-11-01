nums = [int(input()), int(input())]

a = min(nums)
b = max(nums)

print("£" + str(a) + "." + str(b).zfill(2))

if b < 20 or (b == 20 and a == 0):
  print("£" + str(b) + "." + str(a).zfill(2))
  
