pay = int(input())
sold = int(input())

if sold > 10:
  pay += 60
elif sold > 8:
  pay += 40
elif sold > 5:
  pay += 20

print(pay)
