#untuk mengimport modul turtle
import turtle

#untuk memberi warna biru pada bidang yang akan dibuat
turtle.color('blue')

#untuk memasukan jumlah sisi bidang yang ingin dibuat
a = input("Number of sides that you want: ")#input masih dalam bentuk string
sisi = int(a)#input sudah diubah dalam integer

#untuk memasukan panjang sisi bidang yang ingin dibuat
p = input("How length of each side? ")#input masih dalam bentuk string
panjang = int(p)#input sudah diubah dalam integer

#fungsi untuk pengulangan sebanyak "sisi" bidang yang ingin dibuat
for x in range(sisi):
    turtle.forward(panjang)#untuk membuat sisi sesuai panjang yang diinginkan
    turtle.right(360/sisi)#untuk membuat sudut sisi simetris
turtle.hideturtle()#untuk menghilangkan pointer turtle
turtle.exitonclick()#untuk keluar dari jendela turtle graph






