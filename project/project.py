####
# This is a game of yahtzee on the CLI
# made by edwin@madtech.cx for CS50 Python
from random import randint

# This constant defines the characters and ascii art to print the dice
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

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.categories = {
            "upper": [],
            "lower": [],
        }

def xofakind(hand, kind):
    """Finds an X amount of equal values in the hand
    Used for Three of a kind, Four of a kind and Yahtzee (5 of a kind)
    """
    score = {}
    score = {
        3: 17,
        4: 24,
        5: 50,
    }
    for value in set(hand):
        if hand.count(value) >= kind:
            return score[kind]
    return 0

def fullhouse(hand):
    """Finds if the hand has 2 of the same values and 3 of another value
    """
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

def straight(hand, kind="small"):
    """Finds straights in the hands, straights being sequential numbers
    Small straights need 4 sequential numbers, large need 5
    """
    score = {
        "small": 30,
        "large": 40,
    }
    sets = {
        "small": [
            {1, 2, 3, 4},
            {2, 3, 4, 5},
            {3, 4, 5, 6},
        ],
        "large": [
            {1, 2, 3, 4, 5},
            {2, 3, 4, 5, 6},
        ]
    }

    for checkset in sets[kind]:
        if not checkset - set(hand):
            return score[kind]

    return 0

def chance(hand):
    return(sum(hand))

# This constant defines the section, categories and their scores
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
        # "three": lambda hand: xofakind(hand, kind=3),
        # "threes": lambda hand: xofakind(hand, kind=3),
        "threeofakind": lambda hand: xofakind(hand, kind=3),
        # "four": lambda hand: xofakind(hand, kind=4),
        # "fours": lambda hand: xofakind(hand, kind=4),
        "fourofakind": lambda hand: xofakind(hand, kind=4),
        "yahtzee": lambda hand: xofakind(hand, kind=5),
        # "full": fullhouse,
        "fullhouse": fullhouse,
        "chance": chance,
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
        output = "\n"
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
    hand = []
    for _ in range(num_of_dice):
        hand.append(randint(1,6))

    return hand

def valid_dice_choices(dice_to_roll=None):
    if not dice_to_roll:
        return False
    for x in dice_to_roll:
        try:
            int(x)
        except ValueError:
            return False
        if int(x) < 1 or int(x) > 5:
            return False
        if len(x) > 5:
            return False

    return True

def get_players(arg=None):
    while True:
        try:
            pinput = arg or input("How many players? ").strip()
            num_of_players = int(pinput)
            if num_of_players < 1 or num_of_players > 10:
                raise ValueError
        except ValueError:
            continue
        else:
            players = list()
            for x in range(0, num_of_players):
                # TODO: add question for player name
                players.append(Player(name=f"player{x}"))

            return players

def main():
    players = get_players()
    max_rounds = 13
    round = 0
    while round < max_rounds:
        for player in players:
            max_turns = 3
            turn = 0
            while turn < max_turns:
                if turn == 0:
                    dice_faces = roll_dice(5)
                    print(player.name, visualize_dice(dice_faces))
                else:
                    dice_choices=None
                    while not valid_dice_choices(dice_choices):
                        dice_choices = input("Input which dice to re-roll seperated by spaces: ").strip().split()
                    if not dice_choices:
                        print("Nothing to re-roll")
                        turn += 1
                        break
                    dice_to_roll = sorted([int(x) for x in dice_choices], reverse=True)
                    num_to_roll = len(dice_to_roll)
                    for dice in dice_to_roll:
                        dice_faces.pop(dice -1)
                    dice_faces.extend(roll_dice(num_to_roll))
                    print(visualize_dice(dice_faces))

                turn += 1

            if len(player.categories["upper"]) < 6 and len(player.categories["lower"]) < 7:
                while True:
                    section = input("Choose upper or lower section: ").strip().lower()
                    if section in ["upper", "lower"]:
                        break
            elif len(player.categories["upper"]) == 6:
                section = "lower"
                print("Chose section lower, since upper is used up")
            else:
                section = "upper"
                print("Chose section upper, since lower is used up")

            while True:
                print(f"Available categories in section {section}:\n{', '.join(CATEGORIES[section].keys())}")
                category = input("Choose scoring category: ").strip().lower()
                if category in CATEGORIES[section].keys():
                    player.categories[section].append(category)
                    break

            print(f"Final hand: {dice_faces}")

            if section == "upper":
                print(f"Score {section}/{category}: {upper_section_score(dice_faces, category)}")
                player.score += upper_section_score(dice_faces, category)
            else:
                print(f"Score {section}/{category}: {CATEGORIES['lower'][category](dice_faces)}")
                player.score += CATEGORIES['lower'][category](dice_faces)

            print(player.name, player.score)

        round += 1
if __name__ == "__main__":
    main()
