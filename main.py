import turtle 

turtle.speed(20)

#big parts
turtle.pensize(5) 
turtle.circle(80)
turtle.penup()
turtle.backward(55)
turtle.left(90)
turtle.backward(20)
turtle.pendown()
turtle.circle(150)

#eyes

x=40
#x is what moves symmetrical body part components slgihtly apart from their counterpart. it can help move an eye, leg, or an ear. throughout the code, x only equals 40.
turtle.pensize(3)
for i in range (2):
    turtle.penup()
    turtle.forward(110)
    turtle.right(90)
    turtle.forward(30-x)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()

# first ear
turtle.penup()
turtle.backward(60)
turtle.right(70)
turtle.forward(120)
turtle.pendown()

turtle.right(110)
turtle.forward(70)
turtle.right(120)
turtle.forward(65)

#second ear
turtle.penup()
turtle.forward(x-2)
turtle.left(150)

turtle.forward(25)
turtle.pendown()
       
turtle.right(110)
turtle.forward(70)
turtle.right(120)
turtle.forward(45)

#nose
turtle.penup()
turtle.left(20)
turtle.forward(60)
turtle.right(90)
turtle.forward(40)
turtle.pendown()

def flatoval(r):               
    turtle.right(45)
    for loop in range(2):
        turtle.circle(r,90)
        turtle.circle(r/2,90)
flatoval(40)


#nostrils
turtle.penup()
turtle.right(90)
turtle.backward(20)
turtle.right(90)
turtle.forward(5)
turtle.left(90)
turtle.pendown()

turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.left(120)
turtle.forward(30)
turtle.pendown()

turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

#legs
def first_leg():
    turtle.pendown()
    turtle.right(20)
    turtle.forward(50)
    turtle.right(140)
    turtle.forward(40)
    turtle.penup()


turtle.penup()
turtle.forward(80)
turtle.left(90)
turtle.forward(252)

first_leg ()

turtle.left(90)
turtle.forward(x+70)
turtle.right(90)
turtle.forward(15)

# print(turtle.position())

turtle.forward(45)
turtle.left(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(25)
turtle.backward(90)
turtle.right(90)
turtle.forward(120)
turtle.left(90)

def other_legs ():
    turtle.right(220)
    turtle.forward(50)
    turtle.right(140)
    turtle.forward(55)

for i in range (2):
    turtle.pendown()
    other_legs ()
    turtle.penup()
    turtle.right(90)
    turtle.forward(15-x)
    turtle.right(106)
    turtle.forward(32-x)
    turtle.left(180)

for i in range (1):
    turtle.pendown()
    other_legs ()
    turtle.penup()
    turtle.right(90)
    turtle.forward(15-x)
    turtle.right(106)
    turtle.forward(32-x)
    turtle.left(180)


#tail
turtle.left(43)
turtle.forward(80)

b=13
#b represents the  variable that moves the circles slightly to the left to draw the pig's tail or spiral. b takes the value of only 13.
turtle.pendown()
turtle.right(90)
turtle.circle(8)
turtle.backward(b)
turtle.circle(8)
turtle.backward(b)
flatoval(10)
 
   











turtle.exitonclick()