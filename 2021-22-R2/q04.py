while 1:
  sentence = input()

  if sentence == "goodbye":
    print("see you!")
    break

  first_word = sentence.split()[0]
  
  if sentence[-1] == "?":
    print("not sure really")
  elif first_word in ("how", "what", "why", "who", "when", "where"):
    print("not sure really")
  else:
    print("but why?")
