import sys

while True:
    try:
        level = int(input("Level: "))
        if level not in [1, 2, 3]:
            continue
        break
    except KeyboardInterrupt:
        sys.exit()
    except:
        continue

print(level)
