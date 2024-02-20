import mimetypes

filename = input("what is the filename? ").strip().lower()
ext = "." + filename.split(".")[-1]
try:
    print(mimetypes.types_map[ext])
except:
    print("application/octet-stream")
