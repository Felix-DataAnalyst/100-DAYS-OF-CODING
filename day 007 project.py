# PROJECT FOR DAY SIX - HANGMAN game
import random
from hangman_word import word_list
from hangman_art import logo, stages
#from hangman_art import stages

# Start of game
print(logo)

# Step 1
# Step 2
# Step 3
# Step 4
# Step 5
# (1a) Randomly choose a word from the wordlist and assign a variable.
# (4a) Create a variable called lives to keep track of the users lives. Set lives to equal 6.

chosen_word = random.choice(word_list)
#print(chosen_word)
lives = 6

# (2a) Create a placeholder with the same number of blanks as the chosen_word.
length_chosen = len(chosen_word)
placeholder = ""
for position in range(length_chosen):
    placeholder += "_"
print(f"Word to Guess: {placeholder}\nWord Length: {length_chosen}")

# (1b) Ask the user to guess a letter and assign a variable
# (3a) Use a loop to let the user guess again
# (5a) If the user has entered a letter they've already guessed, print the letter and let them know
game_over = False
correct_guess = []
while not game_over:
    print(f"************************************************* {lives}/6 LIVES LEFT *************************************************")
    guess = input("Guess A Letter: ").lower()
    if guess in correct_guess:
        print(f"You've already guessed {guess}")

    # (1c) Check if the letter the user guessed is one of the letters in the chosen_word. Print Right or Wrong
    # (2b) Create a display that puts the guessed letter in the right positions and "_" in the rest of the string.
    # (3b) Change the loop so that you keep the previous correct guess and the new guess.
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guess.append(letter)
        elif letter in correct_guess:
            display += letter
        else:
            display += "_"
    print(display)

# (5b) f the letter is not in the chosen_word, print out the letter and let them know they loose a life.
    # e.g. You guessed d, that's not in the word. you lose a life.
# (4b) If guess is not a letter in the chosen_word, then reduce lives by 1. If lives goes down to 0 then the game
    # should stop and print "You Loose"
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. you lose a life.")
        if lives == 0:
            game_over = True
            print(f"********************* It was {chosen_word} *********************\n********************* Game Over!!! *********************\n********************* You Loose *********************")

    if "_" not in display:
        game_over = True
        print("********************* CONGRATULATIONS *********************\n********************* You Win *********************")
# (4c) Print the ASCII art from stages that corresponds to the current number of lives the user has remaining
    print(stages[lives])
