print('Lab 03\n')
print('From decimal to hexadecimal')
print('---------------------------')

# read the user's input
myInt = int(input('Give a positive integer in decimal representation: '))

# convert the integer stored in myInt to hex digits
hexstr = ''                             # accumulator for hex digits
temp = myInt
while temp > 0 :                        # loop function
    hexdigit = temp%16                  # search the modulo
    if hexdigit < 10:                   # get one hex digit: 0,1,2,3,4,5,6,7,8,9
        hexstr = str(hexdigit) + hexstr # accommodate the modulo from the befor function
    else :                              # get one hex digit: a, b, c, d, e, f
        hexdigit = chr(87+hexdigit)     # convert a==10, b==11, c==12, d==13, e==14, f==15
        hexstr = hexdigit + hexstr      # accommodate the modulo from the befor function
    temp = temp//16     
print('The hexadecimal representation of',myInt,'is','0x'+hexstr)

print()
print('From hexadecimal to decimal')
print('---------------------------')

# read the hex string from the user

hexstr = input('Give a positive integer in hexadecimal representation: ')

# convert the hex string to a correct decimal integer
temp = hexstr[2:]                       # remove '0x' using string slicing
newInt = 0                              # accumulator for decimal value
power = 0
while len(temp)> 0 :                    # loop fuction
    hexdigitstr = temp [-1]             # get the ridhtmost hex digit
    if 47 < ord(hexdigitstr) < 58 :     # if hexdigitstr is 0/1/2/3/4/5/6/7/8/9 (ord('0')=48 , ord('9')=57)
        LOL = (ord(hexdigitstr)-48)*16**power
    else :
        hexdigitstr = (ord(hexdigitstr)-87)
        LOL = hexdigitstr*16**power
    newInt = newInt + LOL               # add the appropriate power
    temp = temp[:-1]                    # remove the rightmost hex digit
    power +=1
print('The decimal representation of',hexstr,'is',newInt)

print()
print('Thanks for using this program.')
print()
print('Press Enter to continue ...')    # hold the screen display



    
        
        
    
   
