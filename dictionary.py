import csv
import os


def menu():
    """Main function for little programmer's dictionary"""

    while True:
        print("""Dictionary for a little programmer:
        1) search explanation by appelation
        2) add new definition
        3) show all appellations alphabetically
        4) show available definitions by first letter of appellation
        0) exit""")

        order = input("Enter a number to choose what to do: ")
        if order == "1":
            search_explanation()
        elif order == "2":
            add_word()
        elif order == "3":
            alphabetic_order()
        elif order == "4":
            search_by_letter()
        elif order == "0":
            quit()
        else:
            print("Wrong command. Choose one number from the list above.")


def dictionary():
    """Read data from the file and put them into dictionary"""
    my_dict = {}
    with open("dictionary.csv", "r") as source:
        reader = csv.reader(source, delimiter="\t")
        for row in reader:
            my_dict[row[0]] = (row[1], row[2])
        return my_dict


def search_explanation():
    """Print out the definition of the input word from the file"""
    my_dict = dictionary()
    appelation = input("\nEnter a word to see its definition: ")
    occurence = 0
    for key in my_dict.keys():
        if key == appelation.capitalize():
            explanation = my_dict[key][0]
            root = my_dict[key][1]
            print("\n%s is %s\nSource: %s" % (key.upper(), explanation, root))
            occurence = 1
    if occurence == 0:
        print("\nSorry, there is no such word in our dictionary.")
    print("\nPress enter to continue")
    input()
    os.system('cls' if os.name == 'nt' else 'clear')


def add_word():
    """Add new appelation to the file"""
    word = input("\nEnter a word you want to add into a dictionary: ")
    explanation = input("\nType a definision of this word: ")
    root = input("\nType the source of the information: ")
    with open("dictionary.csv", "a") as source:
        writer = csv.writer(source)
        writer.writerow(["%s\t%s\t%s" % (word.capitalize(), explanation, root)])
    print("\nPress enter to continue")
    input()
    os.system('cls' if os.name == 'nt' else 'clear')


def alphabetic_order():
    """Print all the appelations from the file in the alphabetic order"""
    my_dict = dictionary()
    words = sorted(my_dict.keys())
    for word in words:
        print(word)
    print("\nPress enter to continue")
    input()
    os.system('cls' if os.name == 'nt' else 'clear')


def search_by_letter():
    """Show all available appelations for input letter and print out the definition of chosen one"""
    my_dict = dictionary()
    letter = input("\nEnter the first word's letter: ")
    available_words = []
    for key in my_dict.keys():
        if key[0] == letter.upper():
            available_words.append(key)
    if len(available_words) > 0:
        for word in available_words:
            print(word)
        word = input("\nChoose a word from the list above: ")
        occurence = 0
        for key in my_dict.keys():
            if key == word.capitalize():
                explanation = my_dict[key][0]
                root = my_dict[key][1]
                print("\n%s is %s\nSource: %s" % (key.upper(), explanation, root))
                occurence = 1
        if occurence == 0:
            print("\nSorry, there is no such word in our dictionary.")
    else:
        print("\nSorry, there is any word for the letter %s." % letter)
    print("\nPress enter to continue")
    input()
    os.system('cls' if os.name == 'nt' else 'clear')


menu()
