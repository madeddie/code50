from datetime import date


# Date of Birth: 1999-12-31
# One thousand, four hundred forty minutes
def main():
    birthdate = input("Date of Birth: ")
    minutes = get_minutes(birthdate)
    print(minutes)

def get_minutes(bd):
    year, month, day = bd.split("-")
    return (date.today() - date(int(year), int(month), int(day))).days * 24 * 60

if __name__ == "__main__":
    main()
