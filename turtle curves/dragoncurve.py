import turtle
import random

#make screen
window = turtle.Screen()

#make size of screen big
window.screensize(10000,10000)

#make screen draw faster
window.delay(5)

#create turtle
dragon = turtle.Turtle()

#make turtle very fast
dragon.speed("fastest")

#hide turtle
dragon.hideturtle()

# Draw the dragon

for n in range(1,1000):
    dragon.forward(10)
    # left or right decision
    if (((n & -n)<< 1) & n)!= 0:
        dragon.left(90)
    else:
        dragon.right(90)
    
#exit
window.exitonclick()
