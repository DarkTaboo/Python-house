from turtle import *

#House Piainting

#Step 1: Draw a square
speed(10)
width(7)
color("Grey")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#End of the square

#Drawing a Door

forward(70)
begin_fill()
color("Black")
left(90)
forward(100) #Height of the door
right(90)
forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()

#Drawing of the roof

color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#Ending of the roof

penup()
goto(15, 130)
pendown()

#Drawing the window N1

color("Black")
begin_fill()
right(150)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

#End of the window N1

penup()
goto(185, 130)
pendown()

#Drawing the window N2

color("Black")
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
end_fill()


exitonclick()