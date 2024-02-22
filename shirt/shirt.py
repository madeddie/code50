import sys

from PIL import Image, ImageOps


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
    outfile = sys.argv[2]

try:
    shirt = Image.open("shirt.png")
except "FileNotFoundError":
    sys.exit("shirt.png does not exist")

try:
    inimage = Image.open(infile)
except "FileNotFoundError":
    sys.exit(f"{infile} does not exist")

inimage_resized = ImageOps.fit(inimage, shirt.size)
inimage_resized.paste(shirt)
inimage_resized.save(outfile)
