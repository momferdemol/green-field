

def treasure_island():
    # more complex if statements + I added a while loop
    print('''
        *******************************************************************************
                 |                   |                  |                     |
        _________|________________.=""_;=.______________|_____________________|_______
        |                   |  ,-"_,=""     `"=.|                  |
        |___________________|__"=._o`"-._        `"=.______________|___________________
                 |                `"=._o`"=._      _`"=._                     |
        _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
        |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
        |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                 |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
        _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
        |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
        |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
        ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
        /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
        ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
        /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
        ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
        /______/______/______/______/______/______/______/______/______/______/[TomekK]
        *******************************************************************************
    ''')

    print("Welcome to Treasure Island!")
    print("Your mission, should you choose to accept it, is to find the hidden treasure.\n")
    game_over = True

    while game_over == True:

        question_1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()

        if question_1 == "right":
            print("Ow shit.. Pirates on the road, you've been killed. Game Over.\n")
            try_again = input('Want to try again? Type "yes" or "no"\n')
            
            if try_again == "yes":
                game_over = True
            else:
                game_over = False

        elif question_1 == "left":
            question_2 = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()

            if question_2 == "swim":
                print("You've been eaten by a very big fish. Game Over.\n")
                try_again = input('Want to try again? Type "yes" or "no"\n')

                if try_again == "yes":
                    game_over = True
                else:
                    game_over = False

            elif question_2 == "wait":
                question_3 = input('You arrive at the island unharmed. There is a house with 3 doors. On red, one yellow, and one blue. Which color do you choose?\n').lower()

                if question_3 == "yellow":
                    print("Yes! You've found the hidden treasure. Good job!\n")
                    game_over = False

                elif question_3 == "red":
                    print("You step into the room, the door closes.. Fire all around you. Game Over.\n")
                    try_again = input('Want to try again? Type "yes" or "no"\n')

                    if try_again == "yes":
                        game_over = True
                    else:
                        game_over = False

                else:
                    print("You've been taken by alians.. sorry.. Game Over.\n")
                    try_again = input('Want to try again? Type "yes" or "no"\n')
                    
                    if try_again == "yes":
                        game_over = True
                    else:
                        game_over = False

            else:
                print("Input Error. No fun!")
                game_over = False

        else:
            print("Input Error. No fun!")
            game_over = False
