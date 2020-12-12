"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"

die_values = [ONES, TWOS, THREES, FOURS, FIVES, SIXES]

def sum_dice(dice, die):
    return [sum(x) for x in dice if x == die]


def score(dice, category):
    score = 0
    unique = list(set(dice))
    if category == YACHT: 
        if len(unique) == 1 : score = 50
    elif category in die_values:
        die_value = die_values.index(category) + 1
        score = dice.count(die_value) * die_value
    elif category == FULL_HOUSE:
        if len(unique) == 2:
            if sorted([dice.count(die) for die in unique]) == [2,3]:
                score = sum(dice)
    elif category == FOUR_OF_A_KIND:
        if len(unique) <= 2:
            for die in unique:
                if dice.count(die) >= 4:
                    score = die * 4
    elif category == LITTLE_STRAIGHT:
        if sorted(dice) == [1,2,3,4,5]:
            score = 30
    elif category == BIG_STRAIGHT:
        if sorted(dice) == [2,3,4,5,6]:
            score = 30
    elif category == CHOICE:
        score = sum(dice)
    return score
        

    
    
    
    
    
    
        
