maximum = int(input())

for num in range(1, maximum):

  cube = num**3

  if cube <= maximum:
    print(cube)
  else:
    break
