import random

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("\nRolling the dices...")
    print("The values are....")
    print(random.randint(1, 6))

    roll_again = input("Roll the dices again? (y/n) ")
