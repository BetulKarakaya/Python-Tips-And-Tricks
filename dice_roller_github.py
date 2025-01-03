import random

def roll_the_dice():
    """
    Simulates a dice roll and allows the user to roll as many times as they want.
    """
    print("🎲 Welcome to the Virtual Dice Roller!")
    print("Roll the dice and try your luck. Type 'q' to quit anytime.\n")

    while True:
        user_input = input("Press 'r' to roll the dice or 'q' to quit: ").strip().lower()
        if user_input == 'r':
            dice = random.randint(1, 6)  # Generate a random number between 1 and 6
            print(f"🎯 You rolled a {dice}!")
        elif user_input == 'q':
            print("🚪 Exiting the Virtual Dice Roller. Goodbye!")
            break
        else:
            print("❌ Invalid input! Please type 'r' to roll or 'q' to quit.")
def main():
    roll_the_dice()
if __name__ == "__main__":
    main()
