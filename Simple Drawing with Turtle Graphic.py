import turtle as t
t.title("Simple Drawing_from Choi")

def right():
    t.setheading(0)
    t.forward(10)

def up():
    t.setheading(90)
    t.fd(10)

def left():
    t.setheading(180)
    t.fd(10)
def down():
    t.setheading(270)
    t.fd(10)

def blank():
    t.clear()

def tup():
    t.up()
    
def tdown():
    t.down()

t.shape('turtle')
t.speed(0)
t.onkeypress(right, "Right")
t.onkeypress(up, "Up")
t.onkeypress(left, "Left")
t.onkeypress(down, "Down")
t.onkeypress(blank, "Escape")
t.onkeypress(tup, "t")
t.onkeypress(tdown, "y")
t.listen()
