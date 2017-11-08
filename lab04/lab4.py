# Nicholas Brown
# CPS300 Lab 4: The Program-Design Process
#
# Given a non negative integer between 0 and 1000 calculate and display
# the number obtained by reversing the digits
#
# Constraints : Must be a positive integer between 0 and 1000
#     Input: INT 0 - 1000 (Ex 312)
#     Output: INT 0 - 1000 (Ex 213)


# TODO: Get user input
IniVal = int(input("Enter a value between 0 and 1000 : "))

# Grab Digits 
Ones = IniVal % 10
IniVal = IniVal // 10

Tens = IniVal % 10
IniVal = IniVal // 10

Hundreds = IniVal % 10


# Reverse Digits
ReVal = str(Ones)+str(Tens)+str(Hundreds)

# TODO: Print Reverse
print ("The reverse value is : " ,ReVal)

##    Sample Runs:
##
##    >>> %Run lab4.py
##    Enter a value between 0 and 1000 : 368
##    The reverse value is :  863
##    >>> %Run lab4.py
##    Enter a value between 0 and 1000 : 48
##    The reverse value is :  840
##    >>> %Run lab4.py
##    Enter a value between 0 and 1000 : 140
##    The reverse value is :  041
