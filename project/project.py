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
        "-------\n|o    |\n|  o  |\n|    o|\n-------\n",
        "-------\n|o   o|\n|     |\n|o   o|\n-------\n",
        "-------\n|o   o|\n|  o  |\n|o   o|\n-------\n",
        "-------\n|o    |\n|     |\n|    o|\n-------\n",
        "-------\n|o   o|\n|o   o|\n|o   o|\n-------\n",
    ]
}

UPPER_CATEGORY = {
    "Aces": 1,
    "Twos": 2,
    "Threes": 3,
    "Fours": 4,
    "Fives": 5,
    "Sixes": 6,
}

def upper_section_score(hand, category):
    if category not in UPPER_CATEGORY.keys():
        raise ValueError

    return sum([x for x in hand if x == UPPER_CATEGORY[category]])

def print_dice(die_faces, style="ascii"):
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
        for die_face in die_faces:
            print(DICE["UNICODE"][die_face -1], end=" ")
        print()
    else:
        die_face_lines = []
        for die_face in die_faces:
            die_face_lines.append(DICE["ASCII"][die_face -1].split("\n"))

        for i in range(5):
            for x in die_face_lines:
                print(x[i], end=" ")
            print()

        # Print identifying numbers under the dice
        for x in range(len(die_faces)):
            print(f"   {x+1}   ", end=" ")
        print()

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
            print_dice(dice_faces)
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
            print_dice(dice_faces)

        turn += 1

    while True:
        section = input("Choose upper or lower section: ").strip().lower()
        if section in ["upper", "lower"]:
            break

    while True:
        print(f"Available categories in section {section})
        category = input("Choose scoring category: ")
if __name__ == "__main__":
    main()
