#  Nicholas Brown
#  CPS 300/500 (Python Programming): Lab 14
#
#  This file contains the beginning of a program to simulate turns 
#  in the dice game Yahtzee.

from random import *

#
#  displayDice (dice)
#
#  The list dice contains the results of most recent roll of the dice.
#
#  The function displayDie prints out the number rolled for each individual die.
#
#  In the future, this function could be replaced with a more visual
#  representation of dice.
#

def displayDice (dice):
    for i in range(len(dice)):
        print (dice[i],end=" ")
    print ("\n")

#
#  The list dice contains the results of most recent roll of the dice.
#
#  This function simulates a possible reroll of the dice: the user is prompted
#  for which dice should be kept and which should be re-rolled.
#
#  This function makes use of the function yesOrNo, which must be written.
#

def reroll (dice):
    for i in range(len(dice)):
        ans = yesOrNo ("Keeping die #{0} (value: {1})? (Y/N) ".format(i,dice[i]))
        if (ans != True):
            dice[i] = rollOneDie()

#  rollAllDice (dice)
#
#  This function simulates the rolling portion of a turn, returning
#  the final values in the list dice.
#
#  Initially, all dice are rolled.  The results are displayed, and
#  the user is given the option to re-roll at most twice (for a total
#  of three rolls).
#
#  This function makes use of the functions yesOrNo and reroll, both 
#  of which must be written.

def rollAllDice (dice):
    for i in range(len(dice)):
        dice[i] = rollOneDie()

    print("\nYour roll: ")
    displayDice(dice) 

 
   # Can re-roll at most twice */
    if yesOrNo("Do you want to re-roll? (Y/N) "):
        reroll(dice)
        print("\nYour roll: ")
        displayDice(dice)
 
        if yesOrNo("Do you want to re-roll? (Y/N) "):
            reroll(dice)
            print("\nYour roll: ")

####################################################
#   Your function definitions should go here


# Part 1: rollOneDie
def rollOneDie():
    seed()
    die = randrange(1,7)
    return die

# Part 2: yesOrNo
def yesOrNo(prompt):
    yval = ["y","Y"]
    decision = input(prompt+" : ")
    tval = decision[:1]

    if tval in yval:
        return True
    else: 
        return False

# Part 3: countUp
def countUp(val,dice):
    count = 0
    for i in range(len(dice)):
        if dice[i] == val:
            count+=1
    return count
    

# Part 4: displayPoints
def displayPoints(msg,points):
    print("Points for {0}: {1}".format(msg,points))

# Part 4: upperSection
def upperSection(val,freq):
    return int(freq[val] * val)       


####################################################

#  main -- the heart of the program 
#
#  There are two arrays here:
#
#      dice[5], which contains the results of a turn's dice roll
#         (e.g., each dice[i] is the roll of a separate die)
#
#      freq[7]: indicates how many dice came up with a given value
#          freq[1] is the number of ones rolled
#          freq[2] is the number of twos rolled
#               etc.
#
#      Example: Suppose the dice rolled were  5 3 6 6 2
#          dice[0] = 5   dice[1] = 3   dice[2] = 6   etc
#
#          freq[1] = freq[4] = 0   freq[5] = freq[3] = freq[2] = 1
#          freq[6] = 2

def main ():
    dice = [0]*5    # dice[i] is the value on die #i
    freq = [0]*7    # freq[v] is how many dice came up with value v
    
    # set seed if you want reproducible dice rolls
    #    (keep next line commented out if you don't)
    # seed (12345678)


    # roll each of the dice exactly once
    rollAllDice (dice)

    # display the results of the rolls
    displayDice (dice)

    # uncomment these lines in Part 3
    for i in range(1,7):
        freq[i] = countUp(i,dice);
        
    for i in range(1,7):
        print("Number of {0}s rolled: {1}\n".format(i,freq[i]))


    # uncomment these lines in Part 4
    displayPoints ("Aces/Ones", upperSection (1,freq))
    displayPoints ("Deuces/Twos", upperSection (2,freq))
    displayPoints ("Threes", upperSection (3,freq))
    displayPoints ("Fours", upperSection (4,freq))
    displayPoints ("Fives", upperSection (5,freq))
    displayPoints ("Sixes", upperSection (6,freq))

