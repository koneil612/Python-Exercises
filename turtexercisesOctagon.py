from turtle import *

def draw_octagon():
    for i in range(5):
        forward(50)
        right(45)
        forward(50)
        right(45)

if __name__ == "__main__":

    draw_octagon()
    up()

    mainloop()
