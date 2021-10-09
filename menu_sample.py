# Course: CS 30
# Period: 1
# Date created: 22 October 2021
# Date last modified: 08 October 2021
# Name: Bryant Liu
# Description: menu sample
# ==============================================================
# CHANGELOG (LATEST AT THE TOP)
# ==============================================================
# 2021-10-08 / Recreated and modified "main.py" (this file)
#            / Added a changelog inside file
#            / Fixed a function breaking indentation error
#            / Fixed docstrings, blank lines to improve readability
# 2021-10-04 / Removed "main.py" (this file)
# 2021-09-22 / Created "main.py" (this file)
# ===============================================================


def lineBreak(width=1, times=1):
    """Function that can print multiple "bar of lines",
        which makes the text UI easier to read."""
    for repeat in range(0, (times)):
        if width == 0:
            print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
        if width == 1:
            print("--------------------------------------------------")
        if width == 2:
            print("==================================================")


def menu(text=None):
    """Function for opearting the menu"""
    while True:
        lineBreak()
        print(text)
        lineBreak(0)
        # List and for loop to print available actions.
        list = ["status", "inventory", "attack", "rest", "quit"]
        lineNo = 1
        for e in list:
            print("(" + str(lineNo) + ")-" + e)
            lineNo = lineNo + 1
        # Asks for the user's input.
        lineBreak(0)
        userInput = input(" ^ |--insert-here-->#")
        if userInput == "1":
            print("   |You checked your status!")
        elif userInput == "2":
            print("   |You viewed your inventory!")
        elif userInput == "3":
            print("   |You attacked the slime!")
        elif userInput == "4":
            print("   |You have rested and recovered stamina!")
        elif userInput == "5":
            print("   |You have quited!")
            lineBreak()
            quit()
        else:
            print("   |>>> INVALID <<<")


def situation1():
    """Function that calls the menu() function with text parameter"""
    situText = "You have encountered a slime! What do you do?"
    menu(situText)


situation1()

