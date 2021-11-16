import math
import random

print("Welcome to my number game!")
input("Press Enter to continue...")
print("You will be assigned a team 1 or 2.")
print("team 1 wins if the rng outputs a number greater than 50, while team 2 wins if it outputs a number less than 50.")
input("Press Enter to continue...")
team=random.randrange(1,2)
exclamation=("!")
print("Aaaannnddd.. your team is... Drumroll please...")
input("Press Enter to continue...")
print(team,exclamation)
print("congratulations, player 1! Player two, that means your team is the other one!")
input("Press Enter to continue...")

x = random.randrange(1,100)
print(x)
if x>50:
    print("The output number was greater than 50!")
else:
    print("The output number was less than 50!")
input("Press Enter to continue...")

print("Now you know who won!")
print("Thanks for playing my simple game!")
