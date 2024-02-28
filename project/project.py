####
# This is a game of yahtzee on the CLI
# made by edwin@madtech.cx for CS50 Python
from random import randint

DICE = {
    "UNICODE": [
        "\u2680",
        "\u2681",
        "\u2682",
        "\u2683",
        "\u2684",
        "\u2685",
    ],
    "ASCII": [
        "-------\n|     |\n|  o  |\n|     |\n-------\n",
        "-------\n|o    |\n|     |\n|    o|\n-------\n",
        "-------\n|o    |\n|  o  |\n|    o|\n-------\n",
        "-------\n|o   o|\n|     |\n|o   o|\n-------\n",
        "-------\n|o   o|\n|  o  |\n|o   o|\n-------\n",
        "-------\n|o   o|\n|o   o|\n|o   o|\n-------\n",
    ]
}

def xofakind(hand, kind):
    score[3] = 17
    score[4] = 24
    for value in set(hand):
        if hand.count(value) >= kind:
            return score[kind]
    return 0

def fullhouse(hand):
    twos = False
    threes = False
    for value in set(hand):
        if hand.count(value) == 2:
            twos = True
        elif hand.count(value) == 3:
            threes = True

    if twos and threes:
        return 25

    return 0

CATEGORIES = {
    "upper": {
        "aces": 1,
        "twos": 2,
        "threes": 3,
        "fours": 4,
        "fives": 5,
        "sixes": 6,
    },
    "lower": {
        "three": lambda hand: xofakind(hand, kind=3),
        "threes": lambda hand: xofakind(hand, kind=3),
        "threeofakind": lambda hand: xofakind(hand, kind=3),
        "four": lambda hand: xofakind(hand, kind=4),
        "fours": lambda hand: xofakind(hand, kind=4),
        "fourofakind": lambda hand: xofakind(hand, kind=4),
        "full": fullhouse,
        "fullhouse": fullhouse,
    }
}

def upper_section_score(hand, category):
    if category not in CATEGORIES["upper"].keys():
        raise ValueError

    return sum([x for x in hand if x == CATEGORIES["upper"][category]])

def visualize_dice(die_faces, style="ascii"):
    """
    Print out the dice in either unicode or ascii art

    :param die_faces: Die face values to print
    :type die_faces: list of int
    :param style: unicode or ascii style
    :type style: str
    """
    if style not in ["unicode", "ascii"]:
        raise ValueError

    if style == "unicode":
        return " ".join([DICE['UNICODE'][die_face -1] for die_face in die_faces])
    else:
        output = ""
        die_face_lines = []
        for die_face in die_faces:
            die_face_lines.append(DICE["ASCII"][die_face -1].split("\n"))

        for i in range(5):
            for x in die_face_lines:
                output += x[i]
            output += "\n"

        # Print identifying numbers under the dice
        for x in range(len(die_faces)):
            output += f"   {x+1}   "
        output += "\n"

        return output

def roll_dice(num_of_dice):
    dice_faces = []
    for _ in range(num_of_dice):
        dice_faces.append(randint(1,6))

    return dice_faces

def main():
    dice_faces = []
    turn = 1
    while turn < 4:
        if turn == 1:
            dice_faces = roll_dice(5)
            print(visualize_dice(dice_faces))
        else:
            dice_to_roll = input("Input which dice to re-roll seperated by spaces: ").strip().split()
            if not dice_to_roll:
                print("Nothing to re-roll")
                turn += 1
                break
            dice_to_roll = sorted([int(x) for x in dice_to_roll], reverse=True)
            num_to_roll = len(dice_to_roll)
            for dice in dice_to_roll:
                dice_faces.pop(dice -1)
            dice_faces = dice_faces[0:5-num_to_roll]
            dice_faces.extend(roll_dice(num_to_roll))
            print(visualize_dice(dice_faces))

        turn += 1

    while True:
        section = input("Choose upper or lower section: ").strip().lower()
        if section in ["upper", "lower"]:
            break

    while True:
        print(f"Available categories in section {section}:\n{', '.join(CATEGORIES['upper'].keys())}")
        category = input("Choose scoring category: ").strip().lower()
        if category in CATEGORIES['upper'].keys():
            break

    print(f"Final hand: {dice_faces}")

    if section == "upper":
        print(f"Score {section}/{category}: {upper_section_score(dice_faces, category)}")
    if section == "lower":
        print(f"Score {section}/{category}: {})
if __name__ == "__main__":
    main()
