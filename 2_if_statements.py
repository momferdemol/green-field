import random
from art import tprint


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


def heads_or_tails():
    # how to get a random number
    number = random.randint(1, 2)

    if number == 1:
        print("Coin flip... heads.")
    else:
        print("Coin flip.. tails.")
