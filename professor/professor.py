import random
import sys

def main():
    level = get_level()
    problems = []

    for i in range(10):
        problems.append((generate_integer(level), generate_integer(level)))

    for problem in problems:
        tries = 3
        while tries > 0:
            answer = input(f"{problem[0]} + {problem[1]} = ")
            if int(answer) == problem[0] + problem[1]:
                break
            else:
                print("EEE")
                tries -= 1


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                continue
        except KeyboardInterrupt:
            sys.exit()
        except:
            continue

def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError
    return random.randrange(10 ** (level - 1), 10 ** level)

main()
