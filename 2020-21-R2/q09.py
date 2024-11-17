num, target = int(input()), int(input())

total = num
seen = {num}
terms = [num]

def next_term(num):
  global total, seen, terms
  
  num *= num
  while num >= 1000000:
    num = str(num)
    half = len(num)//2
    num = int(num[:half]) + int(num[half:])
  while num in seen:
    num += 1

  total += num
  seen.add(num)
  terms.append(num)

  return num

for i in range(9999):
  num = next_term(num)

while total != target:
  num = next_term(num)
  total -= terms.pop(0)

print(next_term(num))
  
