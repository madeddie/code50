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

    print(hour, minute)
    if int(hour) < 1 or int(hour) > 12 or int(minute) < 0 or int(minute) > 60:
        raise ValueError


def convert(s):
    start, stop = re.search("(.*? (?:AM|PM)) to (.*? (?:AM|PM))", s).groups()
    parse_time(start)


if __name__ == "__main__":
    main()
