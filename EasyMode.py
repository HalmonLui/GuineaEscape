'''
Created on January 15th, 2017

@author: luih
'''
#Importing modules
from random import randint
global days
global dayacts
global hunger
global thirst

#Introduction
def welcome():
    print ("Psst! Hey, new neighbor! Welcome to Nom's Pet Store!")
    print ("We've all been trying to escape this place for the longest time.")
    print ("Maybe you'll be the one to finally do it!")
    print ("Since you're a guinea pig, you have 30 days to escape before you get relocated.")
    print ("Good Luck!")
    dayacts = 5;
    day()

#Menu for Day Time
def day():
    while (dayacts > 0):
        print ("You have %d actions left before night time." %dayacts)
        print ("1)Eat\n2)Drink\n3)Sleep\n4)Chew\n5)Act Cute")
        action = input("#: ")
        try:
            action = int(action)
        except ValueError:
            print("Please enter a number")
            day()
        if action == 1:
            eat()
        elif action == 2:
            drink()
        elif action == 3:
            sleep()
        elif action == 4:
            chew()
        elif action == 5:
            actcute()
        else:
            print("That is not a viable action!")
            day()
    hunger=hunger+1
    thirst=thirst+1
    dead()
    print ("After day %d, your hunger is %d/10 and thirst is %d/5" % days,hunger,thirst)
        
            
#Eating Action            
def eat():
    print ("What should I eat?")
    print ("1)Hay\n2)Pellets")
    eat = input("#: ")
    try:
        eat = int(eat)
    except ValueError:
        print("Please enter a number")
        eat()
    if eat == 1:
        if hunger >= 1:
            hunger=hunger-1
        else: 
            print ("Don't eat too much!")
            hunger=hunger-1
    elif eat == 2:
        if hunger >= 2:
            hunger=hunger-2
        else:
            print ("Don't eat too much!")
            hunger=hunger-2
    else:
        print ("That is not a viable action!")
        eat()

#Drinking Action
def drink():
    print ("How much should I drink?")
    print ("1)A Little\n2)A Lot")
    drink = input("#: ")
    try:
        drink = int(drink)
    except ValueError:
        print ("Please enter a number")
        drink()
    if drink == 1:
        if thirst >= 1:
            thirst=thirst-1
        else:
            print ("Don't drink too much!")
            thirst=thirst-1
    elif drink == 2:
        if thirst >=3:
            thirst = thirst - 4
        else:
            print ("Don't drink too much!")
            thirst = thirst - 4
    else:
        print ("That is not a viable action!")
        drink()
        
#Sleeping Action
def sleep():
    
#Chewing Action
def chew():
    
#Acting Cute Action
def actcute():
    
#Check if Dead
def dead():
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    