import random

words = ["CODE", "VSCODE", "HANGMAN", "【entity-ACCENTURE¦canonical_name=ACCENTURE】", "PYTHON"]
secret_word = random.choice(words)

guessed_letters = set()#Will be used for guessed words

attempts_left = 6#Number of wrong guesses allowed

HANGMAN_STAGES = [
"""
   +---+
   |   |
       |
       |
       |
       |
=========""",
"""
   +---+
   |   |
   O   |
       |
       |
       |
=========""",
"""
   +---+
   |   |
   O   |
   |   |
       |
       |
=========""",
"""
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========""",
"""
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
=========""",
"""
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
=========""",
"""
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
========="""
]

def clear_screen():
    print("\n" * 2)

while attempts_left > 0:#Do the following whiile you stil have attempts
    display = ""
    won = True
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
            won = False

    wrong_guesses = 6 - attempts_left
    print(HANGMAN_STAGES[wrong_guesses])#Prints the current hangman diagram based on wrong guesses
    print(f"\nWord: {display}")
    print(f"Attempts left: {attempts_left} | Guessed: {' '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

    if won:
        clear_screen()
        print("""
 __   __            _    _ _       _ 
 \\ \\ / /           |  | | |     | |
  \\ V /___  _   _  | |  | | | __ _| |
   \\ / _ \\| | | | | |  | | |/ _` | |
   | | (_) | |_| | | |/\\| | | (_| | |
   |_|\\___/ \\__,_| \\__/\\__/ \\__,_|_|
                                     
        """)
        print(f"   The word was: {secret_word}")
        print(f"   You survived with {attempts_left} attempts left!")
        break

    guess = input("\nGuess a letter: ").upper().strip()

    if not guess:
        continue

    if len(guess) > 1:
        if guess == secret_word:
            clear_screen()
            print(HANGMAN_STAGES[wrong_guesses])
            print(f"\n   You guessed the whole word: {secret_word}")
            print("   YOU WON!!!")
            break
        else:
            attempts_left -= 1
            print(f"'{guess}' is not the word!")
            continue

    if guess in guessed_letters:#Checks for repeated letters
        print("You already guessed that letter!")
        continue

    guessed_letters.add(guess)#Save guessed letters

    if guess not in secret_word:
        attempts_left -= 1#Reduces number of attempts when you guessed wrong
        print("Wrong guess!")

if attempts_left == 0:
    clear_screen()
    print(HANGMAN_STAGES[6])#checks if you have used all your attempts then displays "game over"
    print(f"""
  ____    _    __  __ _____    _____     _____ ____  
 / ___|  / \\  | \\/ | ____|  / _ \\ \\   / / _ \\|  _ \\ 
| |  _  / _ \\ | |\\/| |  _|   | | | \\ \\ / / | | | |_) |
| |_| |/ ___ \\| |  | | |___  | |_| |\\ V /| |_| |  _ < 
 \\____/_/   \\_\\_|  |_|_____|  \\___/  \\_/  \\___/|_| \\_\\
                                                          
    The word was: {secret_word}
    """)#Reveals the secrete word
    print("Press any key to exit...")