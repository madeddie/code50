while True:
  try:
    fraction = input("Fraction: ")
    x, y = fraction.split("/")
    percentage = int(int(x) / int(y) * 100)
    print(str(percentage) + "%")
    break
  except:
    raise
