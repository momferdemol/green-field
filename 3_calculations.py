import random
from art import tprint


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


