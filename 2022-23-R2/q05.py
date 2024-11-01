one = 0
two = 0

www = 0

for i in range(6):
  choices = input()

  if "W" not in choices:
    if choices[0] == "R":
      if choices[1] == "P":two+=1
      elif choices[1] == "S":one+=1
    if choices[0] == "P":
      if choices[1] == "S":two+=1
      elif choices[1] == "R":one+=1
    if choices[0] == "S":
      if choices[1] == "R":two+=1
      elif choices[1] == "P":one+=1

  else:

    if choices != "WW":
      if choices[0] == "W":
        one += 1
        www = 1
      else:
        two += 1
        www = 2
    else:
      if www == 1:
        one = 0
      elif www == 2:
        two = 0

print(f"{one}-{two}")

