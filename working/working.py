import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    res = re.search("(.*? (?:AM|PM)) to (.*? (?:AM|PM))", s)


...


if __name__ == "__main__":
    main()
