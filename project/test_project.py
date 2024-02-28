import random

import project

def test_roll_dice:
    random.seed(0)
    assert project.roll_dice(5) == [4, 4, 1, 3, 5]
