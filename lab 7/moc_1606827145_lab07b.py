# lab07b.py
#This program draws a Sierpinski fractal figure
from turtle import *                # mengimport modul turtle
import random                       # mengimport modul random
right(30)                           # membelokan turtle 
def sierpinski(length, depth):      # untuk menggambar segitiga sierpinski fractal
    if depth == 1:                  
        colormode(255)              
        r = int(random.random()*255)
        g = int(random.random()*255)
        b = int(random.random()*255)
        color(r,g,b)                # untuk memberi warna random pada segitiga
        
    if depth > 1: dot()             # mark position to better see recursion
    if depth == 0:                  # base case 
        stamp()                     # stamp a triangular shape
        
    else:                           
        forward(length)
        sierpinski(length/2, depth-1) # recursive call
        backward(length)
        left(120)
        forward(length)
        sierpinski(length/2, depth-1) # recursive call
        backward(length)
        left(120)
        forward(length)
        sierpinski(length/2, depth-1) # recursive call
        backward(length)
        left(120)
    
#create a drawing screen
ts = getscreen()                    # menampilkan screen turtle
ts.title("Colorful Sierpinski Fractal")
speed(0)                            # membuat turtle berjalan dengan kecepatan maksimum
sierpinski(200,6)                   # panjang dan tingkatan pusat segitiga telah diatur
hideturtle()                        # menyembunyikan turtle saat sudah selesai
ts.exitonclick()                    # keluar dari screen turtle saat di klik
