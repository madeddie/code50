camel_var = input("Gimme the humps: ")

output = ""
for char in name:
  if char.isupper():
    output += "_" + char.lower()
  else:
    output += char
print(output)
