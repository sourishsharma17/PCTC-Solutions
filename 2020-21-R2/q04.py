score = 0
time = 0

while 1:
  card = input().replace("A","1").replace("T","10").replace("J","11").replace("Q","12").replace("K","13")
  score += int(card)
  time += 1

  if score < time*7:
    break

print(time*10)
