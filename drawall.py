from turtle import *
from turtexercisesShapes import draw_Circle
from turtexercisesShapes import draw_Star
from turtexercisesShapes import draw_pentagon
from turtexercisesShapes import draw_octagon
from turtexercisesShapes import draw_square
from turtexercisesShapes import draw_triangle

def move():
    up()
    forward(20)
    right(270)
    forward(20)
    down()

bgcolor('lightpink')

draw_Circle()
move()
draw_Star()
move()
draw_pentagon()
move()
draw_triangle()
move()
draw_octagon()
move()
draw_square()

mainloop()
