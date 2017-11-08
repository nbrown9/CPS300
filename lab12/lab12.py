## NICHOLAS BROWN
## CPS300

# stringify converts the list sofar into a string
def stringify (sofar):
    
    # Task #1: add your code here (and change value returned)
    return "".join(sofar)


# this function prompts user for character, reads it, and
#    ensures what is sent back is a single character

def getGuess ():
    ch = input ("Guess a char: ")

    # Task #2: add code after this comment to ensure we have a
    #    nonempty response
    while " " in ch or ch == "":
        print("Invalid character, guess again!")
        ch = input ("Guess a char: ")
    
    # only return one character (even if user entered more)
    # do not change this line
    return ch[0].upper ()


# this function copies non-letter characters from
#      orig into sofar
def setup (sofar,orig):
    for i in range(len(orig)):
        if not orig[i].isalpha():
            sofar[i] = orig[i]
 

# update the list sofar to reflect the guess ch:
#    if the i-th element of orig is ch, then the
#     i-th element of sofar should be made ch       
#       
def update (sofar,orig,ch):
    
    # Task # 3: replace pass with your own code
    # pass
    for i in range(len(orig)):
        if orig[i] == ch:
            sofar[i] = ch

# determine whether the list sofar is an accurate representation
#    of the string orig
#
#    Return True if they have the same values (and same length)
#    Return False otherwise
def compare (sofar, orig):

    # Task #4: add your code here (and change value returned)
    if stringify(sofar) == orig:
        return True
    else:
        return False


##
## Do not change ANYTHING in main ()
##
#
#  The basic idea:
#      phrase (a string) holds the correct solution
#      answer (a list of chars) represents the current
#           status of user's attempt to figure out
#           the correct answer
#
def main ():
    phrase = "Magical Mystery Word".upper ()

    # make sure answer is exactly as long as phrase, but make it
    #    mutable  (i.e., a list)
    answer = ['-']* len (phrase)

    # have all nonalphabetic characters show up in answer string
    setup (answer, phrase)

    guesses = 0
    solved = False

    while not solved and guesses <= 20:
        print ("\nCurrent status: ", stringify(answer))
        ch = getGuess ()

        # update answer to account for most recent guess
        update (answer,phrase,ch)
 
        # determine whether puzzle has been solved
        solved = compare (answer,phrase)

        # increase number of guesses
        guesses = guesses + 1

    # we're out of the loop, and ready to declare victory/defeat
    if solved:
        print ("\nCongratulations!")
        print ("You guessed it in",guesses,"guesses")
    else:
        print ("\nSorry, better luck next time.")
        print ("The answer was: ", phrase)
