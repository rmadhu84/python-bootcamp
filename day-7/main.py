import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = ['_'] * len(chosen_word)
print(f"psst, chosen word is {chosen_word}")
lives = 6
win_or_loss = True
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    right_guess = False
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            right_guess = True

    if not right_guess:
        lives -= 1

    if lives == 0:
        win_or_loss = False
        end_of_game = True

    if "_" not in display:
        end_of_game = True

    print(stages[lives])
    print(f"{' '.join(display)}")
if  win_or_loss:
    print("You win!")
else:
    print("You lose!")



