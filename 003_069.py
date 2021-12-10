"""
Nama    : Muhammad Galang Satria
          Mohamad Alghaz Hernanda
NPM     : 140810190003
          140810190069
Kelas   : Praktikum Grafika Komputer
Materi  : Membuat animasi  dengan turtle mainloop
"""

import turtle #memanggil library turtle

emotion = input('pilih pola? (s = spiral, l = lingkaran) ')

win = turtle.Screen() #memunculkan window turtle
win.bgcolor("lightblue") #window color
win.title("Tugas Animation dengan Mainlooop\n") #Judul window
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
else:
    turtle.bgcolor("black")
    turtle.pensize(2)
    turtle.speed(0)

    for i in range(6):
        for colours in ["red","magenta","blue","cyan","green","yellow","white"]:
            turtle.color(colours)
            turtle.circle(100)
            turtle.left(10)
    turtle.hideturtle()
    

