import random

while True:
    try:
        level = int(input("Level: "))
        break
    except:
        continue

random_val = random.randrange(1, level)
