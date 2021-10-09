# Course: CS 30
# Period: 1
# Date created: 21 September 2021
# Date last modified: 08 October 2021
# Name: Bryant Liu
# Description: Main Game
#==============================================================
#CHANGELOG (LATEST AT THE TOP)
#==============================================================
#2021-10-08 / Modified "main.py" (this file)
#2021-10-07 / Modified "main.py" (this file)
#2021-10-06 / Modified "main.py" (this file)
#2021-10-05 / Modified "main.py" (this file)
#2021-10-04 / Added code from "menu.py" (now deleted)
#           / Added dictionaries
#===============================================================

import sys


def lineBreak(width = 1, times = 1):
    """Function that can print multiple "bar of lines", which makes the text UI easier to read."""
    for repeat in range(0,(times)):
        if width == 0:
            print("- - - - - - - - - - - - - - - - - - - - - - - - - ")
        if width == 1:
            print("--------------------------------------------------")
        if width == 2:
            print("==================================================")




character_data = {"rookie":{
                        "description": "the classic new recruit",
                        "bonus": "+5 luck",
                        "health": 100,
                        "armor": 10,
                        "stamina": 100,
                        "critical rate": 10,
                        "luck": 5},
                "close-quarters expert":{
                        "description": "slaughter your opponents with brute force",
                        "bonus": "+10% melee damage",
                        "health": 120,
                        "armor": 20,
                        "stamina": 100,
                        "critical rate": 15,
                        "luck": 0},
                "triggerman":{
                        "description": "overwhelm your foes with gunfire",
                        "bonus": "+10% gun damage",
                        "health": 100,
                        "armor": 10,
                        "stamina": 100,
                        "critical rate": 5,
                        "luck": 0}
                  }


inventory_data = {"laser gun":{
                            "description": "inflict high concentrations of rapid light",
                            "type": "ranged",
                            "damage": 15,
                            "stamina drain": 5,
                            "critical rate": 0},
                "steel dagger":{
                            "description": "short, sharp, and a reliable steel blade",
                            "type": "melee",
                            "damage": 30,
                            "stamina drain": 15,
                            "critical rate": 25},
                "bandage":{
                            "description": "used to treat minor injuries",
                            "type": "miscellaneous",
                            "heal": 20,
                            "stamina drain": 0}
                  }

location_data = {"situation tile": "you are prompted and need to make a decision",
                "resources tile": "you find plenty of supplies to recover (stamina recovers here)",
                "enemy tile": "you fight enemies for your survival",
                "elite enemy tile": "you fight stronger enemies, that rewards higher",
                "boss tile": "fight a boss"
                 }


player_class = "rookie"
player_current_hand = "None"
player_inventory = list(inventory_data.keys())















def character_info(mode = "menu"):
    global player_class
    if mode == "dict":
        lineBreak(2,1)
        print(f"{'characters'.capitalize()}\n")
        for players_class in character_data:
            print(f"{players_class.capitalize()}: {character_data[players_class]['description']}")
            lineBreak()
            for specifications in character_data[players_class]:
                if specifications == "description":
                    continue
                else:
                    print(f"{specifications} - {character_data[players_class][specifications]}")
            print("\n")
    else:
        while True:
            lineBreak()
            print(f"   |PLAYER INFO:")
            lineBreak(0)
            print(f"   |Your Class: {player_class.capitalize()}")
            lineBreak(0)
            y = 0
            tag = {"health": "HP ","armor": "AMR","stamina": "STA","critical rate": "CR ","luck": "LK "}
            for numb in character_data[player_class]:
                y = y + 1
                if y <= 2:
                    if y <= 1:
                        print(f"   |{character_data[player_class]['description'].capitalize()}, {character_data[player_class]['bonus']}.")
                    continue
                print(f"{tag[numb]}|{character_data[player_class][numb]}")
            lineBreak(0)
            print("(1)-Change Class")
            print("(2)-Exit")
            lineBreak(0)
            userInput = input(" ^ |--insert-number-->#")
            if userInput == "1":
                while True:
                    lineBreak()
                    print(f"   |WHICH CLASS WOULD YOU LIKE TO BE")
                    lineBreak(0)
                    print(f"   |Equipped: {player_class.capitalize()}")
                    lineBreak(0)
                    lineNo = 1
                    for e in character_data:
                        print(f"({str(lineNo)})-{e.capitalize()}")
                        lineNo = lineNo + 1
                    lineBreak(0)
                    print(f"({(1+(len(character_data)))})-Exit")
                    lineBreak(0)
                    userInput = input(" ^ |--insert-number-->#")
                    class_classification = {1: "rookie",2: "close-quarters expert",3: "triggerman"}
                    for i in range(1,(1+(len(character_data)))):
                        if userInput == str(i):
                            player_class = class_classification[i]
                    x = []
                    for i in range(1,(1+(len(character_data)))):
                        x.append(str(i))
                    if userInput in x:
                        break
                    elif userInput == str(1+(len(character_data))):
                        break
                    else:
                        print("   |>>> INVALID <<<")

            elif userInput == "2":
                break
            else:
                print("   |>>> INVALID <<<")











