import csv
import sys

if len(sys.argv) != 3:
    sys.exit(f"Usage: {sys.argv[0]} <INFILE> <OUTFILE>")

infile = sys.argv[1]
outfile = sys.argv[2]

after = []
try:
    with open(infile, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            firstname, lastname = row.split(", ")
            after.append{}
except "FileNotFoundError":
    sys.exit("File does not exist")
