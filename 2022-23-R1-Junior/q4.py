age = int(input())

if age >= 10:
  print("B")
else:
  if age >= 8:
    print("A")
  elif age >= 6:
    parent = input()
    if parent == "Y":
      print("A")
    else:
      print("N")
  else:
    print("N")
