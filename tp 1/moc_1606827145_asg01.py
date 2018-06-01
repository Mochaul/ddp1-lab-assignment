import turtle, random                               #import modul turtle dan random 

turtle.getscreen()                                  #munculkan kanvas turtle
turtle.speed(0)                                     #membuat pergerakan turtle menjadi sangat cepat
turtle.title("Colorful Chessboard and Flower")      #membuat judul dari kanvas turtle
turtle.getcanvas()

kotak=int(turtle.numinput("Colorful Chessboard and Flower", "Enter the number of rows: ", minval=2, maxval=25))                  #meminta input jumlah kotak papan catur per barisnya (2<jumlah kotak perbaris<25)
panjang=int(turtle.numinput("Colorful Chessboard and Flower", "Enter the square size (pixels): ", minval=5, maxval=50))          #meminta input panjang dari sisi masing-masing kotak kecil dari papan catur
kelopak=int(turtle.numinput("Colorful Chessboard and Flower", "Enter the number of petals of the flower: ", minval=5, maxval=50))#meminta input jumlah kelopak bunga

turtle.screensize(2*panjang*kotak,2.5*panjang*kotak)#atur ukuran kanvas

turtle.penup()                                      #mengangkat pen turtle
turtle.goto(0,200)                                  #mengarahkan turtle ke koordinat yang ditentukan
turtle.pendown()                                    #menaruh pen turtle

def kotak_kecil():                                  #membuat suatu modul fungsi untuk membuat kotak kecil
    r,g,b = random.uniform(0,1.0),random.uniform(0,1.0),random.uniform(0,1.0) #input warna secara random
    turtle.color(r,g,b)                             #pemberian warna secara random
    turtle.begin_fill()                             #tanda dimulainya pengisian warna
    turtle.forward(panjang)                         #maju sejauh panjang sisi kotak
    turtle.right(90)                                #belok kanan sejauh 90 derajat
    turtle.forward(panjang)
    turtle.right(90)
    turtle.forward(panjang)
    turtle.right(90)
    turtle.forward(panjang)
    turtle.right(90)
    turtle.forward(panjang)
    turtle.end_fill()                               #tanda berakhirnya pengisian warna
        
for i in range (kelopak):                           #fungsi untung meloop sebanyak jumlah kelopak
    turtle.width(2)                                 #mengatur ketebalan garis turtle menjadi 2
    r,g,b = random.uniform(0,1.0),random.uniform(0,1.0),random.uniform(0,1.0)
    turtle.color(r,g,b)
    x = turtle.heading()                            #variabel untuk menampung posisi turtle sebelumnya
    turtle.circle((panjang+kotak)*2, 60)            #menggambar lingkaran dengan jari-jari = (panjang sisi kotak + jumlah kotak)*2 dan sudut 60 derajat)
    turtle.left (120)                               #belok kiri sejauh 120 derajat
    turtle.circle((panjang+kotak)*2, 60)
    turtle.setheading(x)                            #meng-set turtle menjadi sudut sebelumnya
    turtle.left(360/kelopak)                        #belok kiri sejauh (360/banyaknya kelopak) derajat
    
turtle.penup()
turtle.goto(-kotak//2*panjang,180-panjang*3)
turtle.pendown()
turtle.width(1)
for y in range (kotak):                             #fungsi untung meloop sebanyak jumlah kotak
    kotak_kecil()                                   #memanggil def
turtle.right(90)
turtle.forward(panjang)

kotak1 = kotak

while kotak1>0 :                                    #fungsi untuk membuat papan catur secara spiral
    for y in range (kotak1-1):                      #membuat sebaris kotak sebanyak jumlah baris sebelumnya - 1
        kotak_kecil()
    turtle.right(90)
    turtle.forward(panjang)
    for y in range (kotak1-1):                      #membuat sebaris kotak sebanyak jumlah baris sebelum dan sebelumnya - 1
     kotak_kecil()
    turtle.right(90)
    turtle.forward(panjang)
    kotak1-=1

q =str(kotak*kotak)                                 #variabel yang berisi string dari jumlah seluruh kotak papan catur
w =str(kelopak)                                     #variabel yang berisi string dari jumlah seluruh kelopak

turtle.penup()
turtle.goto(0,150-panjang*(3+(kotak+2)))
turtle.pendown()

turtle.color('blue')                                #memberi warna biru pada output tulisan selanjutnya
turtle.write("Colorful Chessboard of "+q+" Squares and Flower of "+w+" Petals",
             align='center', font=('comic sans ms', 16, 'normal')) #membuat tulisan Colorful Chessboard of ... Squares and Flower of ... Petals"

turtle.hideturtle()                                 #menghilangkan tanda kursor turtle
turtle.exitonclick()                                #keluar dari jendela turtel grapich jika diklik di area dalam kanvas
