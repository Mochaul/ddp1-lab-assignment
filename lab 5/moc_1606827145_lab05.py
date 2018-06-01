def acronym (phrase):       #fungsi untuk membuat akronim
    result = ''             #variabel untuk menampung akronim
    lst = phrase.split()    #mengsplit frase menjadi kata per kata ke dalam list
    for word in lst:         
        result += word[0]   #mengambil huruf pertama dari tiap kata dan disatukan
    result = result.upper() #mengkapitalkan akronimnya
    return result           #mereturn akronimnya

def main():                 #fungsi untuk mengolah file untuk menambahkan akronimnya
    phrase=''               #untuk menampung frase per frase dari file masukan
    while True:
        try:
            masukan = input("Please enter input file name: ")   #meminta nama file masukan
            masukan = open(masukan) #untuk membuka dan membaca file masukan
            break                   #jika sudah dapat, keluar dari loop
        except FileNotFoundError:   #untuk eror file tidak ditemukan
            print("***The file "+masukan+" doesn't exist.")
            print("***Try again.")
        except KeyboardInterrupt:   #untuk eror ctrl+c
            print("***Keyboard Interrupt. Input file is required.")
       
    while True:
        try:        
            keluaran = input("Please enter output file name: ") #meminta nama file keluaran
            keluaran = open(keluaran,'x') #menulis file yang benar-benar baru
            break
        except FileNotFoundError:
            print("***Output file is required")
            print("***Try again.")
        except KeyboardInterrupt:
            print("***Keyboard Interrupt. Input file is required.")
        except FileExistsError:         #jika nama file yang di masukan sudah ada, minta nama baru 
            print("***The file "+keluaran+" already exists.")
            print("***To avoid overwriting an existing file, try another file name.")

    for line in masukan :               #membaca tiap line di file masukan
        phrase += line                  #membuat variabel baru yang isinya string dari isi file masuakn       
    phrase = phrase.split('\n')         #memisahkan setiap frase berdasarkan enter
    
    for word in phrase:                 #untuk mengambil tiap frase dari dalam list phrase
        akro = acronym(word)            #untuk membuat akronim dari setiap frase yanf di ambil
        print(akro+' = '+word, file=keluaran) #menuliskan 'akronim = frasenya' di file kluaran 

    input("End of the program. Please type Enter to finish...")    

main()

