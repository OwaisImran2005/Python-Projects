
import random

SIDES = 6

def roll_dice():
   
    dice1: int = random.randint(1, SIDES)
    dice2: int = random.randint(1, SIDES)
    print("Dice 1 : ", dice1)
    print("Dice 2 : ", dice2)

def main():

    print("\nRoll 1")
    roll_dice()
    print("\nRoll 2")
    roll_dice()
    print("\nRoll 3")
    roll_dice()
   
if __name__ == '__main__':
    main()

