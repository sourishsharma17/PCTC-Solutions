start = int(input())
prev = start

while 1:
    price = int(input())

    if price < prev:
        break

    prev = price

print(price - start)
