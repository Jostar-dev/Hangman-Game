import random

def choose_word():
    """Function to choose a word from a predefined list"""
    word_list = ["apple", "banana", "orange", "strawberry", "grape", "watermelon", "pineapple"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    """Function to display the word with guessed letters filled in"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    """Function to run the Hangman game"""
    print("Welcome to Hangman!")
    secret_word = choose_word()
    guessed = False
    guessed_letters = []
    attempts = 6

    print("The word contains", len(secret_word), "letters.")

    while not guessed and attempts > 0:
        print("You have", attempts, "attempts left.")
        print(display_word(secret_word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter.")
            elif guess in secret_word:
                print("Good guess!")
                guessed_letters.append(guess)
                if display_word(secret_word, guessed_letters) == secret_word:
                    guessed = True
            else:
                print("Sorry, that letter is not in the word.")
                attempts -= 1
            print()
        else:
            print("Invalid guess. Please enter a single letter.")

    if guessed:
        print("Congratulations! You guessed the word:", secret_word)
    else:
        print("Sorry, you ran out of attempts. The word was:", secret_word)

hangman()
