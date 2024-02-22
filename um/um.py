import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall('[^\w]um[^\w]', s))


if __name__ == "__main__":
    main()
