import random

def play_hangman():
    # create a list of words for the player to guess
    words = ["python", "programming", "language", "computer", "science"]
    word = random.choice(words)
    word_letters = set(word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set()
    word_guessed = set()
    used_word = []
    for i in word:
        used_word.append("_")
    tries = 6
    print("Welcome to Hangman!")
    while (len(word_letters) != 0) and tries > 0:
        print("You have", tries, "tries left!")
        print("Used letters: ", " ".join(used_letters))
        print("Word: ", " ".join(used_word))
        user_letter = input("Guess a letter:").lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.discard(user_letter)
                word_guessed.add(user_letter)
                for i in range(len(word)):
                    if word[i] in word_guessed:
                        used_word[i] = word[i]
            else:
                tries -= 1
        elif user_letter in used_letters:
            print("You already used that letter.")
        else:
            print("Invalid input, please enter a letter a-z.")
    if tries == 0:
        print("You lost! The word was", word)
    else:
        print("You won! The word was", word)

play_hangman()
