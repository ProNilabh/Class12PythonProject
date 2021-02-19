#Write a Random Number Generator that Generates Random Numbers between 1 and 6 (Simulates a Dice)

import random

def roll():    
    s=random.randint(1,6)
    return s

xD= str(input("Enter R to Roll the Dice!-"))

if xD=="r":
    print(roll())
else:
    print("Thanks for Using the Program!")