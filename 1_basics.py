
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


def split_and_add_number():
    # how to work with positions
    number = input("hi there! Give me a two digit number please.\n")
    num_1 = number[0]
    num_2 = number[1]

    calculation = int(num_1) + int(num_2)

    print(f"That will be {calculation}\n")

#----------------------------------------------------
# LISTS
#----------------------------------------------------

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

#----------------------------------------------------
# FUNCTIONS
#----------------------------------------------------
#
# parameter variable = 123 (value you 'give' the function)
# 
# def my_function(parameter_1, parameter_2):
#   do something
#   do something & use 'given' value
#
#   The value 123 is called an argument

#----------------------------------------------------
# DICTIONARY (+ NESTED)
#----------------------------------------------------
# The travel log is a List
# Each item in the list is a dictionary
# and 1 key 'cities_visited' within the dictionary has a list value
travel_log = [
{
    "country": "France",
    "total_visits": 12,
    "cities_visited": ["Paris", "Lille", "Dijon"]
},
{
    "country": "Germany",
    "total_visits": 5,
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
}
]
