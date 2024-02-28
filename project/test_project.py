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
    assert project.visualize_dice(hand) == "---------------------\n|     ||o    ||o    |\n|  o  ||     ||  o  |\n|     ||    o||    o|\n---------------------\n   1      2      3   \n"

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
    assert project.xofakind(hand, 3) == True
    assert project.xofakind(hand, 4) == False
    hand = [1, 2, 2, 2, 2]
    assert project.xofakind(hand, 4) == True
    hand = [1, 2, 3, 4, 5]
    assert project.xofakind(hand, 3) == False
