string1 = "hello , how are you"

print(string1)

try:
  print(string2)
except NameError:
  print("Variable string2 is not defined")
except:
  print("another error")