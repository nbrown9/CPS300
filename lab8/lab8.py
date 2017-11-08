# Nicholas Brown
# CPS 300/500  CPS300

# create a 12-element list to contain our answers
answers = [1]*12

four = ""
one = 1234.56789
two = 268
three = "october"

# display one in a field of width 15, left justified
answers[0]  = "#{0:<15}#".format(one,two,three,four)


# display one in a field of width 15, centered
answers[1]  = "#{0:^15}#".format(one,two,three,four)


# display one with 20 significant digits
answers[2]  = "20 sig digs: {0:.16f}".format(one,two,three,four)


# display one with 4 decimal places
answers[3]  = "4 dec places: {0:.4f}".format(one,two,three,four)


# display both two and three (in that order),
#     in fields of width 10 that are right justified
answers[4]  = "#{1:>10}#{2:>10}#".format(one,two,three,four)


# display both three and two (in that order),
#     in fields of width 5 that are left justified
answers[5]  = "#{2:<5}#{1:<5}#".format(one,two,three,four)


# display two in a field of width 9, centered, with all blank 
#     spaces replaced by periods
#  Result should be:     ...268...
answers[6]  = "{1:.^9}".format(one,two,three,four)


# display one in a field of width 14, right justified, 
#     with all blank spaces replaced by zeros
answers[7]  = "{0:0>14}".format(one,two,three,four)


# set up the next four so that
#     (1) the decimal points line up with each other
#     (2) 1 decimal place is shown for answers[8]
#     (3) 4 decimal places are shown for answers[9]
#     (4) 3 decimal places are shown for the final two
#
# You'll have to play with field widths to line things up.

answers[8]  = "{0:.>10.1f}".format(528.7568)
answers[9]  = "{0:.>13.4f}".format(-32.17)
answers[10] = "{0:.>12.3f}".format(1.357908642)
answers[11] = "{0:.>12.3f}".format(16326.4)

##########################################################
# display all the answers
for i in range(12):
    print ("answers[{0}]:\n {1}".format(i,answers[i]))
    print ()
