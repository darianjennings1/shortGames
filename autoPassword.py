# Automated password retrieval script - passkeys stored in json file
# Darian Jennings 
# refer to "passwords.json" file to store passwords and data

import json


def main():
    data = getData()
    if not data:
        print("There is currently no data in the storage file...")
        data = {}
    # variables for while/for loops
    repeat = 'Y'
    r1 = 'Y'

    while repeat == 'Y' and data:
        passwords = dict((i.upper(), j) for i, j in data.items())
        choice = getMenu()
        if not data:
            print("\nThere is currently no data...select option 3 to add data.")

        elif choice == 1:
            while r1 == 'Y':
                org = input("What organization do you need the password for?\n").strip().upper()
                if org in passwords:
                    print("Password is: ", passwords[org])
                else:
                    print("The organization key you entered is either misspelled or does not exist")
                r1 = input("Would you like to retrieve another password Y/N? ").strip().upper()

        elif choice == 2:
            while r1 == 'Y':
                org = input("What organization do you need to update the password for?\n").strip().upper()
                if org in passwords:
                    passwords[org] = input("What would you like the new password to be?\n").strip()
                    print(org + " password successfully updated")
                else:
                    print("The organization key you entered is either misspelled or does not exist")
                dumpPass(passwords)
                r1 = input("Would you like to update another organization password Y/N?  ").strip().upper()

        elif choice == 3:
            while r1 == 'Y':
                org = input("What is the organization name?\n").strip().upper()
                if org in passwords:
                    print(org + " already exists...")
                else:
                    passwords[org] = input("What is the password for this organization?\n").strip()
                    print("The organization and password have been successfully saved")
                dumpPass(passwords)
                r1 = input("Would you like to add another organization & password combination Y/N? ").strip().upper()

        elif choice == 4:
            break
        else:
            print("You entered an invalid menu option...")

        # outer for loop to go back to main menu or exit program
        repeat = input("Would you like to go back to the main menu? Y/N ").strip().upper()
        # refresh to pull new data if added/changed from options 2/3
        if repeat == 'Y':
            data = getData()
            r1 = 'Y'
    print("\n")


def getMenu():
    print("\nPASSWORD MAIN MENU\n------------------")
    switch = {
        1: "Retrieve password",
        2: "Update password",
        3: "Add new organization and password",
        4: "Exit"
    }
    for x, y in switch.items():
        print(x, y)
    valid = False
    ans = 0
    while not valid:
        ans = input("What would you like to do?\n")
        try:
            int(ans)
            valid = True
            ans = int(ans)
        except ValueError:
            print('Invalid input!')

    return ans


def getData():
    file = open('pass.json', )
    data_values = json.load(file)
    file.close()
    return data_values


def dumpPass(passwords):
    with open('pass.json', 'w') as fp:
        json.dump(passwords, fp, indent=4)
        fp.close()


if __name__ == "__main__":
    main()
