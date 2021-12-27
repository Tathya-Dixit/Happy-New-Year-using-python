import turtle as turt
import random
turt.bgcolor("black")
turt.speed("normal")
turt.hideturtle()
def happy():
    turt.penup()
    turt.goto(-450,200)
    turt.pensize(15)
    turt.pencolor("brown")
    #H
    turt.lt(90)
    turt.pendown()
    turt.fd(100)
    turt.bk(50)
    turt.rt(90)
    turt.fd(50)
    turt.penup()
    turt.rt(90)
    turt.bk(50)
    turt.pendown()
    turt.fd(100)
    turt.lt(90)
    turt.penup()
    turt.fd(20)
    #A
    turt.lt(75)
    turt.pendown()
    turt.fd(106)
    turt.rt(150)
    turt.fd(106)
    turt.penup()
    turt.bk(55)
    turt.rt(105)
    turt.pendown()
    turt.fd(25)
    turt.penup()
    turt.bk(25)
    turt.lt(105)
    turt.fd(55)
    turt.lt(75)
    turt.fd(20)
    #P
    turt.lt(90)
    turt.pendown()
    turt.fd(100)
    turt.lt(90)
    turt.circle(25,-180)
    turt.penup()
    turt.lt(90)
    turt.bk(50)
    turt.rt(90)
    turt.fd(45)
    #P
    turt.lt(90)
    turt.pendown()
    turt.fd(100)
    turt.lt(90)
    turt.circle(25,-180)
    turt.penup()
    turt.lt(90)
    turt.bk(50)
    turt.rt(90)
    turt.fd(45)
    #Y
    turt.fd(10)
    turt.lt(90)
    turt.pendown()
    turt.fd(50)
    turt.lt(15)
    turt.fd(55)
    turt.bk(55)
    turt.rt(30)
    turt.fd(55)
    turt.penup()
def new():
    turt.pencolor("brown")
    turt.home()
    turt.goto(-200,0)
    turt.lt(90)
    #N
    turt.pendown()
    turt.fd(100)
    x=180-27
    turt.rt(x)
    turt.fd(111.8)
    turt.lt(x)
    turt.fd(100)
    turt.penup()
    turt.bk(100)
    turt.rt(90)
    turt.fd(20)
    #E
    turt.pendown()
    turt.fd(50)
    turt.penup()
    turt.lt(90)
    turt.fd(100)
    turt.lt(90)
    turt.pendown()
    turt.fd(50)
    turt.lt(90)
    turt.fd(100)
    turt.bk(50)
    turt.lt(90)
    turt.fd(50)
    turt.penup()
    turt.fd(20)
    #w
    turt.rt(90)
    turt.fd(50)
    turt.lt(180)
    turt.fd(100)
    turt.pendown()
    turt.bk(100)
    turt.rt(30)
    turt.fd(50)
    turt.rt(120)
    turt.fd(50)
    turt.lt(150)
    turt.fd(100)
def year():
    turt.pencolor("brown")
    turt.penup()
    turt.goto(50,-200)
     #Y
    
    turt.pendown()
    turt.fd(50)
    turt.lt(15)
    turt.fd(55)
    turt.bk(55)
    turt.rt(30)
    turt.fd(55)
    turt.penup()
    turt.rt(165)
    turt.fd(100)
    turt.lt(90)
    turt.fd(20)
    #E
    turt.pendown()
    turt.fd(30)
    turt.penup()
    turt.lt(90)
    turt.fd(100)
    turt.lt(90)
    turt.pendown()
    turt.fd(30)
    turt.lt(90)
    turt.fd(100)
    turt.bk(50)
    turt.lt(90)
    turt.fd(30)
    turt.penup()
    turt.fd(20)
    turt.rt(90)
    turt.fd(50)
    turt.lt(90)
    #A
    turt.lt(75)
    turt.pendown()
    turt.fd(106)
    turt.rt(150)
    turt.fd(106)
    turt.penup()
    turt.bk(55)
    turt.rt(105)
    turt.pendown()
    turt.fd(25)
    turt.penup()
    turt.bk(25)
    turt.lt(105)
    turt.fd(55)
    turt.lt(75)
    turt.fd(20)
    #P
    turt.lt(90)
    turt.pendown()
    turt.fd(100)
    turt.lt(90)
    turt.circle(30,-180)
    turt.rt(50)
    turt.fd(50)
    turt.penup()
def fireworks():
    turt.penup()
    colors = ("light yellow", "light pink", "light blue", "grey")
    color = random.choice(colors)
    color2 = random.choice(colors)
    turt.pensize(2)
    turt.showturtle()
    turt.speed(0)
    x = random.randrange(-550,550)
    y = random.randrange(-300,300)
    turt.goto(x,y)
    turt.color(color, color2)
    turt.pendown()
    turt.begin_fill()
    f = random.randrange(50,200)
    for i in range(36):
        # turt.stamp()
        turt.forward(f)
        turt.left(170)
turt.speed(0)
for i in range(200):
    x = random.randrange(-550,550)
    y = random.randrange(-300,300)
    turt.pencolor("white")
    turt.penup()
    turt.goto(x,y)
    turt.pendown()
    turt.circle(2)
turt.shape("turtle")
for i in range(11):
    fireworks()
turt.hideturtle()
turt.speed(3)

happy()
new()
year()
while True:
    turt.forward(200)
    turt.left(170)
