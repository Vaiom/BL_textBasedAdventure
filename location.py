# Course: CS30 P1
# Name: Bryant Liu
# Date created: 2021-10-24
# Description: Stores location data to be imported into "main.py"
# ==============================================================

from click import style


class Tile:
    def __init__(self, name, tag, text, hide=False):
        self.name = name
        self.tag = tag
        self.text = text
        self.hide = hide

    def t(self):
        if self.hide is False:
            return self.tag
        else:
            return " "

# Create Tiles
X1 = Tile("Boundary", "X", "You can't go here!")
J1 = Tile("Space", " ", "Empty here.")
S1 = Tile("Start", "BEG", "You start here!")
E1 = Tile("End", "END", "You Win!")


class lootroom(Tile):
    def __init__(self, name, tag, text, loot, looted=False):
        super().__init__(name, tag, text, hide=False)
        self.loot = loot
        self.looted = looted

    def get_loot(self, p1):
        if self.looted is False:
            p1.add_inv("key")
            self.looted = True
            return 0
        else:
            return 1

# Special Tiles
C1 = lootroom("Loot", "CHT", "You found", "key")

V1 = Tile("Door", "O", "To go through this door, you will need a key!")

game_map = [[X1.t(), X1.t(), X1.t(), X1.t(),
             X1.t()], [X1.t(), J1.t(), J1.t(),
                       E1.t(),
                       X1.t()], [X1.t(),
                                 V1.t(),
                                 X1.t(),
                                 X1.t(),
                                 X1.t()],
            [X1.t(), J1.t(), J1.t(), C1.t(),
             X1.t()], [X1.t(), J1.t(), X1.t(),
                       X1.t(), X1.t()],
            [X1.t(), S1.t(), X1.t(), X1.t(),
             X1.t()], [X1.t(), X1.t(), X1.t(),
                       X1.t(), X1.t()]]


class Map:
    """Blueprint for the Map"""
    def __init__(self, map):
        self.map = map

    def map_move(self, obj, direction):
        if direction in ('a'):
            return 'x', -1
        elif direction in ('d'):
            return 'x', 1
        elif direction in ('w'):
            return 'y', -1
        elif direction in ('s'):
            return 'y', 1

    def map_check(self, plane, value, cur_x, cur_y, inv, p1):
        if self.map[cur_y][cur_x] == "X":
            return True, plane, -1 * value, None
        if self.map[cur_y][cur_x] == "END":
            return "win", plane, value, None
        if self.map[cur_y][cur_x] == "CHT":
            return "loot", plane, value, None
        if self.map[cur_y][cur_x] == "O":
            if "key" in inv:
                V1.hide = True
                self.map = self.map
                p1.rem_inv("key")
                return False, plane, value, None
            return True, plane, -1 * value, "door"
        else:
            return False, plane, value, None

    def show_map(self, cur_cor):
        """Prints out the game map."""
        master = ""
        master += style("+ --- + --- + --- + --- + --- +\n", 'white')
        for y in range(0, len(self.map)):
            for x in range(0, len(self.map[y])):
                master += style("|", 'white')
                if (x, y) == cur_cor:
                    master += style(f"{'*'.center(5)}", 'bright_yellow')
                else:
                    if self.map[y][x] == X1.t():
                        master += style(f"{'XXX'.center(5)}", 'red')
                    else:
                        if self.map[y][x] == C1.t():
                            master += style("     ", 'blue')
                            continue
                        master += style(f"{self.map[y][x].center(5)}", 'blue')
            master += style("|\n", 'white')
            master += style("+ --- + --- + --- + --- + --- +\n", 'white')
        master = master[:-5]
        return master
