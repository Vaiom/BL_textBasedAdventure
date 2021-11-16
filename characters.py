# Course: CS30 P1
# Name: Bryant Liu
# Date created: 2021-10-24
# Description: Stores character data to be imported into "main.py"
# ==============================================================
# YYYY-MM-DD / CHANGELOG (LATEST AT THE TOP)
# ==============================================================
# 2021-11-16 / Modified "characters.py" (this file)
# 2021-10-26 / Modified "characters.py" (this file)
# 2021-10-25 / Modified "characters.py" (this file)
# 2021-10-24 / Created "characters.py" (this file)
# ==============================================================

# Import statement.
try:
    from utility import *
except:
    raise Exception("Unable to import files.")

p_class = "rookie"  # Default class.


# Dictionary of all character classes.
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
    """States the players'current status."""
    global p_class
    # Sets title.
    title = "PLAYER INFO:"
    # Sets pre_text.
    pre = f"Current: {p_class}\n"
    # Prints user's current class specifications (added to pre_text).
    tag = {"health": " HP",
           "armor": "AMR",
           "stamina": "STA",
           "critical rate": " CR",
           "luck": " LK"
           }
    text = ""
    for value in dict_class[p_class]:
        if value == 'description':
            text = text + f"Description: {dict_class[p_class]['description'].capitalize()}.\nPerk: {dict_class[p_class]['bonus']}.\n"
        elif value == 'bonus':
            pass
        else:
            text = text + f"{tag[value]}-{dict_class[p_class][value]}\n"
    text = text[:-1]
    # Sets options.
    options = ["change class", "exit"]
    # Calls ft().
    input = ft(title=title, pre_text=pre + text, prompt=options)
    if input == "exit":
        return "main_menu", None
    return input, None


def menu_class_change():
    """Menu for changing player's class"""
    global p_class
    # Sets title.
    title = "PICK YOUR CLASS:"
    # Sets list of all available character classes.
    options = []
    for class_item in dict_class:
        options.append(class_item)
    options.append("exit")
    # Calls ft().
    input = ft(title=title, prompt=options)
    # Changes user's current class to the selected class if applicable.
    if input == "exit":
        return "status", None
    else:
        p_class = input
        return "status", "Class Changed!"


 

def menu_class_change():
    """Menu for changing player's class"""
    global p_class
    # Sets title.
    title = "PICK YOUR CLASS:"
    # Sets list of all available character classes.
    options = []
    for class_item in dict_class:
        options.append(class_item)
    options.append("exit")
    # Calls ft().
    input = ft(title=title,prompt=options)
    # Changes user's current class to the selected class if applicable.
    if input == "exit":
        return "status", None
    else:
        p_class = input
        return "status", "Class Changed!"

