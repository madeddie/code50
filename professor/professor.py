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
    problems.append((random.randrange(10 ** (level - 1), 10 ** level), random.randrange(10 ** (level - 1), 10 ** level)))

for problem in problems:
    while True:
        answer = input(f"{problem[0]} + {problem[1]}")
        if answer == problem[0] + problem[1]:
            continue
        else:
