inp = input()
answer = ""

symbols = [
    "@#",
    "####",
    "###@",
    "##@#",
    "##@@",
    "#@##",
    "#@#@",
    "#@@#",
    "#@@@",
    "@@"
]

index = 0
while index < len(inp):
  if inp[index:index+2] == symbols[0]:
    answer += symbols[1]
    index += 2
    break
  elif inp[index:index+2] == symbols[9]:
    answer += symbols[0]
    index += 2
  else:
    answer += symbols[symbols.index(inp[index:index+4])+1]
    index += 4
    break
else:
  answer += symbols[1]

print(answer+inp[index:])

