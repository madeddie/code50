####
# This is a game of yahtzee on the CLI
# made by edwin@madtech.cx for CS50 Python
from random import randrange

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

def roll_dice(num_of_dice):
    dice_faces = []
    for _ in range(num_of_dice):
        dice_faces.append(randrange(6) + 1)
def main():
    dice
