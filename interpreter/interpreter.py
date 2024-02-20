expression = input("what can i deduce, oh deuce? ").strip()

x, y, z = expression.split(" ")

if y == "+":
    print(float(x) + float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "*":
    print(float(x) * float(z))
elif y == "/":
    print(float(x) / float(z))
