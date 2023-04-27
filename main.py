from art import tprint

def length_user_input():

    user_name = input("What is your name?\n")
    input_length = len(user_name)
    print(f"Hi {user_name}, your name consist of {input_length} characters.\n")


def switch_variables():

    a = input("a: ")
    b = input("b: ")

    c = a
    a = b
    b = c

    print("a = " + a)
    print("b = " + b)


def hello_world():

    word = "Hello world"
    length = len(word)
    position = 0

    while position < length:
        print(word[position])
        position += 1


def split_and_add_number():

    number = input("hi there! Give me a two digit number please.\n")
    num_1 = number[0]
    num_2 = number[1]

    calculation = int(num_1) + int(num_2)

    print(f"That will be {calculation}\n")


def body_mass_index():

    height = float(input("Enter your height in m: "))
    weight = float(input("Enter your weight in kg: "))

    body_mass_index = round(weight / height ** 2)

    print(f"Your body mass index is {body_mass_index}")


def what_is_left():

    age = input("What is your current age? ")

    year_left = 90 - int(age)
    months = year_left * 12
    weeks = year_left * 52
    days = year_left * 365

    print(f"You have {days} days, {weeks} weeks, and {months} months left.")


def split_and_tip_calculator():

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

    number = int(input("Which number do you want to check? "))
    check = number % 2

    if check == 1:
        print("This is an odd number.\n")
    else:
        print("This is an even number.\n")


def body_mass_index_2():

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
school_girl_love_calculator()
