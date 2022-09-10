# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 21:51:00 2022

@author: JalenL
"""
import time
import random

Ingio_lost_list = ['Victory is fleeting. Losing is forever.','You have no choices about how you lose,' + 
                   'but you do have a choice about how you come back and prepare to win again.',
                   ' Losing is part of the game. If you never lose,' + 
                   ' you are never truly tested, and never forced to grow.',
                   'You beat me this time.....you won\'t be so lucky next time.']

random_lost = random.choice(Ingio_lost_list)

def play():
    
    score = 0
    
    print("\nRock...")
    time.sleep (3)
    print("\nPaper...")
    time.sleep (3)
    print("\nScissors...")
    time.sleep (3)
    print("\nShoot...")
    
    time.sleep (3)
    while True:   
        
        user = str(input("Enter: 'r' for Rock, 'p' for Paper, 's' for Scissors: ")).lower()
        
        Ingio = random.choice(['r','p', 's'])

        if user == Ingio:
            print("\nIt's a tie")
            print("\n---Greats minds do think alike---")
        
        elif is_win(user, Ingio):
            print("\nYou won!")
            print("\nIngio: ",random_lost)
            score += 1
            
            if score == 3:
                print("\n\n")
                print("\nYou may proceed on your adventure, you truly are a wonder.")
                break
            
        elif is_win != True:
            print("You lose!")
            print("\nWitness my true strength!")          

game = play

def is_win(user, Ingio):
    
    if (user == 'r' and Ingio == 's') or (user =='s' and Ingio== 'p') \
        or (user == 'p' and Ingio == 'r'):
            return True
    

def intro_choice():
    
    print("\nHello player, you've found my secert room. My name is Inigo Montoya and" 
          + " I'm the BEST Rock, Paper, Scissors player in the world, prepare to lose.")
    
    time.sleep(3)
    
    print("\nThese will be rapidfire games, be ready!")
    print("\n----Inigo holds out his hands eager to play------") 
   
    
    time.sleep(0)
    
    while True:     
            user_choice = input("Do you accept the duel? Y/N ").upper()
    
            if user_choice == "N":
                print("\nWell.... that's too bad you will play anyway!")
                return game()
            elif user_choice == "Y":
                print("\nThank you for humoring me....let's make this an epic battle...for me!")
                return game()
            else:
                print("\nInigo does not like that answer....try again")

intro_choice()
    








