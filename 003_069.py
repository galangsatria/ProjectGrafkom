"""
Nama    : Muhammad Galang Satria
          Mohamad Alghaz Hernanda
NPM     : 140810190003
          140810190069
Kelas   : Praktikum Grafika Komputer
Materi  : Membuat animasi  dengan turtle mainloop
"""

import turtle #memanggil library turtle
from tkinter import *
from random import *
import tkinter as tk
import numpy as np





emotion = input('pilih pola? (s = spiral, l = lingkaran, m = mobil) ')

win = turtle.Screen() #memunculkan window turtle
win.bgcolor("lightblue") #window color
win.title("M.Galang Satria (140810190003)\n Mohamad Alghaz Hernanda (140810190069)") #Judul window
win.setup(width=700, height=700) #ukuran windowl



if emotion == 's':
    t = turtle.Turtle() #memasukkan library turtle kedalam variable t
    t.speed(0)
    temp=1
    clrlist=["red","green","red","blue"]
    for i in range(400):
        t.color(clrlist[i%4])
        t.forward(temp)
        t.left(120)
        t.left(1)
        temp=temp+1
    turtle.mainloop()
    turtle.done()
elif emotion == 'l':
    turtle.bgcolor("black")
    turtle.pensize(2)
    turtle.speed(0)

    for i in range(6):
        for colours in ["red","magenta","blue","cyan","green","yellow","white"]:
            turtle.color(colours)
            turtle.circle(120)
            turtle.left(100)
    turtle.hideturtle()
    turtle.mainloop()
    turtle.done()

else:
    t = turtle.Turtle() #memasukkan library turtle kedalam variable t
t.pensize(5) #ukuran garis
t.penup()
t.setx(-200)
t.sety(0)
t.pendown()
t.forward(50)
t.penup()
t.goto(-100,-50)

#Ban mobil
def circle():
    t.pendown()
    t.color('black','red')
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.penup()
circle()
for i in range(10):
    t.penup()
    t.goto(-100,0)
    t.pendown()
    t.left(36)
    t.forward(50)
    t.backward(50)
t.goto(-50,0)
t.pendown()
t.forward(200)
t.penup()
t.goto(200,-50)
circle()
for i in range(10):
    t.penup()
    t.goto(200,0)
    t.pendown()
    t.left(36)
    t.forward(50)
    t.backward(50)

#badan mobil 
t.goto(250,0)
t.pendown()
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.right(60)
t.forward(100)
t.left(60)
t.forward(200)
t.left(60)
t.forward(100)
t.left(120)
t.fillcolor('green')
t.forward(150)
t.left(90)
t.forward(88)
t.backward(88)
t.right(90)
t.forward(150)
t.backward(400)
t.right(90)
t.forward(100)
t.penup()
t.goto(-300,-50)
t.pendown()
t.left(90)

#Membuat jalan
t.forward(700)
t.pendown()
turtle.done()