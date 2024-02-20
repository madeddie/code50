devowel = input("You hate vowels where? ").strip()
for char in ["A", "E", "I", "O", "U"]:
    devowel = devowel.replace(char, "")
    devowel = devowel.replace(char.lower(), "")

print(devowel)
