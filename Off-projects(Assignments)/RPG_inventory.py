# Course: CS30 P1
# Name: Bryant Liu
# Date created: 2021-10-04
# Description: RPG_inventory Assignment
# ==============================================================
# YYYY-MM-DD / CHANGELOG (LATEST AT THE TOP)
# ==============================================================
# 2021-10-20 / Modified "RPG_inventory.py" (this file)
#               / Adjusted formatting to comply with PEP 8
# 2021-10-14 / Created "RPG_inventory.py" (this file)
# 2021-10-13 / Created "RPG_inventory.py" (this file)
# 2021-10-08 / Created "RPG_inventory.py" (this file)
#               / Core function of the code finalized
# 2021-10-07 / Created "RPG_inventory.py" (this file)
# 2021-10-06 / Created "RPG_inventory.py" (this file)
# 2021-10-05 / Created "RPG_inventory.py" (this file)
# 2021-10-04 / Created "RPG_inventory.py" (this file)
# ===============================================================


import sys


def line(width=1, repetition=1):
    """Print lines to improve text UI readability."""
    for repeat in range(0, (repetition)):
        if width == 0:
            print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
        if width == 1:
            print("--------------------------------------------------")
        if width == 2:
            print("==================================================")


dict_class = {"rookie": {
                        "description": "the classic new recruit",
                        "bonus": "+5 luck",
                        "health": 100,
                        "armor": 10,
                        "stamina": 100,
                        "critical rate": 10,
                        "luck": 5},
              "close-quarters expert": {
                        "description":
                        "slaughter your opponents with brute force",
                        "bonus": "+10% melee damage",
                        "health": 120,
                        "armor": 20,
                        "stamina": 100,
                        "critical rate": 15,
                        "luck": 0},
              "triggerman": {
                        "description": "overwhelm your foes with gunfire",
                        "bonus": "+10% gun damage",
                        "health": 100,
                        "armor": 10,
                        "stamina": 100,
                        "critical rate": 5,
                        "luck": 0}
              }


def menu_class():
    """
    Navigates the "dict_class" dictionary.
    Allows user to change their class.
    """
    global u_class
    while True:
        # Prints user's current class.
        line(2)
        print(f"   |PLAYER INFO:")
        line(0)
        print(f"   |Your Class: {u_class.capitalize()}")
        line(0)
        # Prints user's current class specifications.
        tag = {"health": "HP ",
               "armor": "AMR",
               "stamina": "STA",
               "critical rate": "CR ",
               "luck": "LK "
               }
        y = 0
        for numb in dict_class[u_class]:
            y = y + 1
            if y <= 2:
                if y <= 1:
                    print(f"   |\
{dict_class[u_class]['description'].capitalize()}, \
{dict_class[u_class]['bonus']}.")
                continue
            print(f"{tag[numb]}|{dict_class[u_class][numb]}")
        # Prints user options.
        line(0)
        print("(1)-Change Class")
        print("(2)-Exit")
        line(0)
        # Asks for user's input.
        uinput = input(" ^ |--insert-number-->#")
        if uinput == "1":
            while True:
                # Prints "change class" menu.
                line(2)
                print(f"   |WHICH CLASS WOULD YOU LIKE TO BE")
                line(0)
                print(f"   |Equipped: {u_class.capitalize()}")
                line(0)
                # Prints the list of all available character classes.
                lineNo = 1
                for class_item in dict_class:
                    print(f"({str(lineNo)})-{class_item.capitalize()}")
                    lineNo = lineNo + 1
                line(0)
                print(f"({(1+(len(dict_class)))})-Exit")
                line(0)
                # Asks for user's input.
                uinput = input(" ^ |--insert-number-->#")
                class_classification = {1: "rookie",
                                        2: "close-quarters expert",
                                        3: "triggerman"
                                        }
                # Changes user's current class to the selected class.
                for selection in range(1, (1+(len(dict_class)))):
                    if uinput == str(selection):
                        u_class = class_classification[selection]
                # Exits the menu when appropriate.
                x = []
                for numb in range(1, (1+(len(dict_class)))):
                    x.append(str(numb))
                if uinput in x:
                    break
                elif uinput == str(1+(len(dict_class))):
                    break
                else:
                    print("   |>>> INVALID <<<")
        elif uinput == "2":
            break
        else:
            print("   |>>> INVALID <<<")


