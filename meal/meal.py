def main():
    mealtime = convert(input("So you hungry now? ").strip())
    if 8 >= mealtime >= 7:
        print("breakfast time")
    elif 12 >= mealtime >= 13:
        print("lunch time")
    elif 18 >= mealtime >= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    minute_fract = int(minutes) / 60
    return int(hours) + minute_fract


if __name__ == "__main__":
    main()
