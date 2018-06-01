## File name : lab02a.py
## using turtle to draw regular polygons
## prompt user for the number of sides and the color compenent (r,g,b)
import turtle

turtle.shape('turtle')
turtle.title('Lab 02 -- 2016')

# get the number of sides from user
n = int(turtle.textinput("Lab 02","The number of sides: "))

# draw the n-side polygon using for loop
# the lenght of a side is getting shorter as n getting larger
# when n = 4, the length of a side is 100
for x in range (n):
    turtle.forward(400/n)
    turtle.left(360/n)
turtle.up()

# get the value of red color from user
r = float(turtle.textinput("Lab 02","the red color component [between 0 and 1] ex : 0.3"))

# get the value of green color from user
g = float(turtle.textinput("Lab 02","the green color component [between 0 and 1] ex : 0.3"))

# get the value of blue color from user
b = float(turtle.textinput("Lab 02","the blue color component [between 0 and 1] ex : 0.3"))

# create the color from rgb values given by user
turtle.color(r,g,b)

# move the turtle to a new lovation below
turtle.goto(0,-200)

# draw a regular polygon with n sides and color(r.g.b)
# use a for loop
turtle.begin_fill()
turtle.down()
for x in range (n):
    turtle.forward(400/n)
    turtle.left(360/n)
turtle.end_fill()

# make the turtle invisible
turtle.hideturtle()

# message for user
print("Please click on the graphics window to exit...")

# wait for user to click on the screen to exit
turtle.exitonclick()

# the end
