gitprint('''

╔═══╗                         ╔═══╗      ╔╗         
║╔═╗║                         ║╔═╗║      ║║         
║║ ╚╝╔══╗ ╔══╗╔══╗╔══╗ ╔═╗    ║║ ╚╝╔╗╔══╗║╚═╗╔══╗╔═╗
║║ ╔╗╚ ╗║ ║╔╗║║══╣╚ ╗║ ║╔╝    ║║ ╔╗╠╣║╔╗║║╔╗║║╔╗║║╔╝
║╚═╝║║╚╝╚╗║║═╣╠══║║╚╝╚╗║║     ║╚═╝║║║║╚╝║║║║║║║═╣║║ 
╚═══╝╚═══╝╚══╝╚══╝╚═══╝╚╝     ╚═══╝╚╝║╔═╝╚╝╚╝╚══╝╚╝ 
                                     ║║             
                                     ╚╝             ''')


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    new_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        new_text += new_letter
    print(f"The encoded text is: '{new_text}'")

def decrypt(text, shift):
    actual_text = ""
    for letter in text:
        position = alphabet.index(letter)
        actual_position = position - shift
        actual_letter = alphabet[actual_position]
        actual_text -= actual_letter
    print(f"The decoded text is: '{actual_text}'")



if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Invalid Direction !!!")
    
