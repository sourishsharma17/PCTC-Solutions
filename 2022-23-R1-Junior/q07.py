growth = int(input())
days = int(input())

length = 1

for i in range(days):
  print("o"*length + "{")

  length += growth
