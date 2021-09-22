# Course: CS 30
# Period: 1
# Date created: 21 September 2021
# Date last modified: 22 September 2021
# Name: Bryant Liu
# Description: menu sample

# Function that prints a "bar of line", which makes the text UI easier to read.


def lineBreak():
    print("==================================================")


# Function for operating the menu

def menu(text=None):
    while True:
        lineBreak()
        print(text)
        # List and for loop to print available actions.
        list = ["status", "inventory", "attack", "rest", "quit"]
        lineNo = 1
        for e in list:
            print(">" + str(lineNo) + "<|" + e)
            lineNo = lineNo + 1
            # Asks for the user's input.
            userInput = input("/^\|--insert-here--> ")
        if userInput == "1":
            print("You checked your status!")
        elif userInput == "2":
            print("You viewed your inventory!")
        elif userInput == "3":
            print("You attacked the slime!")
        elif userInput == "4":
            print("You have rested and recovered stamina!")
        elif userInput == "5":
            print("You have quited!")
            lineBreak()
            quit()
        else:
            print(">>> INVALID <<<")


# Function that entails the situation.
# Calls out to menu function passing the text parameter.


def situation1():
    situText = "You have encountered a slime! What do you do?"
    menu(situText)

situation1()
 
