import sys

from PIL import Image


def check_ext(filename):
    extension = filename.split(".")[-1]
    if extension.lower() not in ['jpg', 'jpeg', 'png']:
        sys.exit("Wrong file format, only allow jpg and png")

    return extension.lower()

if len(sys.argv) != 3:
    sys.exit(f"Usage: {sys.argv[0]} <INPUT> <OUTPUT>")
elif check_ext(sys.argv[1]) != check_ext(sys.argv[2]):
    sys.exit(f"Files need to have the same extension")
else:
    infile = sys.argv[1]
    try:
        with open(infile, "r") as shirt:
            shirt = Image.open(shiu)
    except "FileNotFoundError":
        sys.exit("File does not exist")

print(shirt.size)
