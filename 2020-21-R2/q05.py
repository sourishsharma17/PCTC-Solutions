scores = []

for i in range(int(input())):
  name, c, bw = input().split()
  c = int(c)
  bw = int(bw)

  scores.append((2*c+bw, c, name))

scores.sort()

print(scores[-1][2])
