start = input()
target = input()

if start > target:
  print(2)
else:
  print(1)

print(abs(ord(start) - ord(target)))
