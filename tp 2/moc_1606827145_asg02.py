import string
from htmlFunctions import *

##############################################################################################################################################################################
print('Program to create word cloud from a text file')
print('The result is stored as an HTML file')

while True:                                                     #kalo filnenya salah masukin atau user pencet ctrl+c, bakal terus looping
    try :
        file_input1=input(str("Please enter the file name: "))
        file_input=open(file_input1)
        break
    except FileNotFoundError:
        print('\nFILE NOT FOUND!\nPlease try again\n')
    except KeyboardInterrupt:
        print('\n-__-"\n')

print(file_input1,":")
print('50 words in frequency order as (count:word) pairs')

stop = open("stopWords.txt",'r')
new_stop = ''
for line in stop:                                               #loop buat ngilangin tab di stopword
    for word in line :
        if word == '    ':
            line = line.replace(word,'')
    new_stop += line
new_stop = list(new_stop.split('\n'))                           #variabel buat nampung stopword baru
stop.close()

new_text = ''
for line in file_input :                                        #loop buat ngilangin punc dan \n
    for word in line :
        if word in string.punctuation+'\n' and word != "-" and word != "'":
            line = line.replace(word,' ')
        elif word == '-':
            line =  line.replace(word,'')
    new_text += line                                            #variabel buat nampung string tanpa punc dan \n
file_input.close()

new_text = list(new_text.split())                               #buat ngubah string jadi list
new_text = [word.lower() for word in new_text]                  #buat bikin jadi huruf kecil semua

clear = []
for word in new_text:                                           #buat ngilangin stopword dan angka dari list
    if word not in new_stop and not word.isdigit() :
        clear.append(word)
clear.sort()                                                    #buat ngurutin kata sesuai abjad

words = []
countB = 1
for indeks,word in enumerate (clear):
    if indeks < len(clear)-1:                                   #buat selain kata terakhir, samain ke kata selanjutnya
        if word == clear[indeks+1]:                             #kalo sama, count + 1
            countB += 1
        else:                                                   #kalo beda, masukin jumlah dan katanya ke dalam list
            words.append((countB,word))                     
            countB = 1
    else :                                                      #buat kata terakhir, samain ke kata sebelumnya
        if word == clear[indeks-1]:                         
            countB += 1
        else:
            words.append((countB,word))
            countB = 1
            
words.sort()                                                    #buat ngurutin dari jumlah terdikit
words = words[-1:-51:-1]                                        #buat ngambil 50 jumlah terbanyak (dari bawah)
        
for indeks,word in enumerate(words) :
    if indeks%4 == 0:                                           #buat kata yang memunyai urutan kelipatan 4, awal kata di beli enter
        print('\n'+'{:>3d}:{:<13s}'.format(word[0],word[1]),end='')
    else:
        print('{:>4d}:{:<13s}'.format(word[0],word[1]),end='')

##########################################################################################################################################################################
for i,l in enumerate (words):                                   #buat ambil jumlah huruf terbanyak dan terdikit 
    if i == 0:
        Max = int(l[0])
    elif i == len(words)-1:
        Min = int(l[0])

high_count = Max
low_count = Min
body=''
def getKey(item):                                               #fungsi buat ngambil indeks 1 di dalem tuple
    return item[1]
words.sort(key=getKey)                                          #ngurutin kata-kata (indeks 1) dalem tuple
for cnt,word in words:                                          
    body = body + " " + make_HTML_word(word,cnt,high_count,low_count)
box = make_HTML_box(body)                                       # creates HTML in a box
print_HTML_file(box,"A Word Cloud of "+file_input1)             # writes HTML to file name 'testFile.html'

input('\n\nPlease type Enter to continue ...')
