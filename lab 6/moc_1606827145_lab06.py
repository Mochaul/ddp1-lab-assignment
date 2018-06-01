def make_new_row(old_row):                  #untuk membuat angka di segitiga pascal
    x = []
    long = len(old_row)+1                   #untuk menambah 1 panjang list old string agar bisa pas di loopnya 
    if long<=2:                             #jika panjang lennya kurang dari 2 masuk kesini
        for i in range (long):
            if i == 0 or i == long-1:       #tambahin angak 1 di ujung2 listnya
                x.append(1)
    else:
        for i in range (long):              
            if i == 0 :                     #tambahin angak 1 di awal listnya
                x.append(1)
            elif i == long-1:               #tambahin angak 1 di ujung listnya
                x.append(1)
            else:
                x.append(old_row[i-1]+old_row[i])   #untuk membuat sum dari indeks list awalnya
    return x

def main ():
    valid = False
    while not valid:                        #untuk memvalidasi inputnya
        try:
            lst=int(input("Enter the height of Pascal's triangle (>2): ")) #masukan tinggi segitiga pascal
            if lst < 3:                     #kalo kurang dari 2 error
                print('Invalid input')
            else:
                valid = True
        except ValueError:
            print('Invalid input')
            
    x = []
    pascal = []
    
    print('[')
    for i in range (lst):                   #untuk membuat list baru yang isinya data pascal
        x = make_new_row(x)
        pascal.append(x)
        print(x,end=',\n')
    print(']')

    spasi = len(' '.join(str(x) for x in pascal[-1]))
    for i in(pascal):
        kalimat = ' '.join(str(x) for x in i)   #membuat isi list jadi string
        print(kalimat.center(spasi))

    input('\nPress Enter to exit...')
    
main()


    
