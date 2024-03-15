# Yahtzee
#### Video Demo: https://youtu.be/bRf7KdcRdFI
#### Description:
This is an implementation of the game of Yahtzee (Trademark of HASBRO, INC).

While creating a Scratch app for CS50x I had the idea to implement a game of Yahtzee. It proved a bit too difficult to implement the whole game in a few days in scratch, mostly because of the weird way global variables work.
My Scratch project was down-scoped to a dice rolling simulator with a hold function. The logic I had already researched and written out I then used to implement fully in Python for CS50p.

#### How to play
You run the game with `python project.py`.

The first step is to choose the amount of players, with an obvious minimum of 1 and a maximum of 10. After that there will be 13 rounds where each player can decide to roll their dice up to three times, with the option to hold some of the dice as not to roll them. After the three rolls (or less if the player chooses so) the player can choose in which category they would like to score their "hand".

#### Scoring
There are 13 categories divided over 2 sections. Every category can only be used once

* Upper section scoring is by adding all the dice of the same face together
    - aces: add all the ones together
    - twos: add all twos
    - threes
    - fours
    - fives
    - sixes

* Lower Section

    - Three Of A Kind: at least three dice the same, score: sum of all dice
    - Four Of A Kind: at least four dice the same, score: sum of all dice
    - Full House: three of one number and two of another, score: 25
    - Small Straight: four sequential dice (1-2-3-4, 2-3-4-5, or 3-4-5-6), score: 30
    - Large Straight: five sequential dice (1-2-3-4-5 or 2-3-4-5-6), score: 40
    - Yahtzee: all five dice the same, score: 50
    - Chance: ny combination, sum of all dice

For more information on the rules, see https://en.wikipedia.org/wiki/Yahtzee#Rules
