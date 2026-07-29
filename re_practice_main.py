import re
import random
from functools import total_ordering

# Messing around with re to figure out how to add up dice for a ttrpg

text = "/1d20 + 1d1"

# Cleaning up user entry
text_cleaned = text.replace(" ", "").lower()
# print(text_cleaned)

# re goodness
# The \d? means it looks for 0 to 1 digit
# This just looks for the dice parts. Successfully ignores 'xd4'
# added an "optional" [+-] in front so I can get the operands in too
pattern_dice = re.compile(r'[+-]?\dd\d\d?')
matches_dice = pattern_dice.findall(text_cleaned)
print(matches_dice)

# # this looks for the operands.  They can only be '+' or '-'
# pattern_operands = re.compile(r'[+-]')
# matches_operands = pattern_operands.findall(text_cleaned)
# print(matches_operands)

def calculate_dice_roll(rolled: str) -> int:
    final = 0
    dices = int(rolled.split("d")[0])
    faces = int(rolled.split("d")[1])

    for i in range(dices):
        final += random.randint(1, faces)

    return final

# Calculates the final score
final_roll: int = 0

for roll in matches_dice:
    if roll[0] != "-" and roll[0] != "+":
        final_roll += calculate_dice_roll(roll)
    else:
        operation = roll[0]
        roll = roll.split(operation)[1]

        if operation == "-":
            final_roll -= calculate_dice_roll(roll)
        else:
            final_roll += calculate_dice_roll(roll)

print(final_roll)