dict_inv = {"laser gun": {
                            "description":
                            "inflict high concentrations of rapid light",
                            "type": "ranged",
                            "damage": 15,
                            "stamina drain": 5,
                            "critical rate": 0},
            "steel dagger": {
                            "description":
                            "short, sharp, and a reliable steel blade",
                            "type": "melee",
                            "damage": 30,
                            "stamina drain": 15,
                            "critical rate": 25},
            "bandage": {
                            "description": "used to treat minor injuries",
                            "type": "miscellaneous",
                            "heal": 20,
                            "stamina drain": 0}
            }


def menu_inventory():
    """
    Navigates the "dict_inv" dictionary.
    Allows user to change equipped item, and remove items from their inventory.
    """
    global u_hand
    global u_inventory
    while True:
        # Incase user decides to remove an equipped item.
        if u_hand not in u_inventory:
            u_hand = "None"
        # Prints out the inventory menu header.
        line(2)
        print(f"   |YOUR INVENTORY:")
        lineNo = 1
        # Prints out all the available items in the player's inventory.
        for item in u_inventory:
            print(f"   -{item.capitalize()}")
            lineNo = lineNo + 1
        line(0)
        # Prints out user's current hand and specifications if applicable.
        print(f"   |Equipped: {u_hand.capitalize()}")
        if u_hand != "None":
            print(f"   |{dict_inv[u_hand]['description']}")
            for specs in dict_inv[u_hand]:
                if specs == "description":
                    continue
                else:
                    print(f"   |{specs} - {dict_inv[u_hand][specs]}")
        # Prints out available actions the user can take.
        line(0)
        print("(1)-Change Equipped Item")
        print("(2)-Remove Item from Inventory")
        print("(3)-Exit")
        line(0)
        # Asks for user's input.
        uinput = input(" ^ |--insert-number-->#")
        if uinput == "1":
            while True:
                # Prints out the equip item menu.
                line(2)
                print(f"   |WHICH ITEM WOULD YOU LIKE TO EQUIP")
                line(0)
                print(f"   |Equipped: {u_hand.capitalize()}")
                line(0)
                # Prints out all possible items to equip plus the exit option.
                lineNo = 1
                for item in u_inventory:
                    print(f"({str(lineNo)})-{item.capitalize()}")
                    lineNo = lineNo + 1
                line(0)
                print(f"({(1+(len(u_inventory)))})-Exit")
                line(0)
                # Asks for user's input.
                uinput = input(" ^ |--insert-number-->#")
                # Equips the selected item.
                for i in range(1, (1+(len(u_inventory)))):
                    if uinput == str(i):
                        u_hand = u_inventory[i-1]
                # Exits the menu if appropriate.
                x = []
                for i in range(1, (1+(len(u_inventory)))):
                    x.append(str(i))
                if uinput in x:
                    break
                elif uinput == str(1+(len(u_inventory))):
                    break
                else:
                    print("   |>>> INVALID <<<")
        elif uinput == "2":
            while True:
                # Prints out the remove item menu.
                line(2)
                print(f"   |WHICH ITEM WOULD YOU LIKE TO REMOVE")
                # Prints out a list of removable items in the user's inventory.
                # Aswell as the exit option.
                lineNo = 1
                for item in u_inventory:
                    print(f"({str(lineNo)})-{item.capitalize()}")
                    lineNo = lineNo + 1
                print(f"({(1+(len(u_inventory)))})-Exit")
                # Asks for user's input.
                uinput = input(" ^ |--insert-number-->#")
                # Removes the selected item.
                for i in range(1, (1+(len(u_inventory)))):
                    if uinput == str(i):
                        u_inventory.remove(u_inventory[i-1])
                # Exits the menu if appropriate.
                x = []
                for i in range(1, (1+(len(u_inventory)))):
                    x.append(str(i))
                if uinput in x:
                    break
                elif uinput == str(1+(len(u_inventory))):
                    break
                else:
                    print("   |>>> INVALID <<<")
        elif uinput == "3":
            break
        else:
            print("   |>>> INVALID <<<")


