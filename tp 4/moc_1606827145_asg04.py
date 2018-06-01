# Author : Mochamad Aulia Akbar Praditomo (1606827145)
# Supercalculator
# DDP Before DWP

from tkinter import *
from math import *
#from idlelib.ToolTip import *

class superCalculator:
    def __init__(self):
        self.memory = '0'
        self.startOfNextOperand = True
        self.window = Tk() # Create a window
        self.window.title("Supercalculator [By : MAAP]") # Set a title
        self.window.geometry("350x450")# Adjust the window size
        self.window.resizable(width=False, height=False)# Make the window unresizeable
        self.entry = Entry(self.window,  font = "System 18", width = 22, bg = 'Cadet Blue', bd = 7)
        self.entry.pack()
        self.frame = Frame(self.window)
        self.frame.pack()
        self.window.bind('<Return>',self.equal)
        
        buttons =   [['Clr',     'MC',       'M+',       'M-',       'MR',      'rad',      'π'],
                            ['sin',     'cos',       'tan',       'ln',       '2C',     'x',    'o'],
                            ['+',     '-',       '/',       '*',       '**',     '√',    '~'],
                            ['A',     'B',       '1',       '2',       '3',     '|',    '&'],
                            ['C',     'D',      '4',        '5',        '6',    '.',    '±'],
                            ['E',     'F',      '7',        '8',        '9',    '^',    '%'],
                            ['hex',     'oct',      'bin',        '0',        'int',    '//',   'exp']]

        buttonstt = [['Clear the entry',    'Clear the memory',     'Add memory to the current entry',      'Subtract memory to the current entry',     'Show current memory to entry',     'Convert degree to radian',     'Insert math Phi'],
                            ['Count Sin in rad(add\')\'',       'Count Cos in rad(add\')\'',        'Count Tan in rad(add\')\'',        'Count natural Logarithm(add\')\'',     '32-bit 2\'s Complement',       'Add variable x',       'Add variable o'],
                            ['Add',     'Subtract',     'Divide',       'Multiply',     'Power',        'Square root',      'Bitwise complement'],
                            ['Letter A',        'Letter B',     'Digit 1',      'Digit 2',      'Digit 3',      'Bitwise or',       'Bitwise and'],
                            ['Letter C',        'Letter D',     'Digit 4',      'Digit 5',      'Digit 6',      'Decimal point',        'Toggle +-'],
                            ['Letter E',        'Letter F',     'Digit 7',      'Digit 8',      'Digit 9',      'Bitwise XOR',      'Modulo'],
                            ['Convert into Hexadecimal',        'Convert into Octal',       'Convert into Binary',      'Digit 0',      'Convert into Integer',     'Integer divide',       'Power of E(2.718...)']]
                
        for r in range(7):
            for c in range(7):
                def cmd(x=buttons[r][c]):
                    self.click(x)
                self.b = Button(self.frame, text=buttons[r][c], height = 2, width=5, bg = 'Gray', font = 'Calibri 12 bold',  relief=RAISED, command=cmd) 
                self.b.grid(row = r+1, column = c)
                if self.b['text'] in '0123456789':
                    self.b['bg'] = 'Gainsboro'
                if self.b['text'] in 'ABCDEF':
                    self.b['bg'] = 'Snow'
                if self.b['text'] == 'Clr':
                    self.b['bg'] = 'maroon'
                if self.b['text'] == 'MC' or self.b['text'] == 'M+' or self.b['text'] == 'M-' or self.b['text'] == 'MR':
                    self.b['bg'] = 'dark goldenrod'
                #ToolTip(self.b, buttonstt[r][c])
                
        self.equal = Button(self.window, text='=',height = 2,width=43, bg ='dark goldenrod', font = 'Calibri 12 bold', relief=RAISED, command=self.equal)
        self.equal.pack()
        #ToolTip(self.equal, 'Compute into Decimal')
        
        self.window.mainloop() # Event loop

    def click(self, key):
        if key in '01234567890ABCDEFxo.π':
            if key == 'π':
                key = pi
            self.entry.insert(END, key)
        elif key == 'MC':
            self.memory = '0'
        elif key == 'M+':
            self.memory = str(eval(self.memory+'+'+self.entry.get()))
            self.entry.delete(0,END)
        elif key == 'M-':
            self.memory = str(eval(self.memory+'-'+self.entry.get()))
            self.entry.delete(0,END)
        elif key == 'MR':
            self.entry.delete(0,END)
            self.entry.insert(END,self.memory)
        elif key == 'Clr':
            self.entry.delete(0,END)
        elif key in '+**-//%^|&~':
            self.entry.insert(END,key)
            self.startOfNextOperand = True
        elif key == 'int' or key == 'bin' or key == 'oct' or key == 'hex' or key == 'sin' or key == 'cos' or key == 'tan' or key == 'exp':
            self.entry.insert(END,key+'(')
        elif key == '√':
            self.entry.insert(END,'sqrt(')
        elif key == 'rad':
            self.entry.insert(END,'radians(')
        elif key == 'ln':
            self.entry.insert(END,'log(')
        elif key == '2C':
            if int(self.entry.get()) < 0:
                cmp2 = self.entry.get()
                self.entry.delete(0,END)
                self.entry.insert(END,str(bin((2**31)+int(cmp2))))
            elif int(self.entry.get()) >= 0:
                cmp2 = self.entry.get()
                self.entry.delete(0,END)
                self.entry.insert(END,str(bin((2**31)-int(cmp2))))
        elif key == '±':
            try:
                if self.entry.get()[0] == '-':
                    self.entry.delete(0)
                else:
                    self.entry.insert(0, '-')
            except IndexError:
                pass
        else:
            if self.startOfNextOperand:
                self.entry.delete(0,END)
                self.startOfNextOperand = False
            self.entry.insert(END, key)

    def equal(self,*args):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, END)
            self.entry.insert(END, result)
        except:
            self.entry.delete(0, END)
            self.entry.insert(END, 'Error')


superCalculator()
