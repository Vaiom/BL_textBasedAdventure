# Course: CS30 P1
# Name: Bryant Liu
# Date created: 2021-09-22
# Description: RPG Simple Menu Assignment
# ==============================================================
# YYYY-MM-DD / CHANGELOG (LATEST AT THE TOP)
# ==============================================================
# 2021-10-14 / Modified "simple_menu.py" (this file)
#               / Adjusted formatting
#               / Changed names of functions and variables to improve readability
# 2021-10-08 / Modified "simple_menu.py" (this file)
#               / Added a changelog inside file
#               / Fixed a function breaking indentation error
#               / Fixed docstrings, blank lines to improve readability
# 2021-09-22 / Created "simple_menu.py" (this file)
# ===============================================================


def line(width=1, repetition=1):
    """Function that can print multiple "bar of lines",
       which makes the text UI easier to read."""
    for repeat in range(0, (repetition)):
        if width == 0:
            print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
        if width == 1:
            print("--------------------------------------------------")
        if width == 2:
            print("==================================================")


def menu(text=None):
    """Function for opearting the menu"""
    while True:
        line()
        print(text)
        line(0)
        # List and for loop to print available actions.
        list = ["status", "inventory", "attack", "rest", "quit"]
        lineNo = 1
        for e in list:
            print("(" + str(lineNo) + ")-" + e)
            lineNo = lineNo + 1
        line(0)
        # Asks for the user's input.
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
            print("   |You have quit!")
            line()
            quit()
        else:
            print("   |>>> INVALID <<<")


def situation1():
    """Function that calls the menu() function with text parameter"""
    situ_text = "You have encountered a slime! What do you do?"
    menu(situ_text)


situation1()

