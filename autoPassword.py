# Automated password retrieval script
# Dictionary {organization == key, password == value}
# Darian Jennings , 08/25/2020


def getPassword():
    passDict = {
        'snapchat': "DarianLon3!",
        'twitter': "Din0Lucid!!",
        'Gameofficial': "Din0Cap00!",
        'Instagram1': "Din0Darian!",
        'Instagram2': "Rapt0rDin0$!",
        'PayPal': "Jennings0!$0",
        'Microsoft': "Din0Jamal$!, Din0S0ft%$!, pin: 137920",
        'Walmart': "DarianJob1",
        'Apple': "Din0N1gha!",
        'AppleENCRYPTION': "DinoCap00",
        'Spotify': "pablo.00 Din0Cap00",
        'Xbox': "Din0Jamal?",
        'Collegeboard': "Dar1anCap00",
        'Gmmail': "Din0Jennings!?",
        'FAFSA': "dar1anjennings L1ghtDin0!,336278 , new 224789",
        'renweb': "DarianCap00",
        'goat': "Din0Jamal",
        'grail': "Jennings0!0",
        'marriott': "darianjennings Din0Black!",
        'amazon': "Lon3Din0D!",
        'LaCanteraResort': "darian.jennings@gvtc.com Din0Darian!",
        'AWSeducate': "Din0Black!",
        'gateway': "L1ghtDin0$!",
        'nationalinstruments': "RattlerDin0$!",
        'xbox': "Din0Penis!",
        'arbiter': "Din0Arb$!",
        'refpay': "Jennings00!",
        'airrosti': "Din0L1ght!$",
        'masteringchemistry': "RattlerDin0",
        'pearson': "L1ghtDin0",
        'chipotlescholarship': "Din0Potle!",
        'discover': "din0chipotl3, JenningsN1nja!",
        'nsls': "Din0Rattler!",
        'gotcha': "Darian.Jennings@gvtc.com, D@20ri00an",
        'bestbuy': "Din0Buy!$",
        'matlab': "Din0Jamal$!",
        'nasa': "djennings3 Din0Darian$!",
        'trend': "Din0Secu!",
        'github': "Din0Hub!",
        'linkedin': "Din0Link3r!",
        'IBM': "Din0Bm$!",
        'Cyclance': "Din0Cycl$!",
        'costar': "DStar$!",
        'discord': "Din0Cord$!",
        'dropbox': "Din0Boxz$!",
        'reu': "RattlerDin0!",
        'notredame': "RattlerDame$!0",
        'saws': "Din0Saw!",
        'ezpay': "Din0Saw%",
        'itch': "Din0Gamez!",
        'quizlet': "Jamal00!$",
        'turbotax': "username Din0Turb$!",
        'chipotle': "0843807, Din0Darian!",
        'efoodcard': "DinM0nster!, Din0Bank$!",
        'researchgate': "gate$Din0",
        'IEEE': "cdariane22",
        'ebooks': "Din0Book!"
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
