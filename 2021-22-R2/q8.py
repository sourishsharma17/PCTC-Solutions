from collections import defaultdict

people = defaultdict(int)

for i in range(int(input())):
  line = input().replace(" ", ":")
  name, choice, name2 = line.split(":")

  if choice == "UP":
    people[name2] += 1
  else:
    people[name2] -= 1

  people[name] += 0  


min_vote = min(people.values())
names = []

for name, vote in people.items():
  if vote == min_vote:
    names.append(name)

names.sort()
for name in names:
  print(name)
  
