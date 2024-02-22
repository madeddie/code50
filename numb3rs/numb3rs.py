import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    parts = ip.split(".")
    for part in parts:
        if 0 > int(part) > 255:
            return False

        return True


if __name__ == "__main__":
    main()
