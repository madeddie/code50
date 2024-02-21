import random
import sys

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
        break
    except KeyboardInterrupt:
        sys.exit()
    except:
        continue

random_val = random.randrange(1, level + 1)

def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                continue
            break
        except KeyboardInterrupt:
            sys.exit()
        except:
            continue

    return guess

while True:
    guess = get_guess()
    if guess == random_val:
        print("Just Right!")
        break
    elif guess > random_val:
        print("Too Large!")
    else:
        print("Too Small!")
