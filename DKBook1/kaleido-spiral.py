import turtle as t
t.hideturtle()
from itertools import cycle
colours = cycle(['red', 'orange', 'yellow' , 'green' , 'blue' , 'purple'])
def draw_circle(size, angle , shift):
    t.pencolor(next(colours))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(size+5 , angle+1 , shift +1)
t.speed('fast')
t.bgcolor('black')
t.pensize(4)
draw_circle(30,0,1)