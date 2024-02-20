def main():
    mealtime = convert(input("So you hungry now? ").strip())
    if 8 >= mealtime >= 7:
        print("breakfast time")
    elif 13 >= mealtime >= 12:
        print("lunch time")
    elif 19 >= mealtime >= 18:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    minute_fract = int(minutes) / 60
    return int(hours) + minute_fract


if __name__ == "__main__":
    main()
