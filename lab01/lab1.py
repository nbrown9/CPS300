# Name: Nick
# Lab 1: Intro to the Python IDE (IDLE)


# the definition of a simple function
def hello (name):
    print ("Hi",name)
    print ("Welcome to Python!")

##
# the main portion of the program
##

user = input ("What's your name? ")
num = int (input ("What's your favorite number? "))

for j in range (1,num+1):
    print ("\nAttempt ",j)
    hello (user)

print ("\n\nGoodbye for now!")
