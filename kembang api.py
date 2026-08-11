# @azzammuhyala - Bro, 

import turtle as t
import time as tm

def start():
    t.penup()
    t.speed(2)
    t.pencolor('green')
    t.pensize(10)
    t.setheading(90)
    t.goto(0, -100)
    t.pendown()
    t.forward(200)
    t.penup()

def boom():
    t.pencolor('red')
    # 2 method ini penting biar penebaran apinya natural
    t.tracer(0)
    t.speed(0)
    n = 20
    for i in range(1, 21):
        for j in range(n):
            t.penup()
            t.goto(0, 100)
            t.setheading(360/n * j)
            t.pendown()
            t.forward(i * 10)
        tm.sleep(0.016) # kasih delay biar keliatan animasinya (60 FPS)
        t.update() # perbarui kanva (kayaknya)

start()
boom()
t.mainloop()
