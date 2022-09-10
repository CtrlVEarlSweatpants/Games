# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 19:06:15 2022

@author: JalenL
"""

import time


def intro():
    
    print("\n----- Welcome to the Cave of Wonders!-----")
    print("\nHello player, my name is Socrates.... you might've heard of me. I wont to test your riddle skills.")
    
    time.sleep(3)
    
    while True:    
            
            user_choice = input("Do you accept the riddle challenge? Y/N ").upper()
    
            if user_choice == "N":
                print("\n\nWell.... that's too bad, you will try to solve the riddle anyway!")
                return riddle_game()
            elif user_choice == "Y":
                print("\n\nThank you for humoring me!")
                return riddle_game()
            else:
                print("\nSocrates does not like that answer....try again")


def riddle_game():

    guess = 0
    
    while True:
        
        time.sleep(3)
        
        print("\n\n")
        print("\nI have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?")
        print("\n\nType your guess, or type 'Help1', 'Help2', or 'I give up' below: ")
        
        answer = input()
        guess +=1
            
        if answer.capitalize() == "Map":
             print("\nCongrats! You got it!")
             break
        if answer.capitalize() == "Help1":
            print("\n\nA modern version of this came out 500 years ago.")
            guess -=1
        elif answer.capitalize() == "Help2":
            print("\n\nMakers of this item use fake places to catch forgers.")
            guess -=1
        else:
          print("Wrong....Try Again!")
          
intro()