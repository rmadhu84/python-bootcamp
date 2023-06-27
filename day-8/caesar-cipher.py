alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
last_index = len(alphabet) - 1
no_of_alphabets = len(alphabet)


def encrypt(plain_text, shift):
    encrypted_string = ""
    for ltr in plain_text:
        if ltr in alphabet:
            new_position = alphabet.index(ltr) + shift
            if new_position > last_index:
                new_position = new_position - no_of_alphabets
            # print(f"{ltr} => {alphabet[new_position]}")
            encrypted_string += alphabet[new_position]
        else:
            encrypted_string += ltr
        # print(f"{ltr} => {alphabet[alphabet.index(ltr) + shift]}")
    print(f"The encoded text is {encrypted_string}!")


encrypt(plain_text=text, shift=shift)
