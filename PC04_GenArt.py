"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author: Logan Turner
********* HEY, READ THIS FIRST **********
This is a description of the code that is written out below. This script draws
flowers on a bush background, and the flowers change with each iteration of the code.
"""
import turtle
import random

turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================

#Establish variables
#name our turtles
starStampTurtle = turtle.Turtle() #this is the turtle that draws star stamp flower
polygonTurtle = turtle.Turtle() #this is the turtle that draws polygon flower

#name color variables
lavendarWeb = (220, 214, 247)
maximumBluePurple = (166, 177, 225)
englishLavendar = (180, 134, 159)
roseDust = (152, 95, 111)
independence = (78, 76, 103)

#create colors array
colors = [lavendarWeb, maximumBluePurple, englishLavendar, roseDust, independence]


#draw background
panel.bgcolor(5,140,66)

#draw 4 octagon flowers
for i in range (4):
    polygonTurtle.penup()
    polygonTurtle.pensize(random.randint(1,7))
    polygonTurtle.speed(random.randint(3,10))
    polygonTurtle.goto(random.randint(-200, 200), random.randint(-150, 225))
    polygonTurtle.pendown()
    polygonTurtle.pencolor(colors[i])
    polygonTurtle.fillcolor(colors[-i])
    polygonTurtle.begin_fill()

    for i in range (9):
        polygonTurtle.forward(25)
        polygonTurtle.right(45)
        
    polygonTurtle.end_fill()

#draw random number of star-shaped stamp flowers
starStampTurtle.shape("arrow")

for i in range(random.randint(3,10)):
    starStampTurtle.penup()
    starStampTurtle.goto(random.randint(-270, 270), random.randint(-270,270))
    starStampTurtle.turtlesize(random.randint(2, 6))
    starStampTurtle.pencolor(random.choice(colors))
    starStampTurtle.fillcolor(random.choice(colors))
    starStampTurtle.pensize(random.randint(1,10))
    starStampTurtle.speed(random.randint(3,7))
    starStampTurtle.pendown()
    starStampTurtle.begin_fill()
    starStampTurtle.stamp()
    starStampTurtle.backward(1)
    starStampTurtle.left(180)
    starStampTurtle.stamp()
    for i in range (random.randint(5,25)):
        starStampTurtle.left(45)
        starStampTurtle.shape("triangle")
        starStampTurtle.stamp()
    starStampTurtle.end_fill()
    
# panel.update() # uncomment this if you've turned off animation (line 26). I recommend leaving this outside of loops, for now.
# =================== CLEAN UP =========================
# uncomment the line below when you are finished with your code (before you turn it in)

turtle.done()