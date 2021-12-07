# Course: CS30 P1
# Name: Bryant Liu
# Date created: 2021-10-24
# Description: Stores character data to be imported into "main.py"
# ==============================================================


class user:
    """Stores/Manages data related to the user"""
    def __init__(self, name=None, inventory=[], x=1, y=5, user_pos=0):
        self.name = name
        self.inv = inventory
        self.x = x
        self.y = y
        self.user_pos = user_pos

    def enter_uname(self, wipe):
        while 1:
            abc = input("What is your name? ")
            if abc.isalnum() is True:
                self.name = abc
                break
            else:
                wipe()
                print("Invalid characters.")

    def get_name(self):
        return self.name

    def get_inv(self):
        return self.inv

    def add_inv(self, item):
        self.inv.append(item)

    def rem_inv(self, item):
        self.inv.remove(item)

    def get_cor(self):
        return (self.x, self.y)

    def cha_cor(self, plane, value):
        if value not in (-1, 1):
            raise Exception("Invalid Value (cha_cor)")
        if plane == "x":
            self.x += value
        elif plane == "y":
            self.y += value

    def set_cor(self, x, y):
        self.x = x
        self.y = y

    def get_upos(self):
        return self.user_pos

    def cha_upos(self, value):
        self.user_pos = value
