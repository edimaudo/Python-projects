import turtle

#make screen
window = turtle.Screen()

#draw faster
window.delay(5)

#create turtle
dragon = turtle.Turtle()

#hide turtle
dragon.hideturtle()

#draw a square
dragon.forward(50)
dragon.left(90)
dragon.forward(50)
dragon.left(90)
dragon.forward(50)
dragon.left(90)
dragon.forward(50)
dragon.left(90)

window.exitonclick()
