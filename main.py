# Course: CS30 P1
# Name: Bryant Liu
# Date created: 2021-10-24
# Description: Main python code for RPG (core logic)
# ==============================================================
# YYYY-MM-DD / CHANGELOG (LATEST AT THE TOP)
# ==============================================================
# 2021-11-16 / Modified "main.py" (this file)
# 2021-10-26 / Modified "main.py" (this file)
# 2021-10-25 / Modified "main.py" (this file)
# 2021-10-24 / Created "main.py" (this file)
# ==============================================================

# Import modules/files.
try:
    import sys
    import click
    import numpy as np
    from utility import *
    from menu import *
    from characters import *
    from inventory import *
    from location import *
    print("Succesfully imported files!")
    # Requires the user to type and ENTER 'continue' to proceed.
    while True:
        userInput = input("Type 'continue' then press ENTER to proceed: ")
        try:
            if userInput == "continue":
                break
            else:
                raise Exception()
        except:
            print("<<< INVALID >>>")

# Force quits the game upon import failure.
except:
    print("Unable to import files.")
    print("Exit Complete!")
    sys.exit()

# Defined variables that support program functionality.
z = "main_menu"
msg = None

# The variable 'z' dictates program flow.
while z != "0":
    if z == "main_menu":
        z, msg = player_menu()
    elif z == "status":
        z, msg = menu_class()
    elif z == "change class":
        z, msg = menu_class_change()
    elif z == "inventory":
        z, msg = menu_inventory()
    elif z == "change equipped item":
        z, msg = inventory_equip()
    elif z == "remove item from inventory":
        z, msg = inventory_remove()
    elif z == "location":
        z, msg = menu_location(msg)
    elif z == "quit":
        z = "0"  # Basically break.
    else:
        raise Exception("INVALID z")

# Exit code.
clear_console()
click.secho("Exit Complete!", fg='green')
sys.exit()
