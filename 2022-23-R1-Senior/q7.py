total = 0
count = 0

while 1:
    total += int(input())
    count += 1

    if total > 20:
        total = 0
    elif total == 20:
        break

print(count)
