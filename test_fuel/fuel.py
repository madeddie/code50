def main():
  while True:
    try:
      f = input("Fraction: ")
      p = convert(f)
    except:
      continue
    else:
      print(gauge(p))
      break

def convert(fraction):
    x, y = fraction.split("/")
    if not x.isdecimal() or not y.isdecimal():
       raise ValueError
    elif int(y) == 0:
       raise ZeroDivisionError
    elif int(x) > int(y):
       raise ValueError

    return round(int(x) / int(y) * 100)


def gauge(percentage):
    if percentage <= 1:
      return "E"
    elif percentage >= 99:
      return "F"
    else:
      return f"{percentage}%"


if __name__ == "__main__":
    main()
