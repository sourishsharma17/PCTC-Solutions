jm = input()
sm = input()

j = 0
s = 0

if jm == sm:
  j += 1
  s += 1
  j += int(input())
  s += int(input())
else:
  if (jm == "paper" and sm == "rock") or (jm == "rock" and sm =="scissors") or (jm == "scissors" and sm == "paper"):
    j += 5
  else:
    s += 5

print(f"{j}-{s}")
