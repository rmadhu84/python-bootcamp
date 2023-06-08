import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

for c in chosen_word:
    if(c == guess):
        print(c)
    else:
        print("_")
