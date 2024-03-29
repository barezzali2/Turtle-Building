import turtle
trt = turtle.Turtle()
trt.hideturtle() #This is to hide the pointer
trt.speed(60)
trt.pensize(2)

#First pen up to start at a new position
trt.penup()
trt.right(180)
trt.forward(525)
trt.left(90)
trt.forward(310)
trt.left(90)
trt.pendown()

#Draw the building
trt.forward(1000) 
trt.left(90)
trt.forward(675) 
trt.left(90)
trt.forward(1000) 
trt.left(90)
trt.forward(675) 
trt.left(90)

#Drawing the Padding like a frame inside of the building
trt.begin_fill()
trt.fillcolor('darkblue')
trt.forward(60)
trt.left(90)
trt.forward(600) 
trt.right(90)
trt.forward(880) 
trt.right(90)
trt.forward(600) 
trt.left(90)
trt.end_fill()

#To design the padding of the building
def padding_design():
    for i in range(24):
        trt.forward(60)
        trt.left(90)
        trt.forward(25)
        trt.left(90)
        trt.forward(60)
        trt.right(180)
       
padding_design()
trt.penup()
trt.backward(940) 
trt.right(90)
trt.forward(600) 
trt.left(90)
trt.pendown()
padding_design()

#Top Design, right after the right and left design
trt.left(90)
trt.forward(25)
trt.right(90)
trt.forward(1000) 
trt.left(90)
trt.forward(25)
trt.left(90)
trt.forward(1000) 
trt.right(180)

#Back to the Original Point
trt.penup()
trt.right(90)
trt.forward(650)
trt.left(90)
trt.pendown()

#Drawing the pillars
for i in range(2):
    trt.begin_fill()
    trt.fillcolor("white")
    trt.forward(310) # starting from the starting point of the building.
    trt.left(90)
    trt.forward(340) #fixed
    trt.right(90)
    trt.forward(35)
    trt.right(90)
    trt.forward(340) #fixed
    trt.left(90)
    trt.end_fill()

#Another pen up
trt.penup()
trt.backward(410) # finding a right place for the top pillar
trt.left(90)
trt.forward(295)
trt.right(90)
trt.pendown()
    
# Creating the cross_pillar
for i in range(2):
    trt.begin_fill()
    trt.fillcolor("white")
    trt.forward(440) #Starting after the pendown.
    trt.right(90)
    trt.forward(30)
    trt.right(90) 
    trt.end_fill()

#Coming back to the original point
trt.penup()
trt.right(90)
trt.forward(295)
trt.right(90)
trt.forward(280) 
trt.right(180)
trt.forward(440) #for the door
trt.pendown()

#Creating the door
for i in range(2):
    trt.color('aliceblue')
    trt.left(90)
    trt.forward(132) 
    trt.right(90)
    trt.forward(60)
    trt.right(90)
    trt.forward(132)
    trt.left(90)


#Going Back to Find a good place for windows
trt.penup()
trt.backward(475)
trt.left(90)
trt.forward(580)
trt.right(90)
trt.pendown()

#Drawing the windows
def draw_windows():
    for i in range(4):
        for j in range(4):
            trt.forward(75)
            trt.right(90)
        trt.forward(30)
        trt.right(90)
        trt.forward(75)
        trt.left(90)
        trt.backward(30) 

        trt.penup()
        trt.right(90)
        trt.forward(50)
        trt.left(90)
        trt.pendown()

#Left windows
draw_windows()

#Going back to the starting point of the windows
trt.penup()
trt.left(90)
trt.forward(500) # starting point of the windows
trt.right(90)
trt.forward(195) # for the middle windows
trt.pendown()

def draw_windows2():
    for i in range(2): # drawing the rectangles
        trt.forward(130)
        trt.right(90)
        trt.forward(75)
        trt.right(90)
    trt.forward(33) # inside the windows
    trt.right(90)
    trt.forward(75)
    trt.left(90)
    trt.forward(48)
    trt.left(90)
    trt.forward(75)
    trt.right(90)
    trt.forward(49)

