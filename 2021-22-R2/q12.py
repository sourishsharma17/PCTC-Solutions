caves = input()
target = int(input())

if len(caves) == 1:
  print(caves)
else:
  dp = [0]*len(caves)
  
  dp[-1] = 1
  dp[-2] = 1
  
  for cave in range(-3, -len(caves)-1, -1):
    dp[cave] = dp[cave+1] + dp[cave+2]
  
  ans = "A"
  pos = 0
  while pos != len(dp)-1:
    if dp[pos+1] >= target:
      pos += 1
    else:
      pos += 2
      target -= dp[pos-1]
  
    ans += caves[pos]
  
  print(ans)
  
  
   
