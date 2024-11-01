num = int(input())

print("___")

for i in range(num):
  if i == num-1:
    print("#" * (3 + i*2) + "]___")
  else:
    print("#" * (3 + i*2) + "]_")
