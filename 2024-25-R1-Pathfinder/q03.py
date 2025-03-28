inp = input()

lst = inp.split(",")

for pet in lst:
  if pet[1:] == ":=":
    print(pet[0])
