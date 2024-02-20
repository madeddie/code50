camel_var = input("Gimme the humps: ")

output = ""
for char in camel_var:
  if char.isupper():
    output += "_" + char.lower()
  else:
    output += char
print(output)
