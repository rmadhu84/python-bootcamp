from art import logo
from os import system
system('clear')
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
last_index = len(alphabet) - 1
no_of_alphabets = len(alphabet)


def start():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text=text, shift=shift, direction=direction)


def caesar(text, shift, direction):
    output_string = ""
    global restart

    if direction == "decode":
        shift *= -1

    for ltr in text:
        if ltr in alphabet:
            new_position = (alphabet.index(ltr) + shift) % 26
            output_string += alphabet[new_position]
        else:
            output_string += ltr
    print(f"The {direction}d text is {output_string}")
    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")


start()
while restart == 'yes':
    start()

print("Goodbye!")
