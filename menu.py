# Course: CS30 P1
# Name: Bryant Liu
# Date created: 2021-10-24
# Description: Stores menu functions to be imported into main.py
# ==============================================================
# YYYY-MM-DD / CHANGELOG (LATEST AT THE TOP)
# ==============================================================
# 2021-11-16 / Modified "menu.py" (this file)
# 2021-10-26 / Modified "menu.py" (this file)
# 2021-10-25 / Modified "menu.py" (this file)
# 2021-10-24 / Created "menu.py" (this file)
# ==============================================================

# Import statement.
try:
    from utility import *
except:
    raise Exception("Unable to import files.")


def player_menu():
    """Manages input for the player's main menu"""
    # Sets title and options.
    title = "MAIN  MENU:"
    options = ["status", "inventory", "location", "quit"]
    # Calls ft().
    input = ft(title=title, prompt=options)
    return input, None

