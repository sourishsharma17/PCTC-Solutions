num = int(input())
names = [input() for i in range(num)]

while 1:
  ended = 0
  
  names.sort()
  
  eliminator = names.pop(0)

  if len(names) == 1:
    print(names[0])
    break
  if len(names) == 0:
    print("NO RESULT")
    break
  
  for letter in eliminator:
  
    to_eliminate = []
    
    for name in names:
      if letter in name:
        to_eliminate.append(name)
  
    for name in to_eliminate:
      names.remove(name)

    if len(names) == 1:
      print(names[0])
      ended = 1
      break
    if len(names) == 0:
      print("NO RESULT")
      ended = 1
      break    

  if ended == 1:
    break

