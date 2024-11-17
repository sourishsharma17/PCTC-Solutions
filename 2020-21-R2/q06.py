from collections import deque

word = deque(input())
n = int(input())

ans = ""

while word:
  word.rotate(-n)
  ans += word.popleft()

print(ans)
