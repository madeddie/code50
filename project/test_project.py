import random

import project

def test_roll_dice():
    random.seed(0)
    assert project.roll_dice(5) == [4, 4, 1, 3, 5]
    assert project.roll_dice(6) == [4, 4, 3, 4, 3, 5]

def test_visualize_dice():
    hand = [1, 2, 3, 4, 5]
    assert project.visualize_dice(hand, style="unicode") == "⚀ ⚁ ⚂ ⚃ ⚄"
    assert project.visualize_dice(hand) == ""
