myString = "We are python developers"

result = myString.endswith(("pers", "a", "python", "are"))


print(result)

result = myString.find("are")

print(result)

result = myString.find("you")

print(result)

newString = myString.replace(" ", "x", 1)

print(newString)

myStringList = myString.split("e")

print(myStringList)

print(myStringList[::-1])

print(myString[::-1 ])

