import turtle

t = turtle.Turtle()

t.shape("turtle")

t.color('red', 'yellow')

t.begin_fill()

while True:t.fd(200)

t.lt(170)

if abs(t.pos()) < 1:

break

t.end_fill()
