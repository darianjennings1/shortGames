import random
import string


def generator(choice, length, custom, place):
    a = string.ascii_lowercase
    b = string.ascii_uppercase
    c = string.punctuation
    d = string.digits
    e = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
    selection = {1: a, 2: b, 3: c, 4: d, 5: e}
    temp = selection[choice]
    if not custom and place == 0:
        password = "".join(random.choice(temp) for x in range(length))
    elif custom and place == 1:
        password = "" + custom + "".join(random.choice(temp) for x in range(length))
    elif custom and place == 2:
        password = "".join(random.choice(temp) for x in range(length)) + custom
    return password


def get_length():
    userInput = input("What length do you want your password to be?:\n")
    return int(userInput)


def main():
    print("***Welcome to the CUSTOMIZED PASSWORD GENERATOR***")
    print("Select an option for your password.\n1.Lowercase Letters\n", string.ascii_lowercase, "\n2.Uppercase Letters\n",
          string.ascii_uppercase, "\n3.Punctuation\n", string.punctuation, "\n4.Digits\n", string.digits,
          "\n5.All of the above\n")
    choice = int(input())
    length = get_length()
    if input("Do you want to add your own prefix or suffix to the password? Y/N").upper() == 'Y':
        place = int(input("1. Prefix\n2.Suffix\n"))
        custom = input("Enter the custom text: ")
    else:
        custom = ''
        place = 1
    print("PASSWORD: ", generator(choice, length, custom, place))


if __name__ == "__main__":
    main()
