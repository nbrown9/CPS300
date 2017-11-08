####################################################################################
##
##  - Author: Nicholas Brown
##  - CPS300
##  - Homework 3
##
##  - Description: A word guessing game similar to hangman and 'Wheel of Fortune'
##
###################################################################################

###################################################################################
## IMPORTS
###################################################################################

from graphics import *


###################################################################################
## FUNCTIONS
###################################################################################

# stringify converts the list sofar into a string
def stringify (sofar):
    return "".join (sofar)

# getSolve() prompts user to see if they would like to try to solve
def getSolve(window,phrase): 
    mx = window.getWidth()
    my = window.getHeight()
    
    # open gui input
    solve_in = Entry(Point(mx/2,my/2), len(phrase))
    solve_in.setFace("helvetica")
    solve_in.setSize(36)
    solve_in.setStyle("bold")

    # solve gui text
    solve_in_text = Text(Point(mx/2,my/2+50),"Press 'Enter' to submit")
    styleText(solve_in_text)

    # solve gui background
    solve_box = Rectangle(Point(mx/2-250,my/2-100), Point(mx/2+250,my/2+100))
    solve_box.setFill("pink")
    # check for enter/return key

    todraw = [solve_box,solve_in,solve_in_text]
    multiDraw(todraw,window)
    while True:
        enterkey = window.getKey()
        solve_text = solve_in.getText()
        if enterkey == "Return" and solve_text != "":
            break
    
    if len(solve_text) < len(phrase):
        diff = len(phrase) - len(solve_text)
        solve_text = solve_text + "-"*diff
    elif len(solve_text) > len(phrase):
        s = slice(0,len(phrase))
        solve_text = solve_text[s]
    # return and undraw
    multiUndraw(todraw,window)
    return solve_text.upper()

# this function prompts user for character, reads it, and-
# ensures what is sent back is a single character
def getGuess (window):
    mx = window.getWidth()
    my = window.getHeight()
    
    # open gui input
    guess_in = Entry(Point(mx/2,my/2), 3)
    guess_in.setFace("helvetica")
    guess_in.setSize(36)
    guess_in.setStyle("bold")

    # solve gui text
    guess_in_text = Text(Point(mx/2,my/2+50),"Press 'Enter' to submit")
    styleText(guess_in_text)

    # solve gui background
    guess_box = Rectangle(Point(mx/2-250,my/2-100), Point(mx/2+250,my/2+100))
    guess_box.setFill("cyan")
    # check for enter/return key

    todraw = [guess_box,guess_in,guess_in_text]
    multiDraw(todraw,window)

    # Wait for enterkey and non blank value
    while True:
        enterkey = window.getKey()
        ch = guess_in.getText()
        if enterkey == "Return" and ch != "":
            break

    # undraw window
    multiUndraw(todraw,window)
    # only return one character (even if user entered more)
    # do not change this line
    return ch[0].upper ()


# this function copies non-letter characters from-
def setup (sofar,orig):
    for i in range(len(orig)):
        if not orig[i].isalpha():
            sofar[i] = orig[i]
 

# update the list sofar to reflect the guess ch:
def update (sofar,orig,ch):
    isin = False
    for i in range (len(orig)):
        if orig[i] == ch:
            sofar[i] = ch
            isin = True
    return isin
# determine whether the list sofar is an accurate representation
def compare (sofar, orig):
    return stringify(sofar) == orig

# Ask user if they want to solve
def solve_mode ():
    yesval = ["Y", "y", "yes"]
    noval = ["N", "n", "no"]

    decision = input("Try and solve ? (Y/N): ")
    
    while decision not in yesval and decision not in noval: 
        print(decision," is not a valid entry, try again !")
        decision = input("Try and solve ? (Y/N): ")

    if decision in yesval:
        return True
    elif decision in noval:
        return False

def inside(point, rectangle):
    """ Is point inside rectangle? """

    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

def drawSquares(phrase,window,answer):
    # create a list of rectangles
    word_blanks = []
    char_blanks = []

    # math for boxes
    mx = window.getWidth()
    my = window.getHeight()

    # create list of rectangles
    for i in range(len(phrase)):
        word_blanks.append(Rectangle(Point((mx/len(phrase)*i)+5,my*.70), Point((mx/len(phrase)*(i+1))-5,my*.70+(my*.08))))
    
    # draw list of rectangles
    for i in range(len(word_blanks)):
        char_blanks.append(Text(word_blanks[i].getCenter(),answer[i]))
        if phrase[i] is not " ":
            #character location
            word_blanks[i].setOutline("black")
            word_blanks[i].setFill("white")
            word_blanks[i].setWidth(2)
            word_blanks[i].draw(window)
            styleText(char_blanks[i],36)
            char_blanks[i].draw(window)

