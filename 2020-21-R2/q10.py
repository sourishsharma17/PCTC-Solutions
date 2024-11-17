from math import prod, factorial
from collections import Counter

letters = list(input())
target = int(input())

answer = ""

while letters:
  for letter in sorted(list(set(letters))):
    letters.remove(letter)
    n_perms = factorial(len(letters))/prod(factorial(freq) for freq in Counter(letters).values())
    if n_perms >= target:
      answer += letter
      break
    else:
      target -= n_perms
      letters.append(letter)

print(answer)


