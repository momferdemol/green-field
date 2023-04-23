
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


# length_user_input()
# switch_variables()
# hello_world()
