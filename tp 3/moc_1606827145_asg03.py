from tkinter import *                                       #import semua fungsi dalam modul tkinter
from tkinter import messagebox

class Barcode:                                              #nama class
    def __init__(self):                                     #constuktor
        win = Tk()                                          #untuk membuat window
        win.resizable(height=False,width=False)             #agar windows tidak bisa di ubah ukurannya
        win.title("EAN-13 barcode")                         #untuk memberi judul window
        self.canvas = Canvas(win, width=250, height=270, bg='White')        #membuat canvas dengan ukuran tersebut dan bg putih
        
        self.label1 = Label(win, text="Save barccode to PS file [eg:EAN13.eps]:", font='Times 12 normal')
        self.file = Entry(win)                              #memasukan nama file postscript yang akan berisi barcodenya
        self.file.bind("<Return>", self.process)            #saat user menekan tombol enter di kolom ini, maka masuk ke fungsi process
        
        self.label2 = Label(win, text="Enter code (first 12 decimal digits):", font='Times 12 normal')
        self.digit = Entry(win)                             #masukan 12 angka pertama dari barcode yang mau di buat
        self.digit.bind("<Return>", self.process)           #saat user menekan tombol enter di kolom ini, maka masuk ke fungsi process
        
        self.label1.pack()                                  #pack semua atribut
        self.file.pack()
        self.label2.pack()
        self.digit.pack()
        self.canvas.pack()

        win.mainloop()

    def process(self,event):                                    #fungsi untuk membuat barcode
     if self.file.get()[-4:]=='.eps' :                          #jika inputan file seusai format, maka baru lanjut
        digit = self.digit.get()                                #mengambil inputan self.digit
        if len(digit)==12 and digit.isdigit() :                 #jika inputan digitnya benar (panjangnya 12 dan tanpa huruf), maka lanjut
            self.canvas.delete('all')                           #untuk membersihkan canvas
            x = -1                                              #penentu koordinat
            self.canvas.create_text(125, 30, text=" EAN-13 Barcode:", font = 'Helvetica 14 bold')

            genap = ganjil = 0                                  #untuk menghitung angka ke 13
            for i in range(12):
                if i%2: genap+=int(digit[i])                    #jumlahkan setiap angka pada urutan genap
                else :  ganjil+=int(digit[i])                   #jumlahkan setiap angka pada urutan ganjil
            cekdigit = (genap*3+ganjil)%10                      
            if cekdigit != 0: cekdigit = 10-cekdigit                
            else : pass
            digit += str(cekdigit)                              #buat ngenambhin angka ke 13 kedalam digit
            
#########################################################################################################################################
            F_digit = {0:'LLLLLL', 1:'LLGLGG', 2:'LLGGLG', 3:'LLGGGL', 4:'LGLLGG',
                       5:'LGGLLG', 6:'LGGGLL', 7:'LGLGLG', 8:'LGLGGL', 9:'LGGLGL'}
            pola = F_digit[int(digit[0])]                       #menurut angka 1, cari pola untuk 6 angka selanjutnya
        
            L_code = {0:'0001101', 1:'0011001', 2:'0010011', 3:'0111101', 4:'0100011',
                      5:'0110001', 6:'0101111', 7:'0111011', 8:'0110111', 9:'0001011'}
            G_code = {0:'0100111', 1:'0110011', 2:'0011011', 3:'0100001', 4:'0011101',
                      5:'0111001', 6:'0000101', 7:'0010001', 8:'0001001', 9:'0010111'}
#########################################################################################################################################
            for i in range(5):                                  #untuk membuat border yang biru-biru
                if i%2:
                    warna='blue'
                else:
                    warna='white'
                self.canvas.create_rectangle(30+x, 50, 32+x, 220, fill=warna, outline=warna)
                x += 2
#########################################################################################################################################   
            #membuat barkode set1 (2-7)
            for n,i in enumerate (pola):                        #mengambil urutan dan code dari pola set 1(2-7)
                if i == 'L':                                    #jika kodenya L masuk kesini
                    code = L_code[int(digit[n+1])]              #mengngambil code urutan angka ke 2/3/4/5/6/7
                    for i in code:
                        if i == '0':
                            warna = 'white'
                            self.canvas.create_rectangle(30+x, 50, 32+x, 205, fill=warna, outline=warna)
                            x += 2                      
                        else:
                            warna = 'red'
                            self.canvas.create_rectangle(30+x, 50, 32+x, 205, fill=warna, outline=warna)
                            x += 2
                else :                                          #jika kodenya G masuk kesini
                    code = G_code[int(digit[n+1])]
                    for i in code:
                        if i == '0':
                            warna = 'white'
                            self.canvas.create_rectangle(30+x, 50, 32+x, 205, fill=warna, outline=warna)
                            x += 2
                        else:
                            warna = 'red'
                            self.canvas.create_rectangle(30+x, 50, 32+x, 205, fill=warna, outline=warna)
                            x += 2 
#########################################################################################################################################                        
            for i in range(5):                                  #untuk membuat border yang biru-biru
                if i%2:
                    warna='blue'
                else:
                    warna='white'
                self.canvas.create_rectangle(30+x, 50, 32+x, 220, fill=warna, outline=warna)
                x += 2
#########################################################################################################################################        
            digit2 = digit[7:]                                   #karena 7 angka pertama udah di pakai, jadi di ambil 6 angka terakhir
            R_code = {0:'1110010', 1:'1100110', 2:'1101100', 3:'1000010', 4:'1011100',
                      5:'1001110', 6:'1010000', 7:'1000100', 8:'1001000', 9:'1110100'}

            for i in digit2:
                for j in R_code[int(i)]:                        #mengubah tiap angke ke kode-kode yang ada
                    if j == '0':
                        warna = 'white'
                        self.canvas.create_rectangle(30+x, 50, 32+x, 205, fill=warna, outline=warna)
                        x += 2
                    else:
                        warna = 'red'
                        self.canvas.create_rectangle(30+x, 50, 32+x, 205, fill=warna, outline=warna)
                        x += 2
#########################################################################################################################################                        
            for i in range(5):                                  #untuk membuat border yang biru-biru
                if i%2:
                    warna='blue'
                else:
                    warna='white'
                self.canvas.create_rectangle(30+x, 50, 32+x, 220, fill=warna, outline=warna)
                x += 2
#########################################################################################################################################                        
            self.canvas.create_text(23, 214, text=digit[0], font='Calibri 14 bold')
            self.canvas.create_text(162//2, 214, text="{} {} {} {} {} {}".format(digit[1],digit[2],digit[3],digit[4],
                                                                                 digit[5],digit[6]), font='Calibri 14 bold')
            self.canvas.create_text(350//2, 214, text="{} {} {} {} {} {}".format(digit[7],digit[8],digit[9],digit[10],
                                                                                 digit[11],digit[12]), font='Calibri 14 bold')
            self.canvas.create_text(125, 240, text="Check Digit: {}".format(digit[-1]), font='Calibri 16 bold', fill='orange')

            self.canvas.postscript(file=self.file.get())
            
        elif len(digit)!=12 or not digit.isdigit() :messagebox.showerror("ERROR!", "Please enter the input correctly\nerror : digit input")
     else:messagebox.showerror("ERROR!", "Please enter the input correctly\nerror : file name")
                 
Barcode ()
