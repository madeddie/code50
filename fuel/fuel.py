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
