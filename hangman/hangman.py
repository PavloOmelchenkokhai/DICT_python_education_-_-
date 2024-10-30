print ("HANGMAN")

secret_word = "python"
guess = input("Guess the word: ").strip().lower()
if guess == secret_word:
 print("You survived!")
else:
 print("You lost!")