def inventory_info(mode = "menu"):
    global player_current_hand
    global player_inventory
    if mode == "dict":
        lineBreak(2,1)
        print(f"{'inventory'.capitalize()}\n")
        for item in inventory_data:
            print(f"{item.capitalize()}: {inventory_data[item]['description']}")
            lineBreak()
            for specifications in inventory_data[item]:
                if specifications == "description":
                    continue
                else:
                    print(f"{specifications} - {inventory_data[item][specifications]}")
            print("\n")
    else:
        while True:
            if player_current_hand not in player_inventory:
                player_current_hand = "None"
            lineBreak()
            print(f"   |YOUR INVENTORY:")
            listz = list(inventory_data.keys())
            lineNo = 1
            # prints out possible tiles using for loops
            for e in player_inventory:
                print(f"   -{e.capitalize()}")
                lineNo = lineNo + 1
            lineBreak(0)
            print(f"   |Equipped: {player_current_hand.capitalize()}")
            if player_current_hand != "None":
                print(f"   |{inventory_data[player_current_hand]['description']}")
                for specifications in inventory_data[player_current_hand]:
                    if specifications == "description":
                        continue
                    else:
                        print(f"   |{specifications} - {inventory_data[player_current_hand][specifications]}")
            lineBreak(0)
            print("(1)-Change Equipped Item")
            print("(2)-Remove Item from Inventory")
            print("(3)-Exit")
            lineBreak(0)
            userInput = input(" ^ |--insert-number-->#")
            if userInput == "1":
                while True:
                    lineBreak()
                    print(f"   |WHICH ITEM WOULD YOU LIKE TO EQUIP")
                    lineBreak(0)
                    print(f"   |Equipped: {player_current_hand.capitalize()}")
                    lineBreak(0)
                    lineNo = 1
                    for e in player_inventory:
                        print(f"({str(lineNo)})-{e.capitalize()}")
                        lineNo = lineNo + 1
                    lineBreak(0)
                    print(f"({(1+(len(player_inventory)))})-Exit")
                    lineBreak(0)
                    userInput = input(" ^ |--insert-number-->#")
                    for i in range(1,(1+(len(player_inventory)))):
                        if userInput == str(i):
                            player_current_hand = player_inventory[i-1]
                    x = []
                    for i in range(1,(1+(len(player_inventory)))):
                        x.append(str(i))
                    if userInput in x:
                        break
                    elif userInput == str(1+(len(player_inventory))):
                        break
                    else:
                        print("   |>>> INVALID <<<")
            elif userInput == "2":
                while True:
                    lineBreak()
                    print(f"   |WHICH ITEM WOULD YOU LIKE TO REMOVE")
                    lineNo = 1
                    for e in player_inventory:
                        print(f"({str(lineNo)})-{e.capitalize()}")
                        lineNo = lineNo + 1
                    print(f"({(1+(len(player_inventory)))})-Exit")
                    userInput = input(" ^ |--insert-number-->#")
                    for i in range(1,(1+(len(player_inventory)))):
                        if userInput == str(i):
                            player_inventory.remove(player_inventory[i-1])
                    x = []
                    for i in range(1,(1+(len(player_inventory)))):
                        x.append(str(i))
                    if userInput in x:
                        break
                    elif userInput == str(1+(len(player_inventory))):
                        break
                    else:
                        print("   |>>> INVALID <<<")
            elif userInput == "3":
                break
            else:
                print("   |>>> INVALID <<<")






















def location_info(mode = "menu"):
    if mode == "dict":
        lineBreak(2,1)
        print(f"{'location tiles'.capitalize()}\n")
        for tile in location_data:
            print(f"{tile.capitalize()}:\n{location_data[tile].capitalize()}.\n")
    else:
        while True:
            lineBreak()
            print(f"   |SELECT AN AVAILABLE TILE:")
            lineBreak(0)
            listz = list(location_data.keys())
            listz.append("exit")
            lineNo = 1
            # prints out possible tiles using for loops
            for e in listz:
                if e == "exit":
                    lineBreak(0)
                    print(f"({str(lineNo)})-{e.capitalize()}")
                    lineBreak(0)
                    continue
                print(f"({str(lineNo)})-{e.capitalize()}")
                lineNo = lineNo + 1
            userInput = input(" ^ |--insert-number-->#")
            for i in range(1,(len(listz))):
                if userInput == str(i):
                    print(f"   |{listz[(int(userInput))-1].capitalize()}:")
                    print(f"   |{location_data[listz[(int(userInput))-1]].capitalize()}.")
            x = []
            for i in range(1,6):
                x.append(str(i))
            if userInput in x:
                continue
            elif userInput == "6":
                break
            else:
                print("   |>>> INVALID <<<")










character_info("dict")
print("\n")
inventory_info("dict")
print("\n")
location_info("dict")











def menu(text = None):
    while True:
        lineBreak()
        print(f"   |{text}")
        lineBreak(0)
        # List and for loop to print available actions.
        listz = ["status", "inventory", "location", "quit"]
        lineNo = 1
        for e in listz:
            print(f"({str(lineNo)})-{e.capitalize()}")
            lineNo = lineNo + 1
        # Asks for the user's input.
        lineBreak(0)
        userInput = input(" ^ |--insert-number-->#")
        if userInput == "1":
            character_info()
        elif userInput == "2":
            inventory_info()
        elif userInput == "3":
            location_info()
        elif userInput == "4":
            print("   |You have quited!")
            lineBreak()
            print("\n\n\n")
            break
        else:
            print("   |>>> INVALID <<<")


# Function that entails the situation.
# Calls out to menu function passing the text parameter.


def situation1():
    situText = "PLAYER MENU"
    menu(situText)

situation1()  
sys.exit()