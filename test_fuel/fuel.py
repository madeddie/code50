def main():
  while True:
    try:
      f = input("Fraction: ")
      p = convert(f)
      print(gauge(p))

def convert(fraction):
    x, y = fraction.split("/")
    if not x.isdecimal() or not y.isdecimal():
       raise ValueError
    elif int(x) > int(y):
       raise ValueError
    elif int(y) == 0:
       raise ZeroDivisionError
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

while True:
  try:
    fraction = input("Fraction: ")
    x, y = fraction.split("/")
    percentage = round(int(x) / int(y) * 100)
    if percentage <= 1:
      print("E")
    elif percentage > 100:
      continue
    elif percentage >= 99:
      print("F")
    else:
      print(str(percentage) + "%")
    break
  except:
    continue
