
a = input(str("lokasi dan nama file input yang anda inginkan(sertakan formatnya, ex:.txt): " ))
b = input(str("lokasi dan nama file output yang anda inginkan(sertakan formatnya, ex:.txt): "))

def putNumber1(line, text):                                 #fungsi untuk membuat nomor 3 digit pada tiap baris teks
    line = str(line)                                        #untuk mengubah dari yang integer ke string
    if len(line)==2:                                        #jika angkanya 2 digit, masuk ke fungsi ini
        line='0'+ line                                      #menambahkan satu angka '0' ke depan angka 2 digit. Lalu masuk ke return
    if len(line)==1:                                        #jika angkanya 1 digit, masuk ke fungsi ini
        line='00'+ line                                     #menambahkan dua angka '0' ke depan angka 1 digit. Lalu masuk ke return
    return(line+'. '+text)                                  #jika angkanya 3 digit, langsung mereturn dengan format 'nomor. teks'

def main():                                                 #fungsi untuk memberi nomor pada tiap baris di teks
    line = 1                                                #variabel untuk menghitung angka tiap baris
    file_input = open(a , "r")                              #membuka dan membaca suatu file
    file_output = open(b , "w")                             #menulis ulang file yang sudah ada atau menulis file baru
    for x in file_input :                                   #loop untuk memberi nomor pada tiap baris teks
        print(putNumber1(line, x),file=file_output,end='')  #menulis nomor. teks di file yang baru
        line += 1                                           #menambahkan 1 nomor pada tiap baris selanjutnya
    file_input.close()                                      #menutup file yang tadi dibuka sebagai input
    file_output.close()                                     #menutup file yang tadi dibuka sebagai output
main()                                                      #jalankan fungsi     
