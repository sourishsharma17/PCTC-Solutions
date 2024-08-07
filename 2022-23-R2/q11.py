precalc = [0, 0, 1]

for i in range(2, 101):
  precalc.append((precalc[-1]*10) + 10**(i-1))

num = input()
total = 0

for i in range(1, len(num)+1):
  digit = int(num[-i])

  total += (digit * precalc[i])

  if digit > 7:
    total += 10**(i-1)

  if digit == 7:
    if i != 1:
      total += (int(num[-i+1:]) + 1)
    else:
      total += 1


print(total)
  





