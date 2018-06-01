from tkinter import Tk, Canvas, Frame, Button, Label, TOP, BOTTOM, BOTH, LEFT
from tkinter.colorchooser import askcolor
class Scribble(object):
    '''a simple pen drawing application'''
    def __init__(self):

        master=Tk()     #untuk buat window
        master.title('Simple Pen Drawing')  #untuk memberi judul

        # mouse coordinates and the drawing color are instance variables
        self.oldx, self.oldy = 0, 0
        self.color = 'green'

        # create canvas 400X250 and bind mouse event to handlers
        self.canvas = Canvas(master, width=400, height=250, bg='white')
        self.canvas.bind('<Button-1>', self.begin)
        self.canvas.bind('<Button1-Motion>', self.draw)

        self.canvas.pack(expand=True, fill=BOTH)

        # create a new frame for holding the buttons
        frame1 = Frame(master)
        frame1.pack(side=TOP)

        self.bt_clear = Button(master=frame1, text='clear', bg='orange',\
                               command = self.delete)
        self.bt_clear.pack(side=LEFT, padx=5)

        self.bt_color = Button(master=frame1, text='color', bg='green',\
                               command = self.change_color)
        self.bt_color.pack(side=LEFT)

        self.message = Label(master, text='Press and drag the left mouse-button to draw'\
                             ,fg='blue')
        self.message.pack(side=BOTTOM)

        # start the event loop
        master.mainloop()

    def begin(self, event):
        '''handles left button click by recording mouse position
           as the start of the curve'''
        self.canvas.create_line(event.x, event.y, event.x+1, event.y+1,\
                                     fill=self.color, width=1)  #menggambar titid di koordinat mouse
        self.oldx, self.oldy = event.x, event.y      #mengupdate posisi mouse saat pertama kali di klik  
        
    def draw(self, event):
        '''handles mouse motion, while pressing left button, by
           connecting the previous mouse position to the new one'''
        self.canvas.create_line(self.oldx, self.oldy, event.x, event.y,\
                                     fill=self.color, width=1)  #menggambar garis dari koordinat yang lama ke koordinat perpindahan mouse
        self.oldx, self.oldy = event.x, event.y     #mengupdate posisi mouse yang sudah berpidah
        

    def delete(self):
        '''clear the canvas'''
        self.canvas.delete('all')       #menghapus semua gambar yang ada di canvas

    def change_color(self):
        '''change the drawing color using the color chooser,
           also change the background color of the color button'''
        self.color = askcolor()                   #meminta user untuk memasukan warna melalui colorbox
        self.color = self.color[1]                #menggambil warna berdasarkan hexadesimalnya
        self.bt_color.configure(bg=self.color)    #mengupdate self.color sesuai dengan inputan user
        

if __name__ == '__main__':
    Scribble()
