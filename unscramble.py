unscrambled = []


def main():
    logo = [
        "                                 ___     __              ___ ",
        "  ______ ___________ __ __  _____\_ |__ |  |   ____   __| _/ ",
        " /  ___// ___\_  __ \  |  \/     \| __ \|  | _/ __ \ / __ |  ",
        " \___ \\  \___|  | \/  |  /  | |  \ \_\ \  |_\  ___// /_/ |  ",
        "/____  >\___  >__|  |____/|__|_|  /___  /____/\___  >____ |  ",
        "     \/     \/                  \/    \/          \/     \/\n"
    ]

    for line in logo:
        print(line)

    readFiles()

# Read the original wordlist and the txt file with the scrambled words
def readFiles():
    # Makes the words from the files available to the whole program
    global words
    global scrambled

    print("[+] Reading Wordlist")
    mf = open("wordlist.txt", "r")
    words = mf.readlines()
    mf.close()

    print("[+] Reading Scrambled Wordlist")
    mf2 = open("scrambled.txt", "r")
    scrambled = mf2.readlines()
    mf2.close()

    matchStrings()


def matchStrings():
    print("[+] Matching Scrambled With Unscrambled")
    for text in scrambled:
        # rstrip() [right-strip] removes trailing characters
        text = text.rstrip("\n")
        txtSorted = ''.join(sorted(text))
        for word in words:
            word = word.rstrip("\n").rstrip("\r")
            wordSorted = ''.join(sorted(word))
            if txtSorted == wordSorted:
                unscrambled.append(word)

    displayUnscrambled()


def displayUnscrambled():
    global unscrambled

    print("[+] Task Complete --> All Strings Matched")
    print("[+] Unscrambled Words:")
    unscrambled = ','.join(map(str, unscrambled))
    print('-' * 80)
    print(unscrambled)
    print('-' * 80)


if __name__ == '__main__':
    main()

