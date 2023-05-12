import random


def get_random_number():
    """This function used the random package
    to return a random number between 1 and 100."""
    return random.randint(1, 100)


def set_difficulty():
    """This function asked the user to choose a difficulty level
    and returns 10 attempts for 'easy' or 5 attempts for 'hard'."""
    result = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if result == "hard":
        return 5
    elif result == "easy":
        return 10
    else:
        return 0


def compare_numbers(guess_by_user, number_to_guess, attempts_user):
    """This function takes the numbers and remaining attempts, compares the numbers,
    and returns if the game is over with true or false."""
    if guess_by_user == number_to_guess:
        print("You've guessed the correct number! 😀\n")
        return True
    elif guess_by_user > number_to_guess:
        print("Too high.\n")
    elif guess_by_user < number_to_guess:
        print("Too low.\n")

    if attempts_user > 1:
        return False
    else:
        print("You've lost 😩\n")
        print(f"The correct number is: {number_to_guess}\n")
        return True
