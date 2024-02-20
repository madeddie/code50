while True:
  try:
    fraction = input("Fraction: ")
    x, y = fraction.split("/")
    percentage = round(int(x) / int(y) * 100)
    if percentage <= 1:
      print("E")
    else:
      print(str(percentage) + "%")
    break
  except:
    raise
