cards = input()

prev = "blank"
total = 0

for card in cards:
  if card == prev:
    total += 1
    prev = "blank"
  else:
    prev = card

print(total)
