num1 = int(input())
num2 = int(input())

vals = []

vals.append(abs(100 - (num1 + num2)))
vals.append(abs(100 - (num2 - num1)))
vals.append(abs(100 - (num1 - num2)))

print(min(vals))

