import src.functions as functions
from art import tprint

tprint("caesar cipher")
end_program = False

while not end_program:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    if (direction == "encode") or (direction == "decode"):
        functions.cipher(text, shift, direction)
    else:
        print("Please provide the correct command.")

    run_program = input("Type 'yes' to go again, or 'no' to stop the program.\n")

    if run_program == "no":
        end_program = True
        print("thank you, come again!")
