import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    res = re.search("src=\"https://.*?\.youtube\.com/embed/(.*?)\"", s)
    return(f"https://youtu.be/{res[1]}")


if __name__ == "__main__":
    main()
