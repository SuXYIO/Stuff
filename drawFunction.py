import turtle as tur
from math import *

#GraphQuadrant
def graphquadrant(xlim: int, ylim: int, color):
    # Init
    tur.speed(0)
    tur.color(color)
    tur.hideturtle()
    # Draw
    tur.goto(xlim, 0)
    tur.goto(-xlim, 0)
    tur.goto(0, 0)
    tur.goto(0, ylim)
    tur.goto(0, -ylim)
    tur.goto(0, 0)

#GraphFuncion
def graphfunc(f_x: str, lower: int, upper: int, step: float, amp: float, color):
    # Init
    tur.speed(0)
    tur.color(color)
    tur.hideturtle()
    tur.up()
    x = lower
    tur.goto(lower * amp, eval(f_x) * amp)
    tur.down()
    # Calc & Graph
    while x <= upper:
        y = eval(f_x)
        tur.goto(x * amp, y * amp)
        x += step
    return 0

if __name__ == '__main__':
    lower = -32
    upper = 32
    step = 0.1
    amp = 32
    graphquadrant(lower * amp, lower * amp, 'black')
    graphfunc('sinh(x)', lower, upper, step, amp, 'black')
    tur.exitonclick()
