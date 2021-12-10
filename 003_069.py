"""
Nama    : Muhammad Galang Satria
          Mohamad Alghaz Hernanda
NPM     : 140810190003
          140810190069
Kelas   : Praktikum Grafika Komputer
Materi  : Membuat animasi  dengan turtle mainloop
"""

import turtle #memanggil library turtle

win = turtle.Screen() #memunculkan window turtle
win.bgcolor("lightblue") #window color
win.title("Tugas Animation dengan Mainlooop") #Judul window
win.setup(width=700, height=700) #ukuran window

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