a = int(input())
b = int(input())
c = int(input())

ans = a**2 + b**2

if ans < c**2:
  print(f"{a} squared plus {b} squared is less than {c} squared")
elif ans == c**2:
  print(f"{a} squared plus {b} squared is equal to {c} squared")
else:
  print(f"{a} squared plus {b} squared is greater than {c} squared")
  
