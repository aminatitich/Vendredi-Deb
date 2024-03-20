import random

def hangman():
    words = ["apple", "banana", "orange", "strawberry", "watermelon", "pineapple", "blueberry", "kiwi"]
    secret_word = random.choice(words)
    guessed_word = ['_'] * len(secret_word)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(" ".join(guessed_word))

    while '_' in guessed_word and attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed that letter.")
            elif guess in secret_word:
                print("Good guess!")
                for i in range(len(secret_word)):
                    if secret_word[i] == guess:
                        guessed_word[i] = guess
            else:
                attempts -= 1
                print(f"Sorry, {guess} is not in the word. You have {attempts} attempts left.")
            guessed_letters.append(guess)
            print(" ".join(guessed_word))
        else:
            print("Please enter a single letter.")

    if '_' not in guessed_word:
        print("Congratulations! You guessed the word:", "".join(guessed_word))
    else:
        print("Sorry, you ran out of attempts. The word was:", secret_word)

hangman()
