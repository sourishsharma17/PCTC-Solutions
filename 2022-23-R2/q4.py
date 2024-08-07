while 1:
  w1, w2 = input().split()

  if w1 == w2:
    continue

  minl = min(len(w1), len(w2))

  for i in range(minl):
    if w1[i] != w2[i]:
      print(w1[i], w2[i])
      break

  else:
    if len(w1) == minl:
      print("_", w2[minl])
    else:
      print(w1[minl], "_")

  break
