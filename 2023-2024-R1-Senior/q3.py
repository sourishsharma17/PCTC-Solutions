price = int(input())

price *= 100

if price >= 1000:
  price *= 0.8
  price -= 400
elif price >= 400:
  price *= 0.8

print(int(price))

