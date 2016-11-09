import turtle

# Make our screen
window = turtle.Screen()

# Make our canvas huge
window.screensize(10000, 10000)

# Make our screen draw faster
window.tracer(32, 1)

# Create our turtle
dragon = turtle.Turtle()

# Hide our turtle
dragon.hideturtle()

# Draw our dragon
short = False
for n in range(1, 5000):
    # Move forward
    if short:
        dragon.forward(5)
    else:
        dragon.forward(10)

    # Toggle forward distance
    short = not short

    # Determine weather we should turn right or left
    if (((n & -n) << 1) & n) != 0:
        dragon.left(90)
    else:
        dragon.right(90)

# Wait for the user to click to exit
window.exitonclick()
