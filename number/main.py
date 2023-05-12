import src.functions as func
from art import tprint

is_game_over = False

tprint("Number Guessing Game")
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number_to_guess = func.get_random_number()
attempts_user = func.set_difficulty()

if attempts_user == 0:
    print("[Error] unknown difficulty")

while not is_game_over:
    print(f"You have {attempts_user} attempt(s) remaining to guess the number.")
    guess_by_user = int(input("Make a guess: "))
    is_game_over = func.compare_numbers(guess_by_user, number_to_guess, attempts_user)
    attempts_user -= 1
