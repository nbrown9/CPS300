## NICHOLAS BROWN
## CPS 300

def one ():
    # replace this for-loop with a while loop
    # don't change any more than is necessary
##    for j in range(20):
##        print ("{0:2} x 2 = {1:<2}".format(j,j*2))
##    
    j = 0
    while j < 20:
        print ("{0:2} x 2 = {1:<2}".format(j,j*2))
        j+=1
    
def two ():
    low = 3
    hi = 50
    total = 0
    
    # replace this for-loop with a while loop
    # don't change any more than is necessary
##
##    for m in range (hi, low-1,-2):
##        total = total + m
##    
    m = hi
    while m > low-1:
        total = total + m
        m-=2
        
    return total

def three ():
    # replace this for-loop with a while loop
    # don't change any more than is necessary

##    for word in "This is a boring sentence".split ():
##        print (word,len(word))
##    
    phrase = "This is a boring sentence".split ()
    
    i = 0
    while i < len(phrase):
        print(phrase[i], len(phrase[i]))
        i += 1

def four ():
    # replace these for-loops with while loops
    # don't change any more than is necessary

##    for salute in ["hello","hi","greetings","hey!","<nod>"]:
##        for person in ["Jane","Charles","Fitz"]:
##            print (salute,person)

##    i = 0
##    w = 0
##    salute = ["hello","hi","greetings","hey!","<nod>"]
##    person = ["Jane","Charles","Fitz"]
##    
##    while i < len(salute):
##        i += 1
##        for p in person:
##            print(salute[i],p)
    i = 0
    salute = ["hello","hi","greetings","hey!","<nod>"]
    person = ["Jane","Charles","Fitz"]
    
    while i < len(salute):
        w = 0
        while w < len(person):
            print(salute[i],person[w])
            w += 1
        i += 1

def syracuse ():
    
    # replace the next line with your code to
    #     (1) prompt user to enter an int
    #     (2) read the integer
    #     (3) print out (on one line) the Syracuse sequence
    #          that starts with the number entered by user
    #
    #   For example, if user enters 5, following should be printed:
    #         5 16 8 4 2 1
    #
    user_in = int(input("Enter a number: "))
    printstring = str(user_in)
    while user_in != 1:
        if user_in % 2 == 0:
            user_in = user_in // 2
        else:
            user_in = user_in*3 + 1
        printstring = printstring + " " + str(user_in)
    
    print (printstring)
    