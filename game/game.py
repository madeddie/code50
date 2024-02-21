import random

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
        break
    except:
        continue

random_val = random.randrange(1, level)
