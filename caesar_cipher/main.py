import src.functions as functions

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    functions.encrypt(text, shift)

elif direction == "decode":
    functions.decrypt(text, shift)
    
else:
    print("Please provide the correct command.")