dict_location = {"situation tile":
                 "you are prompted and need to make a decision",
                 "resources tile":
                 "you find plenty of supplies to recover \
(stamina recovers here)",
                 "enemy tile": "you fight enemies for your survival",
                 "elite enemy tile":
                 "you fight stronger enemies, that rewards higher",
                 "boss tile": "fight a boss"
                 }


def menu_location():
    """Navigates the "dict_location" dictionary."""
    while True:
        # Prints the tile selection menu.
        line(2)
        print(f"   |SELECT AN AVAILABLE TILE:")
        line(0)
        # Prints out possible tiles and exit using for loops.
        listz = list(dict_location.keys())
        listz.append("exit")
        lineNo = 1
        for e in listz:
            if e == "exit":
                line(0)
                print(f"({str(lineNo)})-{e.capitalize()}")
                line(0)
                continue
            print(f"({str(lineNo)})-{e.capitalize()}")
            lineNo = lineNo + 1
        # Asks for user's input.
        uinput = input(" ^ |--insert-number-->#")
        # Prints description of the selected tile.
        for i in range(1, (len(listz))):
            if uinput == str(i):
                print(f"   |{listz[(int(uinput))-1].capitalize()}:")
                print(f"   |\
{dict_location[listz[(int(uinput))-1]].capitalize()}.")
        # Exits or continues loop accordingly.
        x = []
        for i in range(1, 6):
            x.append(str(i))
        if uinput in x:
            continue
        elif uinput == str(1+(len(dict_location))):
            break
        else:
            print("   |>>> INVALID <<<")


def menu_main(text=None):
    """Main function that serves as a main menu
       Also calls relevant functions."""
    while True:
        line(2)
        print(f"   |MAIN  MENU:")
        line(0)
        # List and for loop to print available actions.
        listz = ["status", "inventory", "location", "quit"]
        lineNo = 1
        for e in listz:
            print(f"({str(lineNo)})-{e.capitalize()}")
            lineNo = lineNo + 1
        # Asks for the user's input.
        line(0)
        uinput = input(" ^ |--insert-number-->#")
        if uinput == "1":
            menu_class()
        elif uinput == "2":
            menu_inventory()
        elif uinput == "3":
            menu_location()
        elif uinput == "4":
            print("   |You have quit the game!")
            line(2)
            print("\n\n\n")
            break
        else:
            print("   |>>> INVALID <<<")


# Global variables accessed by functions to modify/store the player's data.
u_class = "rookie"  # Default class.
u_hand = "None"
u_inventory = list(dict_inv.keys())

# Test print of "dict_class".
line(2)
print(f"{'characters'.capitalize()}")
line(2)
for players_class in dict_class:
    print(f"{players_class.capitalize()}: \
{dict_class[players_class]['description']}")
    line(0)
    for specs in dict_class[players_class]:
        if specs == "description":
            continue
        else:
            print(f"{specs} - {dict_class[players_class][specs]}")
    print("\n\n")

# Test print of "dict_inv".
line(2)
print(f"{'inventory'.capitalize()}")
line(2)
for item in dict_inv:
    print(f"{item.capitalize()}: {dict_inv[item]['description']}")
    line(0)
    for specs in dict_inv[item]:
        if specs == "description":
            continue
        else:
            print(f"{specs} - {dict_inv[item][specs]}")
    print("\n\n")

# Test print of "dic_location".
line(2)
print(f"{'location tiles'.capitalize()}")
line(2)
for tile in dict_location:
    print(f"{tile.capitalize()}:\n{dict_location[tile].capitalize()}.\n")


menu_main()


sys.exit()

