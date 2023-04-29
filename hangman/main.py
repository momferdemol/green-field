import random
from art import tprint

stages = ['''
    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
===========
''', '''
    +---+
    |   |
    0   |
   /|\  |
   /    |
        |
===========
''', '''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
===========
''', '''
    +---+
    |   |
    0   |
   /|   |
        |
        |
===========
''', '''
    +---+
    |   |
    0   |
   /    |
        |
        |
===========
''', '''
    +---+
    |   |
    0   |
        |
        |
        |
===========
''', '''
    +---+
    |   |
        |
        |
        |
        |
===========
''']

end_of_game = False
lives = 6
display = []
previous_guess = ""

# ASCII banner ;-)
tprint("hangman")

# choose a word from a list of words to play the game
word_list = ["computer", "harddisk", "keyboard", "mouse"]
chosen_word = random.choice(word_list).lower()
word_length = len(chosen_word)

print(f"DEBUG: {chosen_word}")

# create a game display by adding "_" for each letter in the chosen word
for _ in range(word_length):
    display += "_"

while not end_of_game:

    # ask the user to guess a letter
    guess = input("Guess a letter: ")

    # keep track of previous guesses
    if guess in previous_guess:
        print("\nYou\'ve used this letter already.\n")

    previous_guess += guess

    # check if the letter is in the chosen word and update the game display
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    # check if need to take 1 life and if lives is 0 end the game
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("Game Over\n")

    # print game status
    print(stages[lives])

    # print game display
    print(f"{' '.join(display)}\n")

    # check if user can continue to guess
    if "_" not in display:
        end_of_game = True
        print("You win!\n")

