apples = 50
oranges = 50

while 1:
  fruit = input()
  num = int(input())

  if fruit == "APPLES":
    if num > apples:
      apples = 0
      break
    apples -= num

    if apples == 0:
      break

  else:
    if num > oranges:
      oranges = 0
      break
    oranges -= num

    if oranges == 0:
      break

print(oranges + apples)
