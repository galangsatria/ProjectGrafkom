"""
Nama : Mohamad Alghaz Hernanda
NPM : 140810190069
Praktikium : Grafika Komputer

"""

import turtle

emotion = input('How are you? (s = sad, h = happy) ')

s = turtle.Screen() #memunculkan window turtle
s.bgcolor("White") #window color
s.title("Tugas Turtle Penguin") #Judul window
s.setup(width=600, height=600) #ukuran window

t = turtle.Turtle(shape='turtle')
t.color('orange','yellow') #memberikan warna 

t.begin_fill()
t.circle(100) #membuat lingkarang dengan ukuran 100
t.end_fill()
t.penup


t.color('black','red') #memberikan warna 
#membuat mata kiri
t.goto(-30,135) 
t.pendown()
t.dot(25) #membuat matanya besar
t.penup()


#membuat mata kanan
t.goto(30,135) 
t.pendown()
t.dot(25) #membuat matanya besar
t.penup()

#mulut
#jika memilih 'h' maka mulutnya akan senyum, jika meilih s maka mulutnya akan sedih
if emotion == 'h':
    t.goto(-60,60) #membuat mulut di koordinat -60,60
    t.pendown()
    t.setheading(-60)
    t.circle(70,120)
else:
    t.goto(60,60) #membuat mulut di koordinat 60,60
    t.pendown()
    t.setheading(120)
    t.circle(70,120)



turtle.done()
