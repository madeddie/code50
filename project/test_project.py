import pytest
import random

import project

def test_roll_dice():
    random.seed(0)
    assert project.roll_dice(5) == [4, 4, 1, 3, 5]
    assert project.roll_dice(6) == [4, 4, 3, 4, 3, 5]

def test_visualize_dice():
    hand = [1, 2, 3]

    with pytest.raises(ValueError):
        project.visualize_dice(hand, style="unknown")

    assert project.visualize_dice(hand, style="unicode") == "⚀ ⚁ ⚂"
    assert project.visualize_dice(hand) == "\n---------------------\n|     ||o    ||o    |\n|  o  ||     ||  o  |\n|     ||    o||    o|\n---------------------\n   1      2      3   \n"

def test_upper_section_score():
    hand = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]
    with pytest.raises(ValueError):
        project.upper_section_score(hand, category="unknown")

    assert project.upper_section_score(hand, category="aces") == 1
    assert project.upper_section_score(hand, category="twos") == 4
    assert project.upper_section_score(hand, category="threes") == 9
    assert project.upper_section_score(hand, category="fives") == 20

def test_xofakind():
    hand = [1, 1, 1, 2, 3]
    assert project.xofakind(hand, 3) == 17
    assert project.xofakind(hand, 4) == 0
    hand = [1, 2, 2, 2, 2]
    assert project.xofakind(hand, 4) == 24
    hand = [1, 2, 3, 4, 5]
    assert project.xofakind(hand, 3) == 0
    hand = [1, 1, 1, 1, 1]
    assert project.xofakind(hand, 5) == 50

def test_fullhouse():
    assert project.fullhouse([1, 2, 3, 4, 5]) == 0
    assert project.fullhouse([2, 2, 3, 4, 5]) == 0
    assert project.fullhouse([1, 2, 3, 3, 3]) == 0
    assert project.fullhouse([2, 2, 3, 3, 3]) == 25

def test_straight():
    assert project.straight([1, 2, 3, 5]) == 0
    assert project.straight([1, 1, 2, 3]) == 0
    assert project.straight([1, 2, 3, 4]) == 30
    assert project.straight([2, 3, 4, 5]) == 30
    assert project.straight([3, 4, 5, 6]) == 30

    assert project.straight([1, 2, 3, 4, 4], kind="large") == 0
    assert project.straight([1, 1, 2, 3, 4], kind="large") == 0
    assert project.straight([1, 2, 3, 4, 5], kind="large") == 40
    assert project.straight([2, 3, 4, 5, 6], kind="large") == 40

def test_chance():
    assert project.chance([1, 1, 1, 1, 1]) == 5
    assert project.chance([1, 2, 3, 4, 5]) == 15

def test_valid_dice_choices():
    assert project.valid_dice_choices() == False
    assert project.valid_dice_choices("") == True
    assert project.valid_dice_choices("cat") == False
    assert project.valid_dice_choices("0 1 2") == False
    assert project.valid_dice_choices("1 2 3 4 5 6") == False
    assert project.valid_dice_choices("2 3 4") == True
