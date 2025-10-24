import random

# Hangman stages ASCII art
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
=========
''', '''
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

# Word list
words = ["apple", "beautiful", "potato", "python", "hangman", "computer", "programming", 
         "developer", "keyboard", "monitor", "internet", "software", "hardware", "algorithm",
         "function", "variable", "database", "network", "security", "encryption"]

# Game setup
lives = 6
chosen_word = random.choice(words)
print(f"Hint: The word has {len(chosen_word)} letters")

display = []
for i in range(len(chosen_word)):
    display += '_'

print(display)

game_over = False

# Main game loop
while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    
    # Check if letter already guessed
    if guessed_letter in display:
        print(f"You've already guessed '{guessed_letter}'")
        continue
    
    # Check each position in the chosen word
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    
    print(display)
    
    # Check if guessed letter is not in the word
    if guessed_letter not in chosen_word:
        print(f"'{guessed_letter}' is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"You lose!! The word was '{chosen_word}'")
    
    # Check if player has won
    if '_' not in display:
        game_over = True
        print("You win !!")
    
    # Display hangman stage
    print(stages[lives])
