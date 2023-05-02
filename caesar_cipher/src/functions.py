
alphabet = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#------------------------
# encrypt
#------------------------
# # input is 'hello'
# shift is 5
# output is 'mjqqt'

#------------------------
# decrypt
#------------------------
# input is 'mjqqt'
# shift is 5
# output is 'hello'

def cipher(text, shift, direction):

    new_text = ""

    if direction == "decode":
            shift *= -1

    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift 
            new_text += alphabet[new_position]
        else:
            new_text += char

    print(f"The {direction}d text is: {new_text}")
