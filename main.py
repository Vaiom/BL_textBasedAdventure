# Course: CS 30
# Period: 1
# Date created: 21 September 2021
# Date last modified: 4st October 2021
# Name: Bryant Liu
# Description: Main Game
#==============================================================
#CHANGELOG (LATEST AT THE TOP)
#==============================================================
#2021-10-04 / Added code from "menu.py" (now deleted)
#           / Added dictionaries
#
#
#
#
#
#
#
#
#
#
#
#
#
#===============================================================

inventory_data = {"sword": 3}
location_data = 


enemies_data = {"slime": 5}


controlsDictiionary = {}


userHP = 20
userSTA = 100




def lineBreak(width = None):
  if width == None:
    print("--------------------------------------------------")
  if width == 1:
    print("==================================================")

def menu(text = None, options1 = None, options2 = None, options3 = None, options4 = None, options5 = None):
  while True:
    lineBreak(1)
    print(text)
    if options1 != None:
      print(">1<|" + options1)
    if options2 != None:
      print(">2<|" + options2)
    if options3 != None:
      print(">3<|" + options3)
    if options4 != None:
      print(">4<|" + options4)
    if options5 != None:
      print(">5<|" + options5)
    userInput = input("/^\ --insert-here--> ")
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
      pass










def situation1():
  funcText = "You have encountered a slime! What do you do?"
  opt1 = "status"
  opt2 = "inventory"
  opt3 = "attack"
  opt4 = "rest"
  opt5 = "quit"
  menu(funcText,opt1,opt2,opt3,opt4,opt5)

situation1()




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