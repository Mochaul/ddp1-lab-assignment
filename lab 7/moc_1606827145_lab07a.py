# ********************************************************
#   lab07a.py
#
#   Recursively translates words into digits
# ********************************************************

def main():
    words = input("Please give a sequence of words: ")  # asking for input 
    listOfWords = words.split()                         # split kata-kata inputan, dan masukan ke list
    showDigits(listOfWords)                             # memanggil fungsi showDigit untuk ngeprint translatean

# Recursive function for translating a list of numeric words 
# into a sequence of digits(including a point) and print them
def showDigits(listOfWords): 
    if len(listOfWords) == 1:                           # base case
        printDigit(listOfWords[0])                      # memanggil fungsi printDigit untuk mentranslate kata  
    else:                                               # recursive case
        printDigit(listOfWords[0])                      # memanggil fungsi printDigit untuk mentranslate kata  
        showDigits(listOfWords[1:])                     # buang kata yang sudah di print di atas
        
# Function for translating one word and printing the digit or point
def printDigit(word):
#use a dictionary
    Dictio = {"nol":"0", "satu":"1", "dua":"2", "tiga":"3", "empat":"4", \
             "lima":"5", "enam":"6", "tujuh":"7", "delapan":"8", \
             "sembilan":"9", "titik":"."}               # dictionary untuk mentranslate kata menjadi huruf atau simbol
    print (Dictio[word], end='')                        # print kata yang sudah di translate
    
main()                                                  #memanggil fungsi main
