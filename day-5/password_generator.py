import random
#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letter_rand = []
number_rand = []
symbol_rand = []
password = []

for letter in range(1, nr_letters + 1):
    letter_rand.append(random.choice(letters));

for number in range(1, nr_numbers + 1):
    number_rand.append(random.choice(numbers))

for symbol in range(1, nr_symbols + 1):
    symbol_rand.append(random.choice(symbols))

password.extend(letter_rand)
password.extend(number_rand)
password.extend(symbol_rand)

print(password)

# password_rand = []
# for i in range(1, len(password)+1):
#     c = random.choice(password)
#     password_rand.append(c)

random.shuffle(password)

print(password)

generated_password = ""
for str in password:
    generated_password += str

print(generated_password)
