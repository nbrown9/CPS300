# NICHOLAS BROWN
# CPS 300 (Python Programming): Lab 13

from random import *
                            
def diceExperiment ():
    # create a list with room for 100 items
    #   roll[i] will contain the i-th dice roll generated
    roll = [0]*100
    
    # create a list with room for 7 items
    #   timesRolled[i] will contain the number of times 
    #      i was rolled
    timesRolled = [0]*7
    
    # initialize the seed
    seed ()
    
    # generate 100 pseudo-random dice rolls
    for i in range(100):
        roll[i] = randrange(1,7)
        timesRolled [roll[i]] += 1
        
    # display the results
    print ("The dice rolls generated: ")
    for i in range(100):
        print (roll[i],end=" ")
        if i%10 == 9:
            print ()
    
    print ("\nThe frequency of rolls: ")
    for i in range(1,7):
        print ("Times {0} was rolled: {1}".format(i,timesRolled[i]))
               
    print()
 
 
def guess (low, hi):
    welcome = "I'm thinking of a number between {0} and {1} (inclusive)."
    print (welcome.format(low,hi))
    
    guesses = 0

    # your code goes here
    answer = randint(low,hi)
    
    user_guess = int(input("What's your guess? "))
    guesses += 1
    while user_guess != answer:
        if user_guess > answer:
            print("Go lower")
        elif user_guess < answer:
            print("Go higher")
        user_guess = int(input("What's your guess? "))
        guesses += 1
 
    print ("\nYou guessed it in {0} guesses".format(guesses))
