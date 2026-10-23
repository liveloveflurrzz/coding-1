
import random

def dice_rolling_game():
    score = 0

    while True:
        choice = input("Enter 'r' to roll or 'q' to quit: ").lower()

        if choice == "q":
            print("Thanks for playing!")
            print("Final score:", score)
            break

        elif choice == "r":
            roll = random.randint(1, 7)
            print("You rolled:", roll)

            if roll == 7:
                score += 10
                print("You win! You earned 10 points.")
            else:
                score -= 5
                print("You lose! You lost 5 points.")

            print("Current score:", score)

        else:
            print("Invalid choice. Please enter 'r' or 'q'.")

# Start the game
dice_rolling_game()
