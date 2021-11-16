# Course: CS30 P1
# Name: Bryant Liu
# Date created: 2021-10-24
# Description: Stores utility functions to be imported into "main.py"
# ==============================================================
# YYYY-MM-DD / CHANGELOG (LATEST AT THE TOP)
# ==============================================================
# 2021-11-16 / Modified "utility.py" (this file)
# 2021-10-26 / Modified "utility.py" (this file)
# 2021-10-25 / Modified "utility.py" (this file)
# 2021-10-24 / Created "utility.py" (this file)
# ==============================================================
# Add code to remember user's previous position for ft()
# Add an indent checker using '~' for lim()
# ==============================================================

# Import statements.
try:
    import sys
    import os
    import click
    import numpy as np
except:
    raise Exception("Unable to import files.")

# This is the max character length for the text UI.
# The variable is unused in this current version.
char_len = 39


def clear_console():
    """Clears the console for tidiness."""
    try:
        if os.name == "nt":
            os.system("clr")
        else:
            os.system("clear")
    except:
        click.clear()


def line(character="X", length=39):
    """Print lines to improve text UI readability."""
    text = ""
    for i in range(0, (length)):
        text += character
    return text


# This function is currently unused in this current version.
def lim(text, length=39):
    """
    Slices strings so that each line
    is underneath the character limit.
    """
    # If given text is a string.
    if type(text) == str:
        # If string is underneath character limit, return the string.
        if len(text) <= length:
            return text
        # If string does not contain spaces.
        elif " " not in text or text.find(" ") >= length:
            raise Exception("Not Splitable")
        # Convert the string to a list.
        else:
            text = [text]
            master = text
    # If given text is a list.
    elif type(text) == list:
        # Stores text as a new list to be modified.
        master = text
        # Checks if last string is underneath character limit.
        if len(text[-1]) <= length:
            x = "\n".join(text)
            return x
    # The line below is for checking indents (unavailable).
    # temp = text[0]
    # Left half of string.
    left = text[-1]
    # Right half of string.
    right = text[-1]
    # Shortens left string to length and most right ' '.
    left = left[:length]
    ind = left.rfind(" ")
    # Shortens left string to ' '.
    left = left[:ind]
    # Expands right string to ' '.
    right = right[ind+1:]
    # Adds the two spliced strings to the list.
    master.pop()
    master.append(left)
    master.append(right)
    # Recursion until desired result is reached.
    return (lim(master, length))


def ft(title, prompt,
       pre_text=None,
       post_text=None,
       reply=None,
       length=39):
    """Formats text, ensures lines are within character limit."""
    # line_data keys prompt with True and False values
    # to determine which lines are highlighted.
    # user_position references to line_data by index.
    line_data = {}
    user_position = 0

    def navigator(direction, user_position):
        """Logic that fixates the user_position."""
        # Adjusts user_position accordingly to direction.
        if direction == "up":
            user_position -= 1
        elif direction == "down":
            user_position += 1
        index_count = -1
        # Corrects user_position if out of range.
        for counter in line_data:
            index_count += 1
        if user_position < 0:
            user_position = index_count
        elif user_position > index_count:
            user_position = 0
        # Returns value.
        return user_position

    def show(txt, color='white', length=39):
        """Combines click.secho() and lim()"""
        # lim() currently unavailable.
        # click.secho(lim(txt,length),fg = color)
        click.secho(txt, fg=color)

    if type(prompt) == list:
        while True:
            for item in prompt:
                line_data.update({item: False})
            line_data.update({prompt[user_position]: True})
            clear_console()
            # Print title
            show(line("="), 'magenta')
            show(title, 'blue')
            show(line("-"), 'magenta')
            # Prints pre_text when necessary.
            if pre_text != None:
                if type(pre_text) == list:
                    for printable in pre_text:
                        if printable == None or printable == "":
                            continue
                        show(printable, 'blue')
                        show(line("-"), 'magenta')
                else:
                    if pre_text != None and pre_text != "":
                        show(pre_text, 'blue')
                        show(line("-"), 'magenta')
            # Prints the map.
            if prompt[-1] == "MAP":
                line_data.pop("MAP")
                show(map_print(line_data))
                show(line("-"), 'magenta')
                show("SELECT A TILE:", 'blue')
                show(line("-"), 'magenta')
            # Highlights the selected line.
            for item in line_data:
                if line_data[item] == True:
                    show("> |" + item, 'bright_yellow')
                else:
                    show("  |" + item)
            # Prints post_text when necessary.
            if post_text != None:
                show(line("-"), 'magenta')
                show(post_text, 'blue')
            show(line("-"), 'magenta')
            # Prints user controls.
            show("Press W or S to move Up or Down", 'blue')
            show("Press SPACE to confirm", 'blue')
            show(line("-"), 'magenta')
            # Prints reply when necessary.
            if reply != None:
                show(reply, 'green')
            # Collects character pressed on keyboard.
            user_input = click.getchar()
            # Navigates through the menu accordingly to user_input.
            if user_input.lower() in ['w']:
                user_position = navigator("up", user_position)
            elif user_input.lower() in ['s']:
                user_position = navigator("down", user_position)
            elif user_input.lower() in [' ']:
                return prompt[user_position]
    else:
        pass

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


def map_print(highlight=None):
    """Prints out the game map."""
    master = ""
    if highlight == None:
        # Prints the map in white.
        master += "+ --- + --- + --- + --- + --- +\n"
        for x in game_map:
            for y in x:
                master += "|"
                master += f"{tag[y].center(5)}"
            master += "|\n"
            master += "+ --- + --- + --- + --- + --- +\n"
        master = master[:-1]
        return master
    else:
        # For use in ft().
        master += click.style("+ --- + --- + --- + --- + --- +\n", 'blue')
        for x in game_map:
            for y in x:
                master += click.style("|", 'blue')
                if highlight[y + " tile" + f" ({tag[y]})"] == True:
                    master += click.style(f"{tag[y].center(5)}",
                                           'bright_yellow')
                else:
                    master += click.style(f"{tag[y].center(5)}", 'blue')
            master += click.style("|\n", 'blue')
            master += click.style("+ --- + --- + --- + --- + --- +\n", 'blue')
        master = master[:-5]
        return master

