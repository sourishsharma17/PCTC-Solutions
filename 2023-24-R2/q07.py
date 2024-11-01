m1 = []
m2 = []

for i in range(3):
  m1.append(eval(input()))

for i in range(3):
  m2.append(eval(input()))

ans = []

m2 = list(zip(*m2))

for i in range(3):
  row = []
  for j in range(3):
    row.append(sum(map(lambda pair: pair[0] * pair[1],zip(m1[i], m2[j]))))

  ans.append(row)


for i in ans:
  print(*i, sep=",")


