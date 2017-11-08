# Nicholas Brown
# CPS300


# Our line function
def line(width, ch='!'):
    return width*ch+"\n"

# Our modified line function
def modLine(width, ch='!'):
    return width*ch

# Mixed Line function
def mixedLine(num1,ch1,num2,ch2):
    return modLine(num1,ch1) + modLine(num2,ch2) + "\n"


# Rectangle
def rectangle(height, width, ch='*'):
    return line(width,ch)*height

# Triangle
def triangle(size, ch='$'):
    retString = ''
    for i in range(size):
        i = i + 1
        tempString = i*ch + "\n"
        retString =  retString + tempString
    return retString
        