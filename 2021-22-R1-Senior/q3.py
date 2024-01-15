pin = input()

pin = [int(num) for num in pin]

prev = pin[0]

for i in range(1,len(pin)):
  if pin[i] <= prev:
    print(pin[i])

  prev = pin[i]
