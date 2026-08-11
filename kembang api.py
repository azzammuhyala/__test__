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
    t.pencolor('red')
    # 2 method ini penting biar penyebaran percikannya natural
    t.tracer(0)
    t.speed(0)
    n = 30
    for i in range(1, 16):
        for j in range(n):
            t.penup()
            # titik awal percikan
            t.goto(0, 100)

            t.setheading(360/n * j)
            t.pendown()
            t.forward(i * 10)
        tm.sleep(0.016) # kasih delay biar keliatan animasinya (60 FPS)
        t.update()      # perbarui kanva

start()
boom()
t.mainloop()
