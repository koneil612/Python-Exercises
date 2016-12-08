from turtle import *
import random
from turtexercisesShapes import draw_Circle
from turtexercisesShapes import draw_Star

screensize(400, 600, 'navy')

def move():
    up()
    right(45)
    forward(200)
    down()

def draw_rand_star():
    fillcolor('yellow')
    begin_fill()
    draw_Star()
    end_fill()


fillcolor('white')
begin_fill()
draw_Circle()
end_fill()
move()

draw_rand_star()
# move()

mainloop()
