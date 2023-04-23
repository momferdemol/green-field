
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

# length_user_input()
# switch_variables()
# hello_world()
# split_and_add_number()
body_mass_index()
