#---------------------------------------------------
# Python Pseudocode - Text-Based Adventure Game
# Bryant Liu
# September 21, 2021
#---------------------------------------------------

# Goals:
# - 7 endings
# - include a system that can increase/decrease the likelihood of a specific situation(s) happening, based on your choices in the story.

"""
Main Story:
You and a crewmate are stranded on a unknown alien spaceship.
You and your crewmate decided to split off.
Your objective is to find any means escaping the spaceship.
"""

##########################################################################################################
# Main function of the game (in pseudocode). (As of September 21th, 2021)
# EVERYTHING IS SUBJECT TO CHANGE
##########################################################################################################

# Have a varible that stores the player's health (you instantly lose once the hp reaches 0)
// hp = 5 (default is 5)

# Have a variable that stores the player's stamina(energy) (used for performing certain actions)
// energy = 100 (max is 100, lowest is 0) 

# Have a list that stores objects/items into the user's inventory
// user_inventory = (...) (there will be a weight limit of 30)

# Have a dictionary that stores items with respective values (everything will have some weight, weapons with their damage values, or restoration items with their heal/energy values)
// item_data = {...}



# Have a variable that counts the player's progress (amount of situations they have encountered)
// tally = 0 (default)

# Have a coefficent whos values varies from 0.75 - 1.5
// cofactor = random number between (.75-1.5) (HP will influence the minimum/maximum of the coefficient)

# Have a variable that acounts for "tally" and "cofactor", producing a value that will dictate the flow of the program (what sitatuation the player encounters)
# The higher the risk number, the more dangerous situations the player will face
// risk = randomized value (between 0 + (3 + counter)) * cofactor
# This will be a function

# Have a variable that controls the flow of the program (specifically the loop block)
// omega = 0




# This function creates the text UI for the player
# It takes in parameters and adjusts the user options accordingly
//menu(a,b,c):
//if a = ?:
//  ...
//elif b = ?:
//  ...
//elif c = ?:
//  ...
//else:
//  repeat menu
# Will return a value for the situation#() function to interpret





# There will be a function for each sitatuation
# The basic layout is as follows
//situation#():
//  a = ...
//  b = ...
//  c = ...
//  menu(a,b,c)
//  ...
//  ...
# These lines of codes will adjust hp, energy, user_inventory, and or tally

# Some situations will involve choices where it is restricted by your energy, or an item from user_inventory
# The last few highest numbered situations will be the ones leading to endings 






# While loop block that controls execution flow
# Risk values varies from 0 to ?
# Will execute a specific situation (functions)

// while omega != None:

//  if risk <1:
//    situation #()
//  elif risk <2:
//    situation #()
//  elif y <3:
//    situation #()
//  ...
//  ...
//  ...
//  ...
//  ...
//  ...
//  elif y <10:
//    situation #()
//  else:
//    situation #()



# Once out of loop
// exit()