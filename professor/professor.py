import random
import sys

while True:
    try:
        level = int(input("Level: "))
        if level in [1, 2, 3]:
            break
        else:
            continue
    except KeyboardInterrupt:
        sys.exit()
    except:
        continue

problems = []

for i in range(10):
    problems.append(random.randrange())
