
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(text, shift):

    # example
    # input is 'hello'
    # shift is 5
    # output is 'mjqqt'

    new_text = ""
    
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        new_text += new_letter

    print(new_text)


def decrypt(text, shift):

    # example
    # input is 'mjqqt'
    # shift is 5
    # output is 'hello'

    new_text = ""
    
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        new_letter = alphabet[new_position]
        new_text += new_letter

    print(new_text)
