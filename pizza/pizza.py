import csv
import sys

from tabulate import tabulate


if len(sys.argv) != 2:
    sys.exit("Please give only 1 command-line arguments")
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
