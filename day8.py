## Ceasar Cyper Project
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print('''
,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
''')


## Encrypt function

# def encrypt(plain_text, shift_amount):
#     cipher_text=''
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position+shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f'The encoded text is {cipher_text}')
#
#
# ## decrpting
#
# def decrypt(plain_text, shift_amount):
#     cipher_text=''
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position-shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f'The decoded text is {cipher_text}')
#
# if direction=='encode':
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == 'decode':
#     decrypt(plain_text=text, shift_amount=shift)




def caesar(plain_text, shift_amount):
    if direction == 'encode':
        cipher_text = ''
        for char in plain_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            else:
                cipher_text += char
        print(f'The encoded text is {cipher_text}')
    elif direction == 'decode':
        cipher_text = ''
        for char in plain_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position - shift_amount
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            else:
                cipher_text += char
        print(f'The decoded text is {cipher_text}')

print("Welcome to Caesar's Cypher 🕵️ ")
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(plain_text=text,shift_amount=shift)
    user_input = input("Do you want to continue, yes or no?: ")
    if user_input == 'no':
        should_continue = False
        print('Goodbye!👋')

