name = input()

results = []
for i in range(5):
  results.append(input())

print(results[(results.index(name))+1])

