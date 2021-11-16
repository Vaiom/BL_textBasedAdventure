# Course: CS30 P1
# Name: Bryant Liu
# Date created: 2021-10-24
# Description: Stores location data to be imported into "main.py"
# ==============================================================
# YYYY-MM-DD / CHANGELOG (LATEST AT THE TOP)
# ==============================================================
# 2021-11-16 / Modified "location.py" (this file)
# 2021-10-26 / Modified "location.py" (this file)
# 2021-10-25 / Modified "location.py" (this file)
# 2021-10-24 / Created "location.py" (this file)
# ==============================================================

# Import statement.
try:
    from utility import *
    import numpy as np
except:
    raise Exception("Unable to import files.")

# Dictionary of tiles and their description.
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


# Game map.
game_map = np.array([['boss', 'resources', 'enemy',
                      'resources', 'elite enemy'],
                     ['situation', 'elite enemy', 'situation',
                      'situation', 'enemy'],
                     ['enemy', 'situation', 'situation',
                      'situation', 'boss'],
                     ['situation', 'resources', 'situation',
                      'resources', 'situation'],
                     ['resources', 'elite enemy', 'enemy',
                      'elite enemy', 'boss']])

# tag dictionary to label the map.
tag = {'situation': 'ST',
       'resources': 'RT',
       'enemy': 'ET',
       'elite enemy': 'EET',
       'boss': 'BT'
       }


def menu_location(msg):
    """Navigates the "dict_location" dictionary."""
    # Sets title.
    title = "LOCATION:"
    # Sets pre_text.
    pre = []  # This is for printing the map.
    # Sets options.
    options = []
    for tile in dict_location:
        name = tile
        name = name[:-5]
        options.append(tile + f" ({tag[name]})")
    options.append("exit")
    options.append("MAP")
    # Calls ft().
    input = ft(title=title, prompt=options, pre_text=pre, reply=msg)
    # This is for interpreting the input from ft().
    try:
        ind = input.rindex(" ")
        input = input[:ind]
    except:
        pass
    # Prints description of the selected tile if applicable.
    if input == "exit":
        return "main_menu", None
    else:
        return "location", dict_location[input]

