devowel = input("You have vowerls where? ")
for char in ["A", "E", "I", "O", "U"]:
    devowerl = devowel.replace(char, "")
    devowel = devowel.replace(char.lower(), "")

print(devowel)
