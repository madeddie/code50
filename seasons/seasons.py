import re
import sys
from datetime import date

import inflect

p = inflect.engine()


# Date of Birth: 1999-12-31
# One thousand, four hundred forty minutes
def main():
    birthdate = input("Date of Birth: ")
    if not re.search(r"\d{4}-\d{1,2}-\d{1,2}", birthdate):
        sys.exit("Invalid date")
    minutes = get_minutes(birthdate)
    print(f"{inflect_time(minutes).capitalize()} minutes")

def get_minutes(bd, today=None):
    if not today:
        today = date.today()
    year, month, day = bd.split("-")
    return (today - date(int(year), int(month), int(day))).days * 24 * 60

def inflect_time(minutes):
    return p.number_to_words(minutes, andword="")

if __name__ == "__main__":
    main()
