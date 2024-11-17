from string import ascii_lowercase, ascii_uppercase

ages = list(ascii_lowercase) + list(ascii_uppercase)

current = input()

print(ages[max(ages.index(current)-1, 0)])

