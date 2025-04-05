from math import comb

n = int(input())
m = int(input())

options = ["aa", "b", "c", "d"]
ans = ""

# this is the mathematical approach, but you can make this function recursive (won't get 10/10 though)
def calc(length):
  total = 0
  for aa_count in range(length//2 + 1):
    remaining_length = length - aa_count*2
    total += (3 ** remaining_length) * comb(length-aa_count, aa_count)    

  return total


while len(ans) != n:
  for option in options:
    if len(option) + len(ans) > n:
      continue

    combinations = calc(n - len(ans) - len(option))
    if combinations >= m:
      ans += option
      break
    else:
      m -= combinations

print(ans)
    

