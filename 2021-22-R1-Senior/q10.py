message = input()

message = message.replace(" ", "")

message = message.replace("A", "a")
message = message.replace("U", "A").replace("O", "U")
message = message.replace("I", "O").replace("E", "I")
message = message.replace("a", "E")

print(message)
