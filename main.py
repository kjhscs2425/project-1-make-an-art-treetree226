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
#i is what moves symmetrical things 
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
#HERES THE FUCKING PROBLE 
turtle.forward(30)
turtle.pendown()
       
turtle.right(110)
turtle.forward(70)
turtle.right(120)
turtle.forward(80)



turtle.exitonclick()