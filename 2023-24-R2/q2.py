num = int(input())
total = 1

while num != 0:
  total += 1
  num -= sum(int(digit) for digit in str(num))

print(total)



