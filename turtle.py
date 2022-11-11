import turtle
t = turtle.Turtle()
t.shape("turtle")

count = 0
t.lt(30)
for i in range(7):
    t.fd(100); t.fd(-30); t.lt(60); t.fd(30); t.fd(-30);
    t.rt(120); t.fd(30); t.fd(-30); t.lt(60); t.fd(-70); t.lt(60); 
    
    import turtle
t = turtle.Turtle()
t.shape("turtle")
for i in range(10):
    t.forward(-100)
    t.lt(36)
    t.forward(100)
    t.lt(36)
    t.forward(-100)
    t.lt(36)
    t.forward(100)
    t.lt(36)
    t.forward(-100)
    t.rt(134)
    
    import random
import turtle
t = turtle.Turtle()
t.shape("turtle")


for i in range(10):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    z = random.randint(-180, 180)

    t.up()
    t.goto(x, y)
    t.down()
    t.circle(z);

    import turtle
t = turtle.Turtle()
t.shape("turtle")

count = 0

while True:
    t.fd(100); t.rt(90); t.fd(20); t.rt(90); t.fd(100); t.lt(90); t.fd(20);
    t.lt(90);

    count += 1

    if(count == 7):
        break;
        
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

import turtle
import math

t = turtle.Turtle()
t.shape("turtle")

for i in range(360):
    sine = math.sin(math.pi * i / 180.0)
    print(sine)
    t.goto(i, sine * 100)
    
    
