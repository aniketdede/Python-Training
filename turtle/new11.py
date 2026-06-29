import turtle 

length = 200

t = turtle.Turtle()

for i in range (0,20):
    t.forward(length)
    t.left(90)
    length -= 10
    
    
t.shape("turtle")   
t.color("blue")
turtle.done()
    