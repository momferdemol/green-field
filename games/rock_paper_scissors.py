import random


def rock_paper_scissors():

    options = ["Rock", "Paper", "Scissors"]
    user_choice = int(input("What do you choose? Type 1 for Rock, 2 for Paper, or 3 for Scissors.\n"))
    
    if user_choice < 1 or user_choice > 3:
        print("\nWrong input. You suck!\n")
    else:
        print(f"\nYou\'ve chosen {options[user_choice - 1]}\n")
        print("Computer chose...\n")
        computer_choice = random.randint(1, 3)
        print(f"Computer has chosen {options[computer_choice - 1]}\n")

        # Rock wins against scissors
        # Scissors win against paper
        # Paper wins against rock
        if user_choice == 1 and computer_choice == 3:
            print("You win!\n")
        elif user_choice == 3 and computer_choice == 2:
            print("You win!\n")
        elif user_choice == 2 and computer_choice == 1:
            print("You win!\n")
        elif user_choice == computer_choice:
            print("Let\'s try again.\n")
        else:
            print("You lose.\n")