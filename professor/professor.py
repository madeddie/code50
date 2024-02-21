import random
import sys

while True:
    try:
        level = int(input("Level: "))
        if level in [1, 2, 3]:
            if level == 1:
                level = 10
            elif level == 2:
                level = 100
            else:
                level = 1000
        else:
            continue
    except KeyboardInterrupt:
        sys.exit()
    except:
        continue

problems = []

for i in range(10):
    problems.append(random.rand)
