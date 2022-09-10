# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 18:25:07 2022

@author: JalenL
"""

import time

def intro_2():
    
    print("\n----- Welcome to the Cave of Wonder !-----")
    print("\nHello player, my name is Aristotle..... you might've heard of me."+
          " I want to test your riddle skills.")
    
    time.sleep(3)
    
    while True:    
            
            user_choice = input("Do you accept the riddle challenge?"+
                                " (Y/N): ").upper()
    
            if user_choice == "N":
                print("\n\nWell.... that's too bad, you will try to solve the" 
                      + " riddle anyway!")
                return riddle_game_2()
            elif user_choice == "Y":
                print("\n\nThank you for humoring me!")
                return riddle_game_2()
            else:
                print("\nAristotle does not like that answer....try again")


def riddle_game_2():

    guess = 0
    
    while True:
        
        time.sleep(3)
        
        print("\n")
        print("\nWhat they couldn't catch, they kept; what they caught,"+
              " they got rid of?.")
        print("\nType your guess, or type 'Help1', 'Help2' below: ")
        
        answer = input()
        guess +=1
            
        if answer.capitalize() == "Fleas":
            print("\nCongrats! You got it!")
            break
        elif answer.capitalize() == "Help1":
            print("\nThese are infamous for transmitting the Black Death"+
                  " plaque.")
            guess -=1
        elif answer.capitalize() == "Help2":
            print("\nThey are tiny vampires!")
            guess -=1
        else:
            print("\nWrong....Try Again!")

intro_2()