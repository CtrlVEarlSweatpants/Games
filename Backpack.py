#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Created on: March 1, 2020
@Author: TDBowman
@Course: INF 6050 Introduction to Computer Programming 
@University: Wayne State University 
@Assignment: Homework 2

@Python version: 3.8x
@Required Modules: time

@Description: Create a guessing game using dictionaries/lists
"""
###################################
# import some modules
###################################
import time # time module for waiting
import json

###################################
# Set up global vars for use
###################################
test = False
 # empty list
players = [] 
 # can be set to anything greater than 1
num_items = 3
# only works with 2 players as is
num_players = 2 
# number of guesses each player gets
num_guesses = 3

###################################
# define some functions
###################################
# print new line (default = 1)
def print_newLine(num=1):
    """ Create x number of line breaks """
    print("\n"*int(num))

# print line of asteriscs (default = 78))
def print_line(num=50):
    """ Create x number of asterics """
    print("*"*int(num))

# sleep -- pause play for a moment (default = 1)
def sleep(amount=1):
    """ Sleep x number of seconds """
    time.sleep(amount)

# print out instructions for game
def print_instructions(test, num_items, num_guesses):
    """ Print out instructions """

    print_line(50)
    print("Welcome to the great game of guessing!\n \
Each player will get to create a catalog\n \
containing {} items with 3 pieces of metadata".format(num_items))
    print_newLine()
    print("You will have {} guesses to guess an item \n \
from the other person's catalog.".format(num_guesses))
    
    print("NOTE: *** You can quit at any time by typing 'QUIT' ***")
    print_newLine()
    print("Have fun!")
    print_line()
    sleep(2)
    print_newLine()

# create users for game 
# I can set variables determining how many players and items and pass them 
# to this function! It allows me to change it up at any point. 
# NOTE: I've set the variables from line 14 to line 23
def create_users(test, players, num_players, num_items):
    """ Gather data for each user in game """

    # Run loop to create each player (as defined by variable num_players).
    for profile in range(num_players):       
    
        print_newLine()
        print_line(50)
        
        # Tell player(s) to cover their eyes
        if num_players > 2:
            print("All players other than the current player, please COVER\
                  YOUR EYES!")           
            print_line(50)
            
        else:
            if profile == 0:
                cover_eyes = 2
            else:
                cover_eyes = 1
        
            print("COVER YOUR EYES, PLAYER {}".format(cover_eyes))
            print_line(50)
        
        sleep(1)

        # Adds dictionary of placeholders to 'players' list
        players.append({   
     	"name": "",     # <-- placeholder for storing name of each player  
        "city": "",     # <-- placeholder for storing city of each player  
        "age": None,      # <-- placeholder for storing age of each player  
		"score": 0,     # <-- starts at 0
        "guesses": 0,     # <-- starts at 0
		"collection": []  # <-- empty nested list for collection items
     	})
        
        with open('Players.json', 'w') as f:
            json.dump(players, f)
        
        
        # Ask for name
        print_newLine(3)
        new_name = input("Enter name for player {}: "
               .format(profile + 1))
        
        # Check for "QUIT"
        if new_name.upper() == "QUIT":
            print_newLine(3)
            print_line()
            print("We hate to see you go!")
            return
        
        else:
            players[profile]["name"] = new_name
        
        # Ask for city
        new_city = input("Enter city for player {}: "
               .format(profile + 1))
        
        # Check for "QUIT"
        if new_city.upper() == "QUIT":
            print_newLine(3)
            print_line()
            print("We hate to see you go!")
            return
        
        else:
            players[profile]["city"] = new_city        
   
        # Ask for age
        while True:
            try:
                new_age = input("Enter age for player {}: "
                       .format(profile + 1))
                
                # Check for "QUIT"
                if new_age.upper() == "QUIT":
                    print_newLine(3)
                    print_line()
                    print("We hate to see you go!")
                    return
                
                else:
                    new_age = int(new_age)
                    players[profile]["age"] = new_city  
                    break
        
            except:
                print("Please enter an appropriate age.")
        
            
        
        #########################################
        # Ask for n number (as defined by variable num_items) of items
        print("Enter {} items to put into your collection.".format(num_items))
        
        # Loop through and ask for items / metadata
        for item in range(num_items):
            
            # allows the display of 1 - 3 instead of 0 - 2
            item = item + 1 
            
            # Ask for items/metadata
            collection_title = input("\tItem "+str(item)+" Title: ")
            # CHECK FOR QUIT
            if (collection_title.upper() == "QUIT"):
                print_newLine(3)
                print_line()
                print("We hate to see you go!")
                return
            
            while True:
                try:
                    collection_year = input("\tItem "+str(item)+" Year: ")
                    # CHECK FOR QUIT
                    if (collection_year.upper() == "QUIT"):
                        print_newLine(3)
                        print_line()
                        print("We hate to see you go!")
                        return
                        
                    
                    collection_year = int(collection_year)
                    break
                except:
                    print("Please enter a year")
            
            collection_location = input("\tItem "+str(item)+" Location: ")
            # CHECK FOR QUIT
            if (collection_location.upper() == "QUIT"):
                print_newLine(3)
                print_line()
                print("We hate to see you go!")
                return
            
            collection_type = input("\tItem "+str(item)+" Type: ")
            # CHECK FOR QUIT
            if (collection_type.upper() == "QUIT"):
                print_newLine(3)
                print_line()
                print("We hate to see you go!")
                return
        
            # Add items as dictionary into list using append()
            players[profile]["collection"].append({
                "title": collection_title, 
                "collection": collection_year, 
                "location": collection_location, 
                "type": collection_type})
        
        with open('Players.json', 'w') as f:
            json.dump(players[profile]['collection'], f)
            
            
        sleep(0)
        print_newLine(3)
        print_line()

        # For testing
        if test:    
            print(players[profile]['collection'])
        
    return True


def guessAnnouncement():
    """ Guessing Time announcement """
    print_newLine()
    print_line(50)
    print("! GUESSING TIME !")
    print_line(50)
    print_newLine()


# ask players to guess 
def askGuesses(test, players, num_players, num_items, num_guesses):
    """ The guessing portion of the game """

    sleep(1)
    
    for player in range(num_players):

        
        # Get player's ids
        other_player = (player+1) % 2
        
                
        name_current = players[player]["name"]
        name_other = players[other_player]["name"]
        loops = num_guesses + 1

        for i in range(1, loops):
            print_line()
            print_newLine()
            
            
            # Ask for guesses        
            player_guess = input("\n{}, you have {} guesses to guess \
one item from {}'s collection: ".format(name_current, loops-1, name_other))

            if player_guess.upper() == "QUIT":
                print_newLine(3)
                print_line()
                print("We hate to see you go!")
                return
        
        
            # Search for guess in dictionary entries in other player's items
            for k, dictionary in enumerate(players[other_player]['collection']):
                # This is a dictionary, so I need to loop through
                for key,val in dictionary.items():
                    if key == "title" and val.lower() == player_guess.lower():
                        flag = True
                        players[player]["score"] += 1
                        players[player]["guesses"] += 1
                        item = players[other_player]['collection'][k]
                        break
                        
                    else:
                        flag = False
                
                if flag:
                    break

            if flag == True:
                print("You are correct, {}. Way to go!\
\nYou guessed it in {} trys.".format(name_current, i))
                print_newLine()
                print("Here is the complete record for that item:")
                
                for key, val in item.items():
                    print("\t", key.upper(), " : ", val)
                
                print_newLine()
                break
            else:
                players[player]["guesses"] += 1
                print("Sorry, {}. You are incorrect.".format(name_current))
                
                
            #loops -= 1
            
    return True

# end the game         
def finish_game(players):
    """ Ending of game """
    print_line()
    print_newLine(4)
    print("FINAL RESULTS ARE: \n")
    for player in players:
        print("\t" + player["name"] + " score: " + str(player["score"])
        + " out of " + str(player["guesses"]))
    print_newLine(4)
    print_line()


###################################
# run the functions
###################################
if __name__ == "__main__":
    print_newLine(3)
    print_instructions(test, num_items, num_guesses) # run function
    result = create_users(test, players, num_players, num_items) # run function

    if result != None:
        print_newLine(3)
        print_line()
        result = askGuesses(test, players, num_players, num_items, num_guesses)
        if result:
            finish_game(players)
    
    else:
        finish_game(players)