num1 = int(input())
num2 = int(input())
num3 = int(input())

diff = min(abs(num2 - num1), abs(num3 - num1))

print(min(num1, num2, num3) - diff)
print(max(num1, num2, num3) + diff)
