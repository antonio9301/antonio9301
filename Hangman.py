import random
from file import words
import string


def get_valid_word():
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word()
    to_be_guessed = set(word)
    alphabet = set(string.ascii_uppercase)
    guessed = set()

    while len(to_be_guessed) > 0:
        # show former guesses
        print("You have guessed these letters:", ' '.join(guessed))
        # show current word
        current_word = [letter if letter in guessed else '-' for letter in word]
        print("Current word:", ' '.join(current_word))
        # the guess part
        user_letter = input("\nPlease input your guess: ").upper()
        if user_letter in alphabet - guessed:
            guessed.add(user_letter)
            if user_letter in to_be_guessed:
                print(f"Yes, {user_letter} is in the word.")
                to_be_guessed.remove(user_letter)
            else:
                print(f"No, {user_letter} is not in the word.")
        elif user_letter in guessed:
            print("You have already guessed the word. Try again.")
        else:
            print("Invalid input. Try again.")
    print("Congrats! You have guessed the word", ' '.join(word))


hangman()
