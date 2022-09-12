import random
import string


def generator(choice, length, userText, place):
    a = string.ascii_lowercase
    b = string.ascii_uppercase
    c = string.punctuation
    d = string.digits
    e = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
    selection = {1: a, 2: b, 3: c, 4: d, 5: e}
    temp = selection[choice]
    if (not userText) and place == 0:
        password = "".join(random.choice(temp) for x in range(length))
    elif userText and place == 1:
        password = "" + userText + "".join(random.choice(temp) for x in range(length))
    elif userText and place == 2:
        password = "".join(random.choice(temp) for x in range(length)) + userText
    else:
        password = ""
    return password


def main():
    repeat = 'Y'
    passwords = {}
    cnt = 0
    while repeat == 'Y':
        print("\nWelcome to the CUSTOMIZED PASSWORD GENERATOR ")
        print("Select an option for your password."
              "\n1.Lowercase Letters\n", string.ascii_lowercase,
              "\n\n2.Uppercase Letters\n", string.ascii_uppercase,
              "\n\n3.Punctuation\n", string.punctuation,
              "\n\n4.Digits\n", string.digits,
              "\n\n5. Options 1 & 2\n",
              "\n6. Options 1, 2, & 3\n",
              "\n7. Options 1, 2, 3, & 4\n")
        print("Current passwords created: " + str(passwords))
        choice = int(input())
        length = int(input("What length do you want your password to be? (>0) :\n"))
        index = 0
        if input("Do you want to add your own desired prefix or suffix to the password? Y/N\n").upper() == 'Y':
            index = int(input("1.Prefix\n2.Suffix\n"))
            userText = input("Enter the custom userText: ")
        else:
            userText = ''
        tempP = generator(choice, length, userText, index)
        print("PASSWORD: ", tempP)
        repeat = input("Would you like to go back to the main menu? Y/N ").strip().upper()
        if repeat == 'Y':
            passwords[cnt] = tempP

    print("Goodbye!\nPasswords created: " + str(passwords))


if __name__ == "__main__":
    main()
