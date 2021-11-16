# Course: CS30 P1
# Name: Bryant Liu
# Date created: 2021-10-24
# Description: Stores inventory data to be imported into "main.py"
# ==============================================================
# YYYY-MM-DD / CHANGELOG (LATEST AT THE TOP)
# ==============================================================
# 2021-11-16 / Modified "inventory.py" (this file)
# 2021-10-26 / Modified "inventory.py" (this file)
# 2021-10-25 / Modified "inventory.py" (this file)
# 2021-10-24 / Created "inventory.py" (this file)
# ==============================================================

# Import statement.
try:
    from utility import *
except:
    raise Exception("Unable to import files.")


# Dictionary of all items.
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
                            "description":
                            "used to treat minor injuries",
                            "type": "miscellaneous",
                            "heal": 20,
                            "stamina drain": 0}
            }

# Variables relating to user's inventory/held item.
p_hand = "None"
p_inventory = list(dict_inv.keys())


def menu_inventory():
    """
    Navigates the "dict_inv" dictionary.
    Allows user to change equipped item,
    and remove items from their inventory.
    """
    global p_hand
    global p_inventory
    # Incase user decides to remove an equipped item.
    if p_hand not in p_inventory:
        p_hand = "None"
    available_inventory = ""
    # Sets title.
    title = "YOUR INVENTORY:"
    # Sets all the available items in the player's inventory.
    if p_inventory != []:
        for item in p_inventory:
            available_inventory = available_inventory + f"-{item.capitalize()}\n"
        available_inventory = available_inventory[:-1]
    else:
        available_inventory = "No items avaiable"
    # Sets user's current hand and specifications if applicable.
    equipped_item = f"Equipped: {p_hand.capitalize()}"
    equipped_info = ""
    if p_hand != "None":
        equipped_info += f"Description: {dict_inv[p_hand]['description']}\n"
        for specs in dict_inv[p_hand]:
            if specs == "description":
                continue
            else:
                equipped_info = equipped_info + f"{specs.capitalize()}-{dict_inv[p_hand][specs]}\n"
        equipped_info = equipped_info[:-1]
    pre = [available_inventory, equipped_item, equipped_info]
    # Sets options.
    options = ["changed equipped item", "remove item from inventory", "exit"]
    # Calls ft().
    input = ft(title=title, pre_text=pre, prompt=options)
    # Logic for handling input.
    if input == "exit":
        return "main_menu", None
    elif input[0:1] == "c":
        return "change equipped item", None
    elif input[0:1] == "r":
        return "remove item from inventory", None


def inventory_equip():
    """Manages inventory to equip items."""
    global p_hand
    global p_inventory
    # Sets title.
    title = f"WHICH ITEM TO BE EQUIPPED:"
    # Sets all available items to equip.
    equipped_item = f"Equipped: {p_hand.capitalize()}"
    available_inventory = ""
    if p_inventory == []:
        available_inventory = "No items avaiable"
    pre = [equipped_item, available_inventory]
    # Sets options.
    options = []
    for item in p_inventory:
        options.append(item)
    options.append("exit")
    # Calls ft().
    input = ft(title=title, prompt=options, pre_text=pre)
    # Equips the selected item if applicable.
    if input == "exit":
        return "inventory", None
    else:
        p_hand = input
        return "inventory", None


def inventory_remove():
    """Manages inventory to remove items."""
    global p_hand
    global p_inventory
    # Sets title.
    title = "WHICH ITEM TO BE REMOVED:"
    # Sets a list of removable items in the user's inventory.
    available_inventory = ""
    if p_inventory == []:
        available_inventory = "No items avaiable"
    # Sets options.
    options = []
    for item in p_inventory:
        options.append(item)
    options.append("exit")
    # Calls ft().
    input = ft(title=title, prompt=options, pre_text=available_inventory)
    # Removes the selected item if applicable.
    if input == "exit":
        return "inventory", None
    else:
        p_inventory.remove(input)
        return "inventory", None

