import csv
import sys


def check_ext(filename):
    extension = filename.split(".")[-1]
    if extension.lower() not in ['jpg', 'jpeg', 'png']:
        sys.exit("Wrong file format, only allow jpg and png")

    return extension.lower()

if len(sys.argv) != 3:
    sys.exit(f"Usage: {sys.argv[0] <INPUT> <OUTPUT>}")
elif check_ext(sys.argv[1]) != check_ext(sys.argv[2]):
    sys.exit(f"Files need to have the same extension")
else:
    infile = sys.argv[1]
    lines = []
    try:
        with open(filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            print(tabulate(reader, headers="keys", tablefmt="grid"))
    except "FileNotFoundError":
        sys.exit("File does not exist")
