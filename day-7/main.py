import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = ['_'] * len(chosen_word)
print(f"psst, chosen word is {chosen_word}")
while "_" in display:
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(display)


