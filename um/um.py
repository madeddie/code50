import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall('\W?um\W?', s))


if __name__ == "__main__":
    main()
