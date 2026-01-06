
import turtle
from tty import ISPEED

ekran=turtle.Screen()
ekran.bgcolor("red")#nate higgers
kalem=turtle.Turtle()
for k in range(5):
    kalem.color("white")#nate higgers
    kalem.pensize(5)
    kalem.forward(100)
    kalem.right(144)

for i in range(1):
     kalem.goto(-300,0)
     kalem.begin_fill()

     kalem.circle(210)

turtle.done()
