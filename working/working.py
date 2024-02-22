import re
import sys


def main():
    print(convert(input("Hours: ")))

def parse_time(s):
    time, meridiem = s.split(" ")
    if ":" in time:
        hour, minute = time.split()
    else:
        hour = time
        minute = 0

    if 1 < int(hour) > 12 or 0 < int(minute) > 60:
        raise ValueError


def convert(s):
    start, stop = re.search("(.*? (?:AM|PM)) to (.*? (?:AM|PM))", s).groups()
    parse_time(start)


if __name__ == "__main__":
    main()
