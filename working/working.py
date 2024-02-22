import re
import sys


def main():
    print(convert(input("Hours: ")))

def parse_time(s):
    time, meridiem = s.split(" ")
    if ":" in time:
        hour, minute = time.split(":")
    else:
        hour = time
        minute = 0

    if int(hour) < 1 or int(hour) > 12 or int(minute) < 0 or int(minute) > 59:
        raise ValueError

    return(int(hour), int(minute), meridiem)

def generate_24hr(hour, minute, meridiem):
    if meridiem == "PM" and hour > 12:
        hour = hour + 12
    return(f"{hour:02}:{minute:02}")

def convert(s):
    output = []
    for group in re.search("(.*? (?:AM|PM)) to (.*? (?:AM|PM))", s).groups():
        hour, minute, meridiem = parse_time(group)
        output.append(generate_24hr(hour, minute, meridiem))

    return(" to ".join(output))

if __name__ == "__main__":
    main()
