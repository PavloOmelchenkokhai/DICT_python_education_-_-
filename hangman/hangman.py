import random

def hangman():
    words = ['python', 'java', 'javascript', 'php']
    secret_word = random.choice(words)
    attempts = 8
    guessed_letters = set()
    display_word = '-' * len(secret_word)

    while attempts > 0:
        print("\n" + display_word)
        guess = input("Input a letter: > ").strip().lower()

        if len(guess) != 1:
            print("You should input a single letter")
            continue
        if not guess.islower() or not guess.isalpha():
            print("Please enter a lowercase English letter")
            continue
        if guess in guessed_letters:
            print("You've already guessed this letter")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            display_word = ''.join([letter if letter in guessed_letters else '-' for letter in secret_word])
            if display_word == secret_word:
                print("\nYou guessed the word " + secret_word + "!")
                print("You survived!")
                break
        else:
            print("That letter doesn't appear in the word")
            attempts -= 1
    else:
        print("\nYou lost!")

print("HANGMAN")
while True:
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == "play":
        hangman()
    elif choice == "exit":
        break
