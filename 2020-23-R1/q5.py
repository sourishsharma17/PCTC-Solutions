minl = int(input())
maxl = int(input())

valid = 0
invalid = 0

while 1:
  carrot = int(input())

  if carrot == -1:
    break

  if maxl >= carrot >= minl:
    valid += 1
  else:
    invalid += 1

print(valid)
print(invalid)
