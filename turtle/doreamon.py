import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Doraemon Full Body")
screen.setup(width=800, height=900)

t = turtle.Turtle()
t.speed(0)
t.width(3)

# ==================== FACE ====================

# Blue face
t.penup()
t.goto(0, 0)
t.pendown()
t.color("blue")
t.begin_fill()
t.circle(150)
t.end_fill()

# White mouth area
t.penup()
t.goto(0, 50)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(100)
t.end_fill()

# Red nose
t.penup()
t.goto(0, 170)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(25)
t.end_fill()

# Left eye white
t.penup()
t.goto(-60, 230)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(25)
t.end_fill()

# Left eye black
t.penup()
t.goto(-60, 240)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(15)
t.end_fill()

# Left eye shine
t.penup()
t.goto(-65, 250)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(5)
t.end_fill()

# Right eye white
t.penup()
t.goto(60, 230)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(25)
t.end_fill()

# Right eye black
t.penup()
t.goto(60, 240)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(15)
t.end_fill()

# Right eye shine
t.penup()
t.goto(55, 250)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(5)
t.end_fill()

# Whiskers
t.color("black")
t.width(2)

for y in [150, 170, 190]:
    t.penup()
    t.goto(-100, y)
    t.pendown()
    t.goto(-150, y - 10 if y == 150 else y)

for y in [150, 170, 190]:
    t.penup()
    t.goto(100, y)
    t.pendown()
    t.goto(150, y - 10 if y == 150 else y)

# Mouth vertical line
t.penup()
t.goto(0, 145)
t.pendown()
t.width(3)
t.goto(0, 90)

# Smile
t.penup()
t.goto(-50, 90)
t.pendown()
t.setheading(-60)
t.circle(58, 120)
t.setheading(0)

# Red collar
t.penup()
t.goto(-140, 0)
t.pendown()
t.color("red")
t.width(15)
t.goto(140, 0)

# Yellow bell
t.penup()
t.goto(0, -15)
t.pendown()
t.color("yellow")
t.width(3)
t.begin_fill()
t.circle(20)
t.end_fill()

# Bell line
t.penup()
t.goto(-10, -15)
t.pendown()
t.color("black")
t.width(2)
t.goto(10, -15)

# Bell dot
t.penup()
t.goto(0, -5)
t.pendown()
t.dot(6)

# ==================== BODY ====================

# ---------- BODY (wide blue rounded shape) ----------
t.penup()
t.goto(-120, -25)
t.pendown()
t.color("blue")
t.width(3)
t.begin_fill()
t.setheading(-90)
t.forward(180)              # left side down
t.circle(30, 90)            # bottom-left curve
t.forward(180)              # bottom
t.circle(30, 90)            # bottom-right curve
t.forward(180)              # right side up
t.setheading(180)
t.forward(240)              # close top
t.end_fill()

# ---------- WHITE BELLY (big oval on body) ----------
t.penup()
t.goto(0, -210)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(90)
t.end_fill()

# ---------- POCKET (black half circle on belly) ----------
t.penup()
t.goto(-60, -150)
t.pendown()
t.begin_fill()
t.color("black","white")
t.width(3)
t.setheading(0)
t.forward(120)              # straight top of pocket
t.setheading(-90)
t.circle(-60, 180)          # curve going down
t.end_fill()
t.color("black")
# ---------- LEFT ARM (line from body to hand) ----------
t.penup()
t.goto(-120, -60)
t.pendown()
t.color("blue")
t.width(30)                 # thick line = arm
t.setheading(-150)
t.forward(70)

# ---------- RIGHT ARM ----------
t.penup()
t.goto(120, -60)
t.pendown()
t.color("blue")
t.setheading(-30)
t.forward(70)

# ---------- LEFT HAND (white circle) ----------
t.penup()
t.goto(-185, -130)
t.pendown()
t.color("black","white")
t.width(3)
t.begin_fill()
t.circle(25)
t.end_fill()

# ---------- RIGHT HAND ----------
t.penup()
t.goto(185, -130)
t.pendown()

t.width(3)
t.color("black","white")

t.begin_fill()
t.circle(25)
t.end_fill()

# ---------- LEFT LEG (white rounded shape) ----------
t.penup()
t.goto(-60, -235)
t.pendown()
t.color("white")
t.width(3)
t.begin_fill()
t.setheading(-90)
t.forward(25)
t.setheading(0)
t.circle(-30, 180)          # rounded foot bottom
t.setheading(90)
t.forward(25)
t.end_fill()

# Black outline for left leg
t.penup()
t.goto(-60, -235)
t.pendown()
t.color("black")
t.setheading(-90)
t.forward(25)
t.setheading(0)
t.circle(-30, 180)
t.setheading(90)
t.forward(25)

# ---------- RIGHT LEG ----------
t.penup()
t.goto(5, -235)
t.pendown()
t.color("white")
t.begin_fill()
t.setheading(-90)
t.forward(25)
t.setheading(0)
t.circle(-30, 180)
t.setheading(90)
t.forward(25)
t.end_fill()

# Black outline for right leg
t.penup()
t.goto(5, -235)
t.pendown()
t.color("black")
t.setheading(-90)
t.forward(25)
t.setheading(0)
t.circle(-30, 180)
t.setheading(90)
t.forward(25)

# ---------- LITTLE BLUE TAIL/GAP BETWEEN LEGS ----------
t.penup()
t.goto(-3, -235)
t.pendown()
t.color("blue")
t.width(3)
t.begin_fill()
t.setheading(-90)
t.forward(20)
t.setheading(0)
t.forward(8)
t.setheading(90)
t.forward(20)
t.setheading(180)
t.forward(8)
t.end_fill()

t.hideturtle()
turtle.done()