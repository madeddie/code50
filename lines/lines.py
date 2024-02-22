import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
else:
    filename = sys.argv[1]
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except "FileNotFoundError":
        sys.exit("File does not exist")

print(len(lines))
