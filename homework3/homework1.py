#
# Name: Nicholas Brown
# CPS 300
# Homework 1
#
# Use this program and the accompanying library graphics.py to draw a house
#

from graphics import *

#################################################################
#
# Refinement Task 1: Allow user to set colors
# 
#################################################################

# Options window
options_win = GraphWin("Select Your Color Options",400,400)
options_win.setCoords(0,0,400,400)
options_win.setBackground("white")

# Variables allow easy tweaking of GUI elements location
left_align = 100
verticle_align = 290

# Color Options
options_list = Text(Point(200,370),"Valid Color Options Include: ")
options_list_colors = Text(Point(200,340),"red, orange, yellow, green, blue, cyan, \n indigo, violet, purple, tan, grey, brown, black")
options_list_colors.setFace("arial")
options_list_colors.setSize(14)
options_list.setFace("arial")
options_list.setStyle("bold")
options_list.setSize(14)
options_list.draw(options_win)
options_list_colors.draw(options_win)
# House Color Query
wall_query = Text(Point(left_align,verticle_align),"Wall Color: ")
wall_query.setFace("arial")
wall_query.setStyle("bold")
wall_query.setTextColor("black")
wall_query.draw(options_win)

# House Color Response
wall_response = Entry(Point(left_align+90,verticle_align),10)
wall_response.setText("tan")
wall_response.setFill("grey")
wall_response.draw(options_win)

# Roof Color Query
roof_query = Text(Point(left_align,verticle_align-40),"Roof Color: ")
roof_query.setFace("arial")
roof_query.setStyle("bold")
roof_query.draw(options_win)

# Roof Color Response
roof_response = Entry(Point(left_align+90,verticle_align-40),10)
roof_response.setText("brown")
roof_response.setFill("grey")
roof_response.draw(options_win)

# Door Color Query
door_query = Text(Point(left_align,verticle_align-80),"Door Color: ")
door_query.setFace("arial")
door_query.setStyle("bold")
door_query.draw(options_win)

# Door Color Response
door_response = Entry(Point(left_align+90,verticle_align-80),10)
door_response.setText("red")
door_response.setFill("grey")
door_response.draw(options_win)

# Window Color Query
window_query = Text(Point(left_align,verticle_align-120),"Window Color: ")
window_query.setFace("arial")
window_query.setStyle("bold")
window_query.draw(options_win)

# Window Color Response
window_response = Entry(Point(left_align+90,verticle_align-120),10)
window_response.setText("cyan")
window_response.setFill("grey")
window_response.draw(options_win)

# Submit Button
submit_button = Rectangle(Point(left_align+10,verticle_align-150),Point(left_align+170,verticle_align-170))
submit_button.setFill("cyan")
submit_button.draw(options_win)

# Submit Button Text
submit_text = Text(Point(left_align+90,verticle_align-160), "Press Anywhere to Submit")
submit_text.setFace("arial")
submit_text.setStyle("bold")
submit_text.draw(options_win)

# Check for submit button press
if options_win.getMouse():
    wall_color = wall_response.getText()
    roof_color = roof_response.getText()
    door_color = door_response.getText()
    window_color = window_response.getText()
    options_win.close()

###################################################################
#
# House Drawing Code with Instruction Steps Window
#
###################################################################

# Instructions Window
inst_win = GraphWin ("Instructions",400,400)
inst_win.setCoords(0,0,400,400)
inst_win.setBackground("white")

# Alignment Variables
inst_left_align = 200
inst_vert_align = 340

# Instruction Steps Text
inst_title = Text(Point(inst_left_align,inst_vert_align),"Follow the steps")
inst_title.setFace("arial")
inst_title.setSize(14)
inst_title.setStyle("bold")
inst_title.draw(inst_win)

# Step 1 Text
inst_step1 = Text(Point(inst_left_align + 10,inst_vert_align-40),"Step 1: Select bottom lefthand corner of house")
inst_step1.setSize(14)
inst_step1.draw(inst_win)

# Step 2 Text
inst_step2 = Text(Point(inst_left_align ,inst_vert_align-75),"Step 2: Select top righthand corner of house")
inst_step2.setSize(14)
inst_step2.draw(inst_win)

# Step 3 Text
inst_step3 = Text(Point(inst_left_align - 62,inst_vert_align-110),"Step 3: Select roof peak")
inst_step3.setSize(14)
inst_step3.draw(inst_win)

# Step 4 Text
inst_step4 = Text(Point(inst_left_align - 35, inst_vert_align-145),"Step 4: Select top corner of door")
inst_step4.setSize(14)
inst_step4.draw(inst_win)

# Step 5 Text
inst_step5 = Text(Point(inst_left_align - 47, inst_vert_align-180),"Step 5: Select window center")
inst_step5.setSize(14)
inst_step5.draw(inst_win)

# Done Text
inst_done = Text(Point(inst_left_align - 120, inst_vert_align-215),"Done !")
inst_done.setSize(14)
inst_done.draw(inst_win)

# Instruction Pointer
inst_pointer = Circle(Point(inst_left_align - 160, inst_vert_align-40),10)
inst_pointer.setFill("cyan")
inst_pointer.draw(inst_win)

# Open House Drawing Window
win = GraphWin ("Draw-a-house",800,800)
win.setCoords(0,0,800,800)
win.setBackground("white")

# Main Wall Coords
lower_left = win.getMouse()
inst_pointer.move(0,-35)
upper_right = win.getMouse()


# Main Wall Object
wall = Rectangle(lower_left,upper_right)
wall.setFill(wall_color)
wall.draw(win)
inst_pointer.move(0,-35)

# Get Roof Point
roof_point = win.getMouse()

# Upper Left Main Wall Coords
upper_left = Point(lower_left.getX(), upper_right.getY())

# Roof Object
roof = Polygon(roof_point,upper_right,upper_left)
roof.setFill(roof_color)
roof.draw(win)
inst_pointer.move(0,-35)

# Get Door Coords
door_upper_corner = win.getMouse()
door_other_corner = Point(roof_point.getX(),lower_left.getY())

# Door Object
door = Rectangle(door_other_corner,door_upper_corner)
door.setFill(door_color)
door.draw(win)
inst_pointer.move(0,-35)

# Get Window Coords
window_center_point = win.getMouse()

# Calculate Door Width
# Uses abs() function incase result is negative
door_width = abs((door_upper_corner.getX() - door_other_corner.getX()))
window_width = door_width/4

# Calculate Window Points
window_point1 = Point(window_center_point.getX() + window_width, window_center_point.getY() + 20)
window_point2 = Point(window_center_point.getX() - window_width, window_center_point.getY() - 20)

# Window Object
window = Rectangle(window_point1,window_point2)
window.setFill(window_color)
window.draw(win)
inst_pointer.move(0,-35)