# drawGuess() draws the guessing interface
def drawGuess(window):
    mx = window.getWidth()
    my = window.getHeight()

    # create and draw guess button
    # kind of hardcoded and crappy maybe make it less shitty
    button_guess = Rectangle(Point(mx/2-(mx*.22), my/4),Point(mx/2-(mx*.02),my/4+(my*.10)))
    button_guess.setFill("green")
    button_guess_text = Text(button_guess.getCenter(),"Guess a character")
    styleText(button_guess_text)
    todraw = [button_guess,button_guess_text]
    multiDraw(todraw,window)
    return button_guess

# drawSolve() draws the guessing interface
def drawSolve(window):
    mx = window.getWidth()
    my = window.getHeight()

    # create and draw solve it button
    button_solve = Rectangle(Point(mx/2+(mx*.02), my/4),Point(mx/2+(mx*.22),my/4+(my*.10)))
    button_solve.setFill("pink")
    button_solve_text = Text(button_solve.getCenter(),"Try and solve")
    styleText(button_solve_text)
    # to draw
    todraw = [button_solve,button_solve_text]
    multiDraw(todraw,window)

    # return object type 
    return button_solve

# create money counter
def drawMoney(window,money):
    mx = window.getWidth()
    my = window.getHeight()

    money_window = Rectangle(Point(10,my-10),Point(300,my-50))
    money_window.setFill("cyan")
    money_window_text = Text(money_window.getCenter(),"Prize Remaining: ${0:.2f}".format(money))
    money_window_text.setSize(18)
    money_window_text.setStyle("bold")
    money_window_text.setFace("helvetica")
    # todraw
    todraw = [money_window,money_window_text]
    multiDraw(todraw,window)

# Creates our main play window
def createWindow():
    # create window
    mw = GraphWin("Guess the Phrase!",1024,768)
    mw.setCoords(0,0,mw.getWidth(),mw.getHeight())
    mw.setBackground("grey")

    # return object type GraphWin
    return mw

# draw array of objects
def multiDraw(todraw,window):
    # to draw bulk elements at once
    for i in range(len(todraw)):
        todraw[i].draw(window)

# undraw array of objects
def multiUndraw(todraw,window):
    for i in range(len(todraw)):
        todraw[i].undraw()

#apply batch styles to text objects
def styleText(textobj,size=18,style="bold",face="helvetica"):
    textobj.setSize(size)
    textobj.setStyle(style)
    textobj.setFace(face)

# end screen for winners and losers
def endScreen(window,solved,money):
    mx = window.getWidth()
    my = window.getHeight()

    
    if solved:
        bgcolor = "green"
        message = "YOU WON ${0:.2f} !".format(money)
    else:
        bgcolor = "red"
        message = "YOU LOSE !"
    
    end_window = Rectangle(Point(mx/2-300,my/2-150), Point(mx/2+300,my/2+150))
    end_window.setFill(bgcolor)

    end_window_text = Text(end_window.getCenter(),message)
    styleText(end_window_text,36)

    close_text = Text(Point(mx/2,my/2-50),"Click anywhere to close")
    styleText(close_text)

    todraw = [end_window,end_window_text,close_text]
    multiDraw(todraw,window)

    window.getMouse()
    window.close()

###################################################################################
## MAIN 
###################################################################################

def main ():
    # define some variables we'll use
    phrase = "Magical Mystery Word".upper ()
    answer = ['-']* len (phrase)
    prize_pool = 1500
    solved = False
    already_guessed = []

    # create main window
    mw = createWindow()

    # create and draw guess button and solve button
    gb = drawGuess(mw)
    sb = drawSolve(mw)

    # have all nonalphabetic characters show up in answer string
    setup (answer, phrase)

    while not solved and prize_pool >= 0:
        
        # we'll want to keep udating these
        drawSquares(phrase,mw,answer)
        drawMoney(mw,prize_pool)

        # Game Main Menu / Message
        print ("\nCurrent status: ", stringify(answer))      
        print ("Prize pool: ${0:.2f}".format(prize_pool))

        # Detect attempted solve
        solve_attempt = False

        # True will run after the initial GUI setup and end once a choice is made 
        while True:
            # pt is the last clicked location of the mouse
            pt = mw.getMouse()

            # test for guess or solve
            if inside(pt,gb):
                ch = getGuess(mw)
                update (answer,phrase,ch) # update answer with most recent guess
                # add character guess
                already_guessed.append(ch)
                break
            elif inside(pt,sb):
                answer = getSolve(mw,phrase)
                solve_attempt = True
                break
        
        solved = compare(answer,phrase)

        # reduce pool according to results
        if  solve_attempt is True:
            break
        elif ch not in already_guessed and update(answer,phrase,ch):
            prize_pool = prize_pool-100
        elif not solved:
            prize_pool = prize_pool-150

    # we're out of the loop, and ready to declare victory/defeat
    endScreen(mw,solved,prize_pool)