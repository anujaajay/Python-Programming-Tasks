import random

words = ["apple", "tiger", "table", "house", "plant"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman!")

while wrong_guesses < max_wrong:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in word:
        guessed_letters.append(guess)
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining chances:", max_wrong - wrong_guesses)

if wrong_guesses == max_wrong:
    print("Game Over! The word was:", word)
