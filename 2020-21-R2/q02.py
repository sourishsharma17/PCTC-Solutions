d = int(input())

words = [input() for i in range(2)]

sanction = 0

if "UNTUCKED" in words:
  sanction = d
if "LOOSE" in words:
  sanction = d + 5

print(sanction)
