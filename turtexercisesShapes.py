from turtle import *


def draw_octagon():
    for i in range(5):
        forward(50)
        right(45)
        forward(50)
        right(45)


def draw_triangle():
    for i in range(3):
        forward(100)
        left(120)



def draw_Star():
    for i in range(5):
        forward(100)
        right(144)


def draw_pentagon():
    for i in range(6):
        forward(50)
        right(60)

def draw_Circle():
    for i in range(36):
        right(10)
        forward(10)
        # right(270)
        # right(180)

def draw_square():
    for i in range(4):
        forward(50)
        left(90)
