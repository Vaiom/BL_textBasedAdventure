# Course: CS30 P1
# Name: Bryant Liu
# Date created: 2021-10-24
# Description: Main python code for RPG (core logic)
# ==============================================================

# Import modules/components.
try:
    import sys
    import os
    import numpy as np
    from click import *
    from time import sleep
    from characters import *
    from inventory import *
    from location import *
    print("Succesfully imported files!")
except:
    print("There was en error!")
    raise Exception()


def wipe():
    """Clears the console for tidiness."""
    try:
        if os.name == "nt":
            os.system("clr")
        else:
            os.system("clear")
    except:
        clear()


def ft(title="Title",
       map=None,
       prompt=("inventory", "help", "exit"),
       pre_text=None,
       post_text=None,
       reply=None,
       key=False,
       inpute=True,
       any=False):
    """Formats the user interface."""
    # Variables to store ui data
    index_count = -1
    for counter in prompt:
        index_count += 1
    lineS = '--------------------------------------'
    user_position = p1.get_upos()

    # Top fixed text.
    top = []
    top.append(style(lineS, 'magenta'))
    top.append(style(title, 'blue'))
    top.append(style(lineS, 'magenta'))
    top = "\n".join(top)

    # Top bottom text.
    bottom = []
    if map is not None:
        bottom.append(style("Use WASD to move your character", 'blue'))
    if any is False:
        bottom.append(style("Press R or F to select options", 'blue'))
        bottom.append(style("Press E to confirm", 'blue'))
        bottom.append(style(lineS, 'magenta'))
        bottom = "\n".join(bottom)

    # Prints the changable menu.
    wipe()
    print(top)
    if map is not None:
        print(map)
    # Prints pre_text when necessary.
    if pre_text is not None:
        if type(pre_text) == list or type(pre_text) == tuple:
            for printable in pre_text:
                if printable is None or printable == "":
                    continue
                secho(printable, 'blue')
                secho(lineS, 'magenta')
        else:
            if pre_text is not None and pre_text != "":
                print(style(pre_text, 'blue'))
                print(style(lineS, 'magenta'))
    # Highlights the selected line.
    if any is False:
        for item in prompt:
            if prompt.index(item) == user_position:
                secho("> |" + item, fg='bright_yellow')
            else:
                print(style("  |" + item, 'blue'))
    # Prints post_text when necessary.
    if post_text is not None:
        if type(post_text) == list or type(post_text) == tuple:
            for printable in post_text:
                if printable is None or printable == "":
                    continue
                secho(printable, 'blue')
                secho(lineS, 'magenta')
        else:
            if post_text is not None and post_text != "":
                print(style(post_text, 'blue'))
    secho(lineS, fg='magenta')
    if any is False:
        print(bottom)
    # Prints reply when necessary.
    if reply is not None:
        secho(reply, fg='green')
    # Collects character pressed on keyboard.
    if inpute is True:
        acti = getchar()
    else:
        acti = ""
    # Navigates through the menu accordingly to user_input.
    if map is not None:
        if acti in ('w', 'a', 's', 'd'):
            plane, count = m1.map_move(p1, acti)

            p1.cha_cor(plane, count)
            coordinate = p1.get_cor()
            x_cor = coordinate[0]
            y_cor = coordinate[1]
            test, plane, count, lop = m1.map_check(plane, count, x_cor, y_cor,
                                                   p1.get_inv(), p1)
            if test is True:
                if lop == "door":
                    p1.cha_cor(plane, count)
                    return "meu", V1.text
                p1.cha_cor(plane, count)
                return "menu", X1.text
            if test == "win":
                p1.set_cor(3, 1)
                return "win", None
            if test == "loot":
                y = C1.get_loot(p1)
                if y == 0:
                    return "menu", "You found a key!"
                else:
                    return "menu", None
            return "menu", None
    # Manages scroll input from user.
    if acti in ('r'):
        user_position -= 1
        if user_position < 0:
            user_position = index_count
        p1.cha_upos(user_position)
        return "menu", None
    elif acti in ('f'):
        user_position += 1
        if user_position > index_count:
            user_position = 0
        p1.cha_upos(user_position)
        return "menu", None
    elif acti in ('e'):
        return prompt[user_position], None
    else:
        return None, None


# Setup lines.
pause(info="Press any key to proceed.")
wipe()
m1 = Map(game_map)
p1 = user()
p1.enter_uname(wipe)
z = "menu"
message = None


def exit_menu():
    """Confirms exit with user."""
    p1.cha_upos(0)
    while 1:
        wipe()
        acti, message = ft(title="EXIT MENU:",
                           pre_text="Are you sure you want to quit?" +
                           "\nYOUR PROGRESS WILL BE LOST",
                           prompt=("no", "yes"))
        if acti in ('no', 'yes'):
            break
        else:
            continue
    if acti == "no":
        return "menu"
    elif acti == "yes":
        wipe()
        print("Exit Complete!")
        sys.exit()


def help_menu(name):
    """Shows text to help user."""
    a = f"""Using WASD controls, move your
character to the end tile!.
You may encounter a door
in which you will need to
find a key to unlock it!
Good Luck {name}!"""
    ft(title="HELP MENU:",
       pre_text=a,
       post_text="PRESS ANY KEY TO PROCEED",
       inpute=False,
       any=True)
    pause(" ")
    p1.cha_upos(0)


# Core Logic of game.
while 1:
    if z == "menu":
        z, message = ft(f"MENU: {p1.get_name()}",
                        m1.show_map(p1.get_cor()),
                        reply=message)
        if z == "inventory":
            z = "menu"
            message = get_inv(p1.get_inv())
        elif z == "help":
            z = "help"
        elif z == "exit":
            z = "exit"
        elif z == "win":
            z = "win"
        else:
            z = "menu"
    elif z == "win":
        message = f"You win! {p1.get_name()}"
        ft(f"MENU: {p1.get_name()}",
           m1.show_map(p1.get_cor()),
           reply=message,
           inpute=False)
        sys.exit()
        break
    elif z == "exit":
        z = exit_menu()
    elif z == "help":
        help_menu(p1.get_name())
        z = "menu"
