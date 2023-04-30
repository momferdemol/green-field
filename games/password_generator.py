import random
from art import tprint


def password_generator():

    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','#','$','%','&','(',')','*','+']

    tprint("password generator")
    print("Welcome to the password generator!")
    
    # ask for input from user
    number_for_length = int(input("What should be the length of your password? e.g. 12, 14, 20\n"))
    number_of_numbers = int(input("How many numbers do you want to include?\n"))
    number_of_symbols = int(input("How many symbols do you want to include?\n"))
    
    # subtracks numbers and symbols for total password digits
    number_for_length -= number_of_numbers + number_of_symbols

    # generate lists with random letters, numbers, and symbols
    list_of_letters = random.choices(letters, k=number_for_length)
    list_of_numbers = random.choices(numbers, k=number_of_numbers)
    list_of_symbols = random.choices(symbols, k=number_of_symbols) 
    
    # combine separate lists together
    password_list = list_of_letters + list_of_numbers + list_of_symbols

    # shuffle all characters in the list
    random.shuffle(password_list)

    # set empty string and loop through list to make one string value
    password = ""
    for item in password_list:
        password += item
    
    print(password)