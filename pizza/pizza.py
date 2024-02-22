import csv
import sys

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
            for row in reader:
                print(row)
    except "FileNotFoundError":
        sys.exit("File does not exist")
