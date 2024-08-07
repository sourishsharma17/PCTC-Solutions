lst = input()
lst = eval(lst)

ans = ""

def func(sublst):
  global ans

  newlst = []
  
  for thing in sublst:
    if isinstance(thing, list):
      func(thing)
    else:
      newlst.append(thing)

  ans += str((newlst[0] + newlst[-1])//2)
      
func(lst)
print(ans)


