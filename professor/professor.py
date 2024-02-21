import random
import sys

def main():
    level = get_level()
    score = 0
    problems = generate_problems(level)

    for problem in problems:
        tries = 3
        while tries > 0:
            answer = input(f"{problem[0]} + {problem[1]} = ")
            if not answer.isdecimal():
                print("EEE")
                tries -= 1
            elif int(answer) == problem[0] + problem[1]:
                score += 1
                break
            else:
                print("EEE")
                tries -= 1
        else:
            print(f"{problem[0]} + {problem[1]} = {problem[0] + problem[1]}")

    print(f"Score: {score}")

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
    if level == 1:
        return random.randrange((10 ** (level - 1)) -1, (10 ** level) -1)
    else:
        return random.randrange(10 ** (level - 1), 10 ** level)

def generate_problems(level):
    problems = []
    for i in range(10):
        problems.append((generate_integer(level), generate_integer(level)))
    return problems

if __name__ == "__main__":
    main()
