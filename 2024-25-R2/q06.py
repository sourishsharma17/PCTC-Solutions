inp = [int(i) for i in input()]

wave = []

for sample in range(len(inp)//2):
  for tick in range(inp[sample*2+1]):
    col = ["."] * 10
    col[inp[sample*2]] = "@"

    if sample != 0 and tick == 0:
      curr = inp[sample*2]
      prev = inp[(sample-1)*2]
      for i in range(min(curr, prev), max(curr, prev)+1):
        col[i] = "@"

    wave.append(col)

wave = list(zip(*wave)) # transpose

for row in wave[::-1]:
  print(*row, sep="")

