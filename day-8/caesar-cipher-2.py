alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
last_index = len(alphabet) - 1
no_of_alphabets = len(alphabet)


def caesar(text, shift, direction):
    output_string = ""
    for ltr in text:
        if ltr in alphabet:
            if direction == "encode":
                new_position = alphabet.index(ltr) + shift
                if new_position > last_index:
                    new_position = new_position - no_of_alphabets
                # print(f"{ltr} => {alphabet[new_position]}")
                output_string += alphabet[new_position]
            if direction == "decode":
                new_position = alphabet.index(ltr) - shift
                # print(f"{ltr} => {alphabet[new_position]}")
                output_string += alphabet[new_position]
        else:
            output_string += ltr
    print(f"The {direction}d text is {output_string}")


caesar(text=text, shift=shift, direction=direction)
