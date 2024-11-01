img1 = [input() for i in range(10)]

def extract(lst):
  for i in range(2):
    ones = [i for i in range(10) if "1" in lst[i]]
    lst = lst[ones[0]:ones[-1]+1]
    lst = list(zip(*lst))

  return lst

img1 = extract(img1)
matches = 0

for i in range(5):
  imgN = [input() for i in range(10)]
  imgN = extract(imgN)
  if imgN == img1:
    matches += 1


count_ones = 0
for line in img1:
  count_ones += line.count("1")

print(count_ones * matches)
