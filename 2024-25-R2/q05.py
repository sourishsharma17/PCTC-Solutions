expire = int(input())
day, month = [int(i) for i in input().split("/")]

total = 1

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(month, expire):
  total += days_in_month[i]

total += days_in_month[month-1] - day 

print(total)
