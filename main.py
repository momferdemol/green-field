import random
from art import tprint


def length_user_input():
    # how many characters in the user input
    user_name = input("What is your name?\n")
    input_length = len(user_name)
    print(f"Hi {user_name}, your name consist of {input_length} characters.\n")


def switch_variables():
    # play around with variables, switch values
    a = input("a: ")
    b = input("b: ")

    c = a
    a = b
    b = c

    print("a = " + a)
    print("b = " + b)


def hello_world():
    # simple 'hello word' loop
    word = "Hello world"
    length = len(word)
    position = 0

    while position < length:
        print(word[position])
        position += 1


def split_and_add_number():
    # how to work with positions
    number = input("hi there! Give me a two digit number please.\n")
    num_1 = number[0]
    num_2 = number[1]

    calculation = int(num_1) + int(num_2)

    print(f"That will be {calculation}\n")


def body_mass_index():
    # BMI calculation
    height = float(input("Enter your height in m: "))
    weight = float(input("Enter your weight in kg: "))

    body_mass_index = round(weight / height ** 2)

    print(f"Your body mass index is {body_mass_index}")


def what_is_left():
    # another calculation
    age = input("What is your current age? ")

    year_left = 90 - int(age)
    months = year_left * 12
    weeks = year_left * 52
    days = year_left * 365

    print(f"You have {days} days, {weeks} weeks, and {months} months left.")


def split_and_tip_calculator():
    # input some values, calculate, and print
    tprint("tip calculator")
    print("\nWelcome to the tip calculator.\n")
    bill = float(input("What was the total bill? "))
    percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
    split = int(input("How may people to split the bill? "))

    tip = percentage / 100 * bill
    bill_with_tip = bill + tip
    result_per_person = round(bill_with_tip / split, 2)

    message = f"Each person should pay: ${'{:.2f}'.format(result_per_person)}\n"
    print(message)


def odd_or_event():
    # is this an odd or even number
    number = int(input("Which number do you want to check? "))
    check = number % 2

    if check == 1:
        print("This is an odd number.\n")
    else:
        print("This is an even number.\n")


def body_mass_index_2():
    # BMI calculation with additional feedback
    height = float(input("Enter your height in m: "))
    weight = float(input("Enter your weight in kg: "))

    body_mass_index = round(weight / height ** 2)

    if body_mass_index < 18.5:
        print(f"\nYour body mass index is {body_mass_index}")
        print("You are underwight. Go and eat something!\n")
    elif body_mass_index < 25:
        print(f"\nYour body mass index is {body_mass_index}")
        print("You have a normal weight. Awesome\n")
    elif body_mass_index < 30:
        print(f"\nYour body mass index is {body_mass_index}")
        print("You are overweight. Stop eating those chips!\n")
    elif body_mass_index < 35:
        print(f"\nYour body mass index is {body_mass_index}")
        print("You are obese! You should think about your health.\n")
    else:
        print(f"\nYour body mass index is {body_mass_index}")
        print("You are clinically obese. Game over.\n")


def pizza_order():
    # more if statements
    tprint("python pizza")
    size = input("What size pizza do you want? S, M, L: ").upper()
    add_pepperoni = input("Do you want pepperoni? Y or N: ").upper()
    extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
    bill = 0

    if size == "S":
        bill = 15
    elif size == "M":
        bill = 20
    else:
        bill = 25
    
    if add_pepperoni == "Y":
        if size == "S":
            bill += 2
        else:
            bill += 3

    if extra_cheese == "Y":
        bill += 1

    print(f"\nYour final bill is: {bill}.\n")


def school_girl_love_calculator():

    tprint("love calculator")
    name1 = input("What is your name?\n")
    name2 = input("What is their name?\n")

    combine_name = (name1 + name2).lower()

    # TRUE letter count
    count_t = combine_name.count("t")
    count_r = combine_name.count("r")
    count_u = combine_name.count("u")
    count_e = combine_name.count("e")
    true = count_t + count_r + count_u + count_e

    # LOVE letter count
    count_l = combine_name.count("l")
    count_o = combine_name.count("o")
    count_v = combine_name.count("v")
    count_e = combine_name.count("e")
    love = count_l + count_o + count_v + count_e

    # Add together as string value (e.g. TRUE=5 and LOVE=3 => score=53)
    score = int(str(true) + str(love))

    if score < 10 or score >90:
        print(f"\nYour score is {score}, you go together like coke and mentos.\n")
    elif score >= 40 and score <= 50:
        print(f"\nYour score is {score}, you are alright together.\n")
    else:
        print(f"\nYour score is {score}.\n")


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


def heads_or_tails():
    # how to get a random number
    number = random.randint(1, 2)

    if number == 1:
        print("Coin flip... heads.")
    else:
        print("Coin flip.. tails.")


def who_pays_bill():
    # how to play around with random numbers
    string_of_names = input("\nWho is playing? Type in the names separated by a comma.\n")
    names = string_of_names.split(",")

    count = len(names) - 1
    payer = random.randint(0, count)

    print(f"\n{names[payer]} is going to pay the bill today! Thank you, come again!\n")

    # OR use another random function
    payer = random.choice(names)
    print(f"\n{payer} is going to pay the bill today! Thank you, come again!\n")


def play_with_lists():
    # create a matrix of lists and ask for which position in the matrix the value needs to change.
    row1 = ["X","X","X"]
    row2 = ["X","X","X"]
    row3 = ["X","X","X"]

    matrix = [row1, row2, row3]

    print(f"\n{row1}\n{row2}\n{row3}\n")

    position = input('Where do you want to place your mark? Specify column and row like "31" or "23" ')

    column = int(position[0]) - 1
    row = int(position[1]) - 1

    matrix[row][column] = "M"

    print(f"\n{row1}\n{row2}\n{row3}\n")


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

###############
#### LOOPS ####
###############

# for item in list_of_items:
#   do something for each item

def average_height():

    student_heigths = input("Input a list of student heights, separated by a space.\n").split()
    heights_total = 0

    for height in range(0, len(student_heigths)):
        student_heigths[height] = int(student_heigths[height])
        heights_total += student_heigths[height]

    heights_average = round(heights_total / (height + 1))
    print(f"\nYour input: {student_heigths}\n")
    print(f"The average height is: {heights_average}\n")


# length_user_input()
# switch_variables()
# hello_world()
# split_and_add_number()
# body_mass_index()
# what_is_left()
# split_and_tip_calculator()
# odd_or_event()
# body_mass_index_2()
# pizza_order()
# school_girl_love_calculator()
# treasure_island()
# heads_or_tails()
# who_pays_bill()
# play_with_lists()
# rock_paper_scissors()
# average_height()
