import turtle
import math

# --- Yardımcı fonksiyonlar ---

def draw_rectangle(color, width, height):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_line(color, x1, y1, x2, y2, thickness):
    turtle.up()
    turtle.goto(x1, y1)
    turtle.down()
    turtle.color(color)
    turtle.width(thickness)
    turtle.goto(x2, y2)
    turtle.width(1)

def draw_star_of_david(center_x, center_y, size, color):
    turtle.color(color)
    turtle.up()
    turtle.goto(center_x, center_y)
    turtle.setheading(90)

    # İki eşkenar üçgen çizilecek
    for angle in [90, 270]:
        turtle.up()
        turtle.goto(center_x, center_y)
        turtle.setheading(angle)
        turtle.forward(size / (3 ** 0.5))
        turtle.setheading(angle - 150)
        turtle.down()
        turtle.begin_fill()
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
        turtle.end_fill()

# --- Çizim başlıyor ---

turtle.speed(0)
turtle.bgcolor("white")

flag_width = 600
flag_height = 400

# Başlangıç noktası (sol üst köşe)
turtle.up()
turtle.goto(-flag_width/2, flag_height/2)
turtle.down()

# 1) Beyaz zemin
draw_rectangle("white", flag_width, flag_height)

# Mavi şerit kalınlığı (resmi orana yakın)
stripe_thickness = 40

# 2) Üst mavi şerit
draw_line("blue",
          -flag_width/2, flag_height/2 - 30,
          flag_width/2,  flag_height/2 - 30,
          stripe_thickness)

# 3) Alt mavi şerit
draw_line("blue",
          -flag_width/2, -flag_height/2 + 30,
          flag_width/2,  -flag_height/2 + 30,
          stripe_thickness)

# 4) Davud Yıldızı (Magen David)
star_size = 150
draw_star_of_david(0, 0, star_size, "blue")

turtle.hideturtle()


def draw_star_of_david(cx, cy, size, color):
    turtle.color(color)
    turtle.up()

    # Bir eşkenar üçgen çizme fonksiyonu
    def draw_triangle(center_x, center_y, side, rotation):
        h = (3 ** 0.5 / 6) * side  # merkeze uzaklık
        turtle.up()
        turtle.goto(center_x, center_y - h)
        turtle.setheading(rotation)
        turtle.down()
        turtle.begin_fill()
        for _ in range(3):
            turtle.forward(side)
            turtle.left(120)
        turtle.end_fill()

    # Üst üste iki üçgen (biri 0°, diğeri 180°)
    draw_triangle(cx, cy, size, 90)  # Yukarı bakan üçgen
    draw_triangle(cx, cy, size, -90)  # Aşağı bakan üçgen


turtle.done()
