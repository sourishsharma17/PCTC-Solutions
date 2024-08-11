num = int(input())
pattern = input()

pattern *= 500

i = num

print(pattern[:i])

for _ in range(num-1):
  print("."*(num//2) + pattern[i] + "."*(num//2))
  i += 1
