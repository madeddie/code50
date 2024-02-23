from datetime import date


# Date of Birth: 1999-12-31
# One thousand, four hundred forty minutes
def main():
    birthdate = input("Date of Birth: ")


def minutes(date):
    year, month, day = date.split("-")
    return (date.today() - date(int(year), int(month), int(day))).days * 24 * 60

if __name__ == "__main__":
    main()
