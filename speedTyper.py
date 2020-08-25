# Simple Speed-Typing Test Project
# Darian Jennings - 08/23/2020
import time


def play(level):
    sentences = {
        1: "Hello this is a speed typing test written in python programming language",
        2: "The creator of this simplistic game is unknown, I tried to google the answer and had no luck",
        3: "You have chosen the most difficult level possible for this simple python program"
    }
    # retrieves a phrase based on user inputted level
    phrase = sentences.get(level)
    pc = letterCount(phrase)
    print("This phrase has ", pc, "letters.")
    # returns the # of letters in the phrase pc == phraseCount
    pc = letterCount(phrase)

    t0 = time.time()
    print("Enter the following phrase:\n " + phrase + "\n")
    userInput = input()
    # ic == input count
    ic = letterCount(userInput)

    t1 = time.time()

    readingTime = calculateReadingTime(phrase)
    totalTime = round((t1 - t0) - readingTime, 2)
    acc = calculateAccuracy(phrase, userInput, pc)

    rate = 60 / totalTime
    wpm = round(len(phrase.split()) * rate, 2)

    print("The phrase had ", pc, " letters you entered ", ic, " letters.")
    print("Your accuracy from this test was ", acc, "%.")
    print("Total time elapsed: ", totalTime, " seconds")
    print("The program calculated your expected words per minute -> ", wpm)


def calculateAccuracy(phrase, userInput, pc):
    # will count the number of correct input letters in userInput
    mismatch = []
    i = 0
    for letter in phrase:
        if i not in range(len(userInput)):
            mismatch.append("*")
            print("You did not enter enough letters....")
            break
        elif letter.isalpha() and userInput[i].isalpha() and letter != userInput[i]:
            mismatch.append("*")
        i += 1
    print("\nYou entered ", len(mismatch), " letter(s) incorrectly.")
    accuracy = round(((pc - len(mismatch)) / pc) * 100, 2)
    return accuracy


def calculateReadingTime(phrase):
    # avg human reads 225 words per min (225/60)
    # phraseCount gives us the number of words in the selected phrase
    # 225/60 -> 225/phrase count tells us what factor we need to convert the original 60s by
    phraseWordCount = len(phrase.split())
    ratioFactor = 225 / phraseWordCount
    rt = 60 / ratioFactor
    return rt


def letterCount(phrase):
    count = 0
    for letter in phrase:
        if letter.isalpha:
            count += 1
    return count


def wordCount(phrase):
    return len(phrase.split())


def main():
    print("Welcome to the Speed-Typing Test!")
    level = int(input("What level would you like: \n1 == Beginner\n2 == Medium\n3 == Advanced\n"))
    play(level)
    while input("Would you like to play again Y/N?  ").strip().upper() == "Y":
        level = int(input("\nWhat level would you like: \n1 == Beginner\n2 == Medium\n3 == Advanced\n"))
        play(level)


if __name__ == "__main__":
    main()