#Having a nested loop in a function to create windows in two rows
def middle_windows():
    for i in range(2):
        for j in range(2):
            draw_windows2() #Calling the middle windows here
            trt.penup()
            trt.forward(190)
            trt.pendown()
        trt.penup()
        trt.backward(640)
        trt.right(90)
        trt.forward(125)
        trt.left(90)
        trt.pendown()

middle_windows()

#Going to find a place for the right windows
trt.penup()
trt.left(90)
trt.forward(250) # back to the line of the windows origin place
trt.right(90)
trt.forward(561)
trt.pendown()

#Calling function of the small windows in the right!
draw_windows()

#Going back and finding a place to create the glass-house
trt.penup()
trt.color('black')
trt.backward(495)
trt.left(90)
trt.forward(185)
trt.right(90)
trt.pendown()

#Drawing the glasses inside the pillars
def draw_glass_house1(): 
    for i in range(6):
        trt.forward(46)
        trt.right(90)
        trt.forward(44)
        trt.right(90)
        trt.forward(46)
        trt.right(90) 
        trt.forward(44)
        trt.penup()
        trt.right(180)
        trt.forward(44)
        trt.left(90)
        trt.pendown() 

def pen_up():
    trt.penup()
    trt.left(90)
    trt.forward(264)
    trt.right(90)
    trt.forward(46)
    trt.pendown()

#Calling them
draw_glass_house1()
pen_up()
draw_glass_house1()


#Going up for middle glasses
pen_up()

#Middle glasses
def draw_glass_house2():
    for i in range(3):
        trt.forward(62)
        trt.right(90)
        trt.forward(44)
        trt.right(90)
        trt.forward(62)
        trt.right(180)

def pen_up2():
    trt.penup()
    trt.left(90)
    trt.forward(132)
    trt.right(90)
    trt.forward(62)
    trt.pendown()

#Calling them
draw_glass_house2()
pen_up2()
draw_glass_house2()

pen_up2()

#Calling the glasses of left to be in right as well
draw_glass_house1() 
pen_up()
draw_glass_house1()

#These are the patterns for the building, Pattern 1, 2 and 3 for the windows, and 4, 5, 6 for the glasses.
def pattern1(color):
    trt.penup()
    trt.goto(-440, 270)
    trt.pendown()
    trt.pencolor('white')
    trt.begin_fill()
    trt.fillcolor(color)
    draw_windows()
    trt.end_fill()

def pattern2(color):
    trt.penup()
    trt.goto(-245, 270) #245
    trt.pendown()
    trt.pencolor('white')
    trt.begin_fill()
    trt.fillcolor(color)
    middle_windows()
    trt.end_fill()

def pattern3(color):
    trt.penup()
    trt.goto(315.5, 270) #312
    trt.pendown()
    trt.pencolor('white')
    trt.begin_fill()
    trt.fillcolor(color)
    draw_windows()
    trt.end_fill()

def pattern4(color): #for glasses
    trt.penup()
    trt.goto(-179.5, -45)
    trt.pendown()
    trt.begin_fill()
    trt.fillcolor(color)
    draw_glass_house1()
    pen_up()
    draw_glass_house1()
    pen_up()
    trt.end_fill()

def pattern5(color):
    trt.begin_fill()
    trt.fillcolor(color)
    draw_glass_house2()
    pen_up2()
    draw_glass_house2()
    pen_up2()
    trt.end_fill()

def pattern6(color):
    trt.begin_fill()
    trt.fillcolor(color)
    draw_glass_house1()
    pen_up()
    draw_glass_house1()
    pen_up()
    trt.end_fill()

#Getting input from the user to decide about the pattern
def main():
    get_input = int(input('Enter 1 for windows lighting, or 2 for the glasses lighting: '))
    if get_input == 1:
        for i in range(2):
            pattern1('darkgoldenrod');
            pattern2('peru')
            pattern3('goldenrod')
            pattern1('tan');
            pattern2('burlywood')
            pattern3('wheat')
            pattern1('khaki');
            pattern2('palegoldenrod')
            pattern3('lemonchiffon')
    elif get_input == 2:
        for i in range(3):
            pattern4('lightskyblue')
            pattern5('cornflowerblue')
            pattern6('royalblue')
            pattern4('mediumturquoise')
            pattern5('lightseagreen')
            pattern6('darkcyan')

main()