firstname = input()
surname = input()

username = ""

username += firstname[0].lower()
username += surname[0].lower()
username += surname[-1].lower()
username += str(len(firstname))

if len(set(username[:3])) != 3:
  username += "x"

print(username)
