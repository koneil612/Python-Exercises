from turtle import *
from draw_a_square import draw_square

coord_list = [(-100, -100,50), (100, 100,20), (-100, 100,120), (100, -100,200)]

for coord in coord_list:
    up()
    home()
    x,y,size = coord
    setheading(0)
    forward(x)
    setheading(270)
    forward(y)
    down()
    fillcolor('purple')
    begin_fill()
    draw_square(size)
    end_fill()

mainloop()
