string = input()

state = 0

for i in string:
  if i == "R":
    state = 0
  if i == "L":
    state = min(state + 1, 2)

print(state)
  
