first_day = input()
leap = input()

if leap == "y":
  days = 366
else:
  days = 365

weeks, extra_days = divmod(days, 7)

answer = weeks

days_of_week = "SU / MO / TU / WE / TH / FR / SA".split(" / ")

if 7 - days_of_week.index(first_day) <= extra_days:
  answer += 1

print(answer)
