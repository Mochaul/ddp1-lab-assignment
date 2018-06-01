# Program template for Lab Tutorial 8

import string

# string of all uppercase letters :'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
uppercase = string.ascii_uppercase

# Gather input from the user:
# keyword, input file name, output file name, kind of operation

keyword = input("Enter the secret keyword: ")       #meminta masukan keyword
in_name = input("Enter the input file name: ")      #meminta nama file yang mau diolah
out_name = input("Enter the output file name: ")    #meminta nama file yang akan dihasilkan
operation = input("(E)ncrypt or (D)ecrypt? ")       #meminta jenis operasi yang mau dilakukan

# Read all of the text out of the file.
inf = open (in_name, "r")                           #membuka dan membaca file masukan
text = inf.read()                                   #mengcopy semua isi dari file masukan kebentuk string dan di simpan pada variabel "text"
inf.close()

# Create dictionaries for encryption and decryption
plain = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
sup_list = []
if operation == "E" :               #membuat dictionary untuk encryption 
    for i in keyword:               #untuk ngambil setiap huruf dalam keyword
        new = uppercase[(ord(i)%ord("A")):]+uppercase[:(ord(i)%ord("A"))]   #untuk membuat list berisi urutan abjad baru yang di mulai dari huruf keyword
        dct = dict(zip(plain,new))  #untuk membuat dictionary berisi (abjad lama : abjad baru)      
        sup_list.append(dct)        #masukan dictionarynya ke list

elif operation == "D" :             #membuat dictionary untuk decryption 
    for i in keyword:               #untuk ngambil setiap huruf dalam keyword
        new = uppercase[(ord(i)%ord("A")):]+uppercase[:(ord(i)%ord("A"))]   #untuk membuat list berisi urutan abjad baru yang di mulai dari huruf keyword
        dct = dict(zip(new,plain))  #untuk membuat dictionary berisi (abjad baru : abjad lama)      
        sup_list.append(dct)        #masukan dictionarynya ke list

# Encrypt or decrypt the text string provided by user, letter by letter
result = ''     # accumulate the result of encryption/decryption here
for i in range (1, len(text)+1):    #membaca setiap huruf dalam "text:
    if text[i-1] in uppercase:      #jika huruf, maka masuk ke sini
        letter = text[i-1]          #store huruf tersebut ke sebuah variabel
        i = i%len(keyword)          #mod indeks dari huruf tersebut untuk menentukan kuncinya
        result += sup_list[i-1].get(letter,letter)  #olah huruf tersebut
    else: result+=text[i-1]         #jika selain huruf, masuk kesini

# Save the result to the file
outf = open(out_name,"w")           #menulis file baru
outf.write(result)
outf.close()
