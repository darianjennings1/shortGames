# Simple Hangman Project
# Darian Jennings - 08/23/2020
# Hangman: interactive word guessing game, word is randomly chosen each iteration. 
# Limit is 6 incorrect guesses, repeats will not count against you.

import random


def get_word():
    words = ['panda', 'giraffe', 'rhino', 'alligator', 'lion', 'tiger',
             'donkey', 'horse', 'dog', 'raccoon', 'squirrel', 'jazz',
             'classic', 'rock', 'september', 'july', 'august', 'terrestrial'
             'aliens', 'blanket', 'lotion', 'decipher', 'algorithms', 'data',
             'mathematics', 'signals', 'discrete', 'structure', 'programming', 'python'
             'matlab', 'java', 'ruby', 'assembly', 'engineering', 'organization', 'university',
             'religion', 'hangman', 'sudoku', 'football', 'soccer', 'basketball', 'bison', 'wolf',
             'mammal', 'speed', 'velocity', 'tension', 'friction', 'force', 'studio', 'apartment']
    word = random.choice(words)
    return word.upper()


def play(word):
    word_progress = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display(tries))
    print(word_progress)
    while not guessed and tries > 0:
        print("You have ", tries, " possible attempts")
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("\nYou already guessed the letter", guess, " try again")
            elif guess not in word:
                print("\n", guess, "is not in the word....")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("\nGood job, ", guess, " is in the word!")
                guessed_letters.append(guess)
                word_list = list(word_progress)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_list[index] = guess
                word_progress = "".join(word_list)
                if "_" not in word_progress:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("\nYou already guessed the word", guess, " try again")
            elif guess != word:
                print("\n ", guess, " is not the word....")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_progress = word
        else:
            print("\n", guess, " is not a valid guess. Try again.")
        print(display(tries))
        print(word_progress)
        print("\n")
    if guessed:
        print("You guessed the word correctly, you win!")
    else:
        print("You ran out of tries.. The word was " + word)


def display(tries):
    stages = ["""
                --------------
                |      |      |
                |      O      |
                |     \\|/    |
                |      |      |
                |     / \\     |
                ---------------
                """,
              """
                --------------
                |      |      |
                |      O      |
                |     \\|/    |
                |      |      |
                |     /       |
                ---------------
                """,
              """
                --------------
                |      |      |
                |      O      |
                |     \\|/    |
                |      |      |
                |             |
                ---------------
                """,
              """
                --------------
                |      |      |
                |      O      |
                |     \\|     |
                |      |      |
                |             |
                ---------------
                """,
              """
                --------------
                |      |      |
                |      O      |
                |      |      |
                |      |      |
                |             |
                ---------------
                """,
              """
                --------------
                |      |      |
                |      O      |
                |             |
                |             |
                |             |
                ---------------
                """,
              """
                --------------
                |      |      |
                |             |
                |             |
                |             |
                |             |
                ---------------
                """,

              ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Would you like to play again Y/N?  ").strip().upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
