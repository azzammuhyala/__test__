# @azzammuhyala - Bro, 

# ini cuma cara bikin animasi percikan aja..

import turtle as t
import time as tm

def start():
    # bikin garis ke atas
    t.penup()
    t.speed(2)
    t.pencolor('green')
    t.pensize(3)
    t.setheading(90)
    t.goto(0, -100)
    t.pendown()
    t.forward(200)
    t.penup()

def boom():
    n = 30
    l = []

    screen = t.Screen()
    screen.delay(0)

    for i in range(n):
        p = t.Turtle()
        p.penup()
        p.hideturtle()
        p.speed(0)
        p.pensize(3)
        p.pencolor('red')
        p.setheading(360/n * i)
        # ke tengah percikan
        p.goto(0, 100)
        p.pendown()
        # idk
        l.append(p)

    # cara 1:
    for i in range(10):
        for p in l:
            p.forward(10)

    # cara 2:
    # with screen.no_animation():
    #     for i in range(30):
    #         for p in l:
    #             p.forward(5)
    #         tm.sleep(0.016)
    #         screen.update()

start()
boom()
t.mainloop()
