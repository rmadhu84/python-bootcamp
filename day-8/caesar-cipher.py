alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift):
    encrypted_string = ""
    for ltr in plain_text:
        if ltr in alphabet:
            encrypted_string += alphabet[alphabet.index(ltr) + shift]
        else:
            encrypted_string += ltr
        # print(f"{ltr} => {alphabet[alphabet.index(ltr) + shift]}")
    print(f"The encoded text is {encrypted_string}!")


encrypt(plain_text=text, shift=shift)
