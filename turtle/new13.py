import turtle

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spiral Heptagon")

# Create the turtle
t = turtle.Turtle()
t.speed(0)          # 0 = fastest speed
t.width(2)          # thickness of the line

# List of colors to cycle through
colors = ["red", "orange", "yellow", "green", "blue", "purple", "white"]

# Draw the spiral
for i in range(150):           # 150 shapes stacked
    t.color(colors[i % 7])     # pick a color (cycles every 7)
    
    # Draw a heptagon (7 sides)
    for _ in range(7):
        t.forward(200)
        t.right(360 / 7)       # exterior angle of heptagon (~51.43°)
    
    t.right(10)                # rotate before next heptagon -> spiral effect

turtle.done()



# this is not correct answer