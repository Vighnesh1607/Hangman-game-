import random

# List of words for the game
word_list = ["apple", "banana", "orange", "strawberry", "kiwi"]

def choose_word(word_list):
    """Randomly selects a word from the word_list."""
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """Displays the current state of the word with guessed letters filled in."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def draw_hangman(incorrect_guesses):
    """Displays ASCII art for the hangman based on the number of incorrect guesses."""
    stages = [ 
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[incorrect_guesses]

def hangman_game():
    """Main function to run the Hangman game."""
    print("Welcome to Hangman!")
    
    word = choose_word(word_list)
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6
    
    while incorrect_guesses < max_attempts:
        # Display current state of the word
        print(display_word(word, guessed_letters))
        
        # Ask player for a guess
        guess = input("Guess a letter: ").lower()
        
        # Validate the guess
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)
        
        # Check if the guessed letter is in the word
        if guess in word:
            print("Correct guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            print("Incorrect guess!")
            incorrect_guesses += 1
            print(draw_hangman(incorrect_guesses))
    
    if incorrect_guesses >= max_attempts:
        print(f"Sorry, you ran out of attempts! The word was: {word}")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman_game()
    else:
        print("Thank you for playing!")

# Run the game
hangman_game()
