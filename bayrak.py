import turtle
import math

def draw_rectangle(color, width, height):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_circle(x, y, r, color):
    turtle.up()
    turtle.goto(x, y - r)
    turtle.setheading(0)
    turtle.color(color)
    turtle.down()
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

def draw_star(x, y, r, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.setheading(90)
    turtle.color(color)
    turtle.down()
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(r)
        turtle.right(144)
        turtle.forward(r)
        turtle.left(72)
    turtle.end_fill()

# --- ÇİZİM BAŞLANGICI ---

turtle.speed(0)
turtle.bgcolor("white")
turtle.up()
turtle.goto(-300, 200)
turtle.down()

# Bayrak oranları (2:3)
flag_width = 600
flag_height = 400

# 1) KIRMIZI ZEMİN
draw_rectangle("red", flag_width, flag_height)

# 2) HİLAL (Büyük + küçük daire)
R_outer = 80
R_inner = 60
cx = -60
cy = 0

draw_circle(cx, cy, R_outer, "white")
draw_circle(cx + 25, cy, R_inner, "red")

# 3) YILDIZ (küçültülmüş)
star_size = 40    # <<< Burayı küçülttük
star_x = 80
star_y = 15

draw_star(star_x, star_y, star_size, "white")

turtle.hideturtle()
turtle.done()
