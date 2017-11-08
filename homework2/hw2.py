#Nicholas Brown
#CPS 300
#Homework 2


# Entwine Function
def entwine(str, item):
    tempStr = ""
    for i in range(len(str)):
        tempStr = tempStr + str[i] + item
    return(tempStr)

# Shout !
def shout(str):
    tempStr = ""
    for i in range(len(str)):
        tempStr = tempStr + str[i] + " "
    return(tempStr.upper())

# Banner of stars
def banner(str):
    strLen = len(str)
    tempStr = "*"*(strLen + 4)+"\n* "+str+" *\n"+("*"*(strLen+4))+"\n"
    return(tempStr)

# Triangle
def triangle(str):
    tempStr = ""
    for i in range(len(str)):
        i = i+1
        tempStr = tempStr + str[0:i] + "\n"
    return(tempStr)

#Rotate letters
def rotate(str):
    tempStr = ""
    for i in range(len(str)):
        tempStr = tempStr + str[i:] + str[:i] + "\n"
    return(tempStr)

# word count
def wordCount(inputfile, special):
    workingFile = open(inputfile, 'r')
    lines = workingFile.readlines()
    wordCounter = 0
    for line in lines:
        if special in line:
            wordCounter = wordCounter + 1
    print ("The word "+special+" appears this many times: " + str(wordCounter))
    workingFile.close()
