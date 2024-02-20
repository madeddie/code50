def main():
    mealtime = convert(input("So you hungry now? ").strip())
    if 8 >= mealtime > 7:
        print


def convert(time):
    hours, minutes = time.split(":")
    minute_fract = minutes / 60
    return hours + minute_fract


if __name__ == "__main__":
    main()
Hints
