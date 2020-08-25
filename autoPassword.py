# Automated password retrieval script
# This is a sample script, my personal script contains 100+ passwords; allows me to retrieve easily without
# reading through every single line of organization and password combination
# Dictionary {organization == key, password == value}
# Darian Jennings , 08/25/2020


def getPassword():
    passDict = {
        'organization': "password1234"
        'github': "githubPassword"
    }
    return passDict


def main():
    data = getPassword()
    passwords = dict((i.upper(), j) for i, j in data.items())
    key = input("What organization do you need the password for?:\n").upper()
    if key in passwords:
        print("Password is: ", passwords[key])
    else:
        print("The organization key you entered is either misspelled or does not exist")
    if input("Would you like to re-enter Y/N?  ").strip().upper() == "Y":
        main()


if __name__ == "__main__":
    main()
