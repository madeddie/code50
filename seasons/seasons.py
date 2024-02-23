from datetime import date

import inflect

p = inflect.engine()


# Date of Birth: 1999-12-31
# One thousand, four hundred forty minutes
def main():
    birthdate = input("Date of Birth: ")
    minutes = get_minutes(birthdate)
    print(f"{inflect_time(minutes).capitalize()} minutes")

def get_minutes(bd):
    year, month, day = bd.split("-")
    return (date.today() - date(int(year), int(month), int(day))).days * 24 * 60

def inflect_time(minutes):
    return p.number_to_words(minutes, andword="")

if __name__ == "__main__":
    main()
