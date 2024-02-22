import csv
import sys


if len(sys.argv) != 3:
    sys.exit(f"Usage: {sys.argv[0] }")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    filename = sys.argv[1]
    lines = []
    try:
        with open(filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            print(tabulate(reader, headers="keys", tablefmt="grid"))
    except "FileNotFoundError":
        sys.exit("File does not exist")
