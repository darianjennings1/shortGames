# Speed-Typing Test
# Darian Jennings, created 8/23/20, updated 5/6/21
import time


def play(level):
    sentences = {
        1: "This level is very easy",
        1: "Hello this is a speed typing test written in python programming language",
        2: "You have chosen the most difficult level possible for this simple python program",
        3: "The creator of this simplistic game is unknown, I tried to google the answer and had no luck"
    }
    # retrieves a phrase based on user inputted level
    phrase = sentences.get(level)
    pc = letterCount(phrase)
    # returns the # of letters in the phrase,, pc == phraseCount
    t0 = time.time()
    print("Enter the following phrase:\n" + phrase)
    userInput = input()
    # ic == input count
    ic = letterCount(userInput)
    t1 = time.time()
    # estimated reading time based on phrase
    readingTime = calculateReadingTime(phrase)
    # total time elapsed
    totalTime = round((t1 - t0) - readingTime, 2)
    # returns accuracy and number of mismatched key inputs
    acc, mism = calculateAccuracy(phrase, userInput, ic, pc)

    rate = 60 / totalTime
    wpm = round(len(phrase.split()) * rate, 2)

    print("The phrase had ", pc, " letters you entered ", str(ic-mism), " of the letters correctly.")
    print("Accuracy: ", acc, "%.")
    print("Total elapsed time: ", totalTime, " seconds")
    print("Expected words per minute -> ", wpm)


def calculateAccuracy(phrase, userInput, ic, pc):
    # will count the number of correct input letters in userInput
    mismatch = []
    if ic > pc:
        print("You entered " + str(ic-pc) + " letter(s) over the required amount.")
    elif ic < pc:
        print("You entered " + str(ic-pc) + " letter(s) under the required amount.")
    i = 0
    for letter in phrase:
        if letter != userInput[i]:
            mismatch.append("*")
        i += 1
    if mismatch:
        print("\nYou entered ", len(mismatch), " letter(s) incorrectly.")
    accuracy = round(((pc - len(mismatch)) / pc) * 100, 2)

    return accuracy,len(mismatch)


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
    # for letter in phrase: if letter.isalpha: count += 1
    for letter in phrase:
        if letter.isalpha:
            count += 1
    return count


def main():
    print("\n\nWelcome to the Speed-Typing Test!")
    level = int(input("What level would you like: \n1 == Beginner\n2 == Medium\n3 == Advanced\n"))
    play(level)

    while input("Would you like to play again Y/N?  ").strip().upper() == "Y":
        level = int(input("\nWhat level would you like: \n1 == Beginner\n2 == Medium\n3 == Advanced\n"))
        play(level)


if __name__ == "__main__":
    main()
