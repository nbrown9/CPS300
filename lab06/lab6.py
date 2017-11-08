#  Lab 6:  Nicholas Brown

# import the graphics package
from graphics import *


#####################################################################
# Task #1:
#   Create/open a single graphics window:
#   1.  Its title is:  My Lab 6
#   2.  The window is 500 pixels wide and 250 pixels high
#   3.  The window's background is: tan
#
# All items created in subsequent tasks should be place in this window.
win1 = GraphWin("My Lab 6", 500, 250)
win1.setBackground("tan")
#####################################################################
# Task #2:
#   Draw a green circle (with radius of 30 pixels),
#              centered at the point (125,125)
green_circ = Circle(Point(125,125),30)
green_circ.setFill("green")
green_circ.draw(win1)

#####################################################################
# Task #3:
#   Draw a purple rectangle (height of 50 pixels, width of 20 pixels)
#           whose top-left corner is at point (50,10)
purp_rec = Rectangle(Point(50,10),Point(70,60))
purp_rec.setFill("purple")
purp_rec.draw(win1)



#####################################################################
# Task #4:
#   Draw a cyan triangle, whose vertices are at the points
#               (400,5), (495,245), and (305,200)

tp1 = Point(400,5)
tp2 = Point(495,245)
tp3 = Point(305,200)

cyan_tri = Polygon(tp1,tp2,tp3)
cyan_tri.setFill("Cyan")
cyan_tri.draw(win1)


#####################################################################
# Task #5:
#   Wait for a mouse click inside window, then close window
 
if win1.getMouse():
    win1.close()