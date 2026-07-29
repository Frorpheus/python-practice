import re

# Messing around with re to figure out how to add up dice for a ttrpg

text = "2D20 + 3d6 - xd4"

# Cleaning up user entry
text_cleaned = text.replace(" ", "").lower()
# print(text_cleaned)

# re goodness
# The \d? means it looks for 0 to 1 digit
# This just looks for the dice parts. Successfully ignores 'xd4'
pattern_dice = re.compile(r'\dd\d\d?')
matches_dice = pattern_dice.findall(text_cleaned)
print(matches_dice)

# this looks for the operands.  They can only be '+' or '-'
pattern_operands = re.compile(r'[+-]')
matches_operands = pattern_operands.findall(text_cleaned)
print(matches_operands)
