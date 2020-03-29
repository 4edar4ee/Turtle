from turtle import *
speed('fast')
width(10)
for n in range(-100, 100):
    r=(100-n)/200
    b=(n+100)/200
    pencolor(r,0,b)
    fd(20)
    rt(n)

exitonclick()
