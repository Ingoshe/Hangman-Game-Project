import random #computer choice of words

# List of words used for the game
word_list = ['python', 'javascript', 'ruby', 'csharp', 'java', 'swift', 'kotlin','styling']

# Choose random word from the provided list of words (word_list)
chosen_word = random.choice(word_list)

# Create undescores to represent the letters of the chosen word keeping in mind the number of letters
guesses = ['_'] * len(chosen_word)

# Setting the maximum number of incorrect guesses allowed
max_no_incorrect_guesses = 6

# Keep track of the number of incorrect guesses
incorrect_guesses = 0

# Keep track of already guessed letters
guessed_letters = []

# Game loop
while True:
    # Show current game state
    print(' '.join(guesses))
    print(f'Incorrect guesses: {incorrect_guesses}/{max_no_incorrect_guesses}')
    print(f'Letters guessed: {", ".join(guessed_letters)}')

    # Ask user for input letter
    guess = input('Guess a letter: ').lower()

    # Validating the guess
    if len(guess) != 1 or not guess.isalpha():
        print('Please enter a single letter.')
        continue
    if guess in guessed_letters:
        print('You already guessed that letter. Try again.')
        continue

    # Update list of guesses
    guessed_letters.append(guess)

    # Check if the guess is in the chosen word
    if guess in chosen_word:
        # Update the guesses list with the correctly guessed letters
        for l in range(len(chosen_word)):
            if chosen_word[l] == guess:
                guesses[l] = guess
    else:
        # Increment the number of incorrect guesses after every incorrect guess
        incorrect_guesses += 1

    # THE END/check whether the game is over
    if incorrect_guesses >= max_no_incorrect_guesses:
        print(f'You lost! The word was {chosen_word}.')
        break
    if '_' not in guesses:
        print(f'You won! The word was {chosen_word}.')
        break
