import random
print ("HANGMAN")
words = ['python', 'java', 'javascript', 'php']
secret_word = random.choice(words)
attempts = 8
guessed_letters = set()
display_word = '-' * len(secret_word)

while attempts > 0:
    print("\n" + display_word)
    guess = input("Input a letter: > ").strip().lower()

    if guess in guessed_letters:
        print("You've already tried that letter.")
    elif guess in secret_word:
        guessed_letters.add(guess)
        display_word = ''.join([letter if letter in guessed_letters else '-' for letter in secret_word])
        if display_word == secret_word:
            print("\n" + display_word)
            print("You survived!")
            print("Thanks for playing!\nWe'll see how well you did in the next stage.")
            break
    else:
        print("That letter doesn't appear in the word")
        attempts -= 1
        guessed_letters.add(guess)
else:
    print("\nYou lost!")
