"""
Lab 10 Solution
DDP 1 / FPROG 1 -- 2017
L.Y.Stefanus

**Do not distribute**

- draw elastic (rubber) shapes on a canvas by
  a left mouse-click and dragging,
- move the last drawn shape by a right mouse-click,
- for drawing a polygon: first left mouse click gives
  the first vertex, subsequent left mouse clicks give
  the subsequent vertices. Between clicks, mouse motion
  creates rubber lines. Double left mouse clicks give
  the last vertex.
"""

from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import messagebox
import time

class DrawRubberShapes(object):
    def __init__(self):
        window = Tk() # Create a window 
        window.title("Lab 11: Select, Move, and Animate") # Set a title       
        frame1 = Frame(window) # Create and add a frame to window 
        frame1.pack()

        # Create a button for choosing color using a color chooser
        self.fillColor = StringVar()
        self.fillColor.set('red')

        def colorCommand():
            (rgb,color) = askcolor()
            if color != None:
                self.fillColor.set(color)
                colorButton["bg"] = color        
        colorButton = Button(frame1, text = "Color",
            command=colorCommand, bg = self.fillColor.get())
        colorButton.grid(row=1,column=1,columnspan=2)
        
        self.v1 = StringVar()
        rbLine = Radiobutton(frame1, text = "Line", 
            variable = self.v1, value = 'L', 
            command = self.processRadiobutton) 
        rbOval = Radiobutton(frame1, text = "Oval", 
            variable = self.v1, value = 'O', 
            command = self.processRadiobutton)
        rbRectangle = Radiobutton(frame1, text = "Rectangle", 
            variable = self.v1, value = 'R', 
            command = self.processRadiobutton)
        rbPolygon = Radiobutton(frame1, text = "Polygon", 
            variable = self.v1, value = 'P', 
            command = self.processRadiobutton)
        self.v1.set('L')
        
        rbLine.grid(row = 1, column = 3)
        rbOval.grid(row = 1, column = 4)
        rbRectangle.grid(row = 1, column = 5)
        rbPolygon.grid(row = 1, column = 6)

        clearButton = Button(frame1, text = "Clear", bg = 'yellow',
            command = self.clear)        
        clearButton.grid(row=1,column=7)
        
        self.canvas = Canvas(window, width=500, height=400, bg='white')
        self.canvas.pack()
        self.canvas.create_text(65,12,text = 'Press h for help', font='Times 14')
        window.bind('<KeyPress-h>', self.help)                 # h / d
        self.canvas.bind('<ButtonPress-1>', self.onStart)      # click
        self.canvas.bind('<ButtonPress-3>', self.onStart2)
        self.canvas.bind('<B1-Motion>', self.onGrow)           # and drag
        self.canvas.bind('<Double-1>', self.onEnd)             # end polygon
        self.canvas.bind('<B3-Motion>',self.onMove)            # move latest
        self.canvas.bind('<Motion>', self.onMotion)
        window.bind('<KeyPress-d>', self.delete)
        self.canvas.bind('<ButtonPress-2>', self.onAnimation)
        
        self.drawn  = None
        
        self.shape = self.canvas.create_line

        self.points = []

        window.mainloop()
        
    def clear(self):
        self.canvas.delete('all')
        self.canvas.create_text(65,12,text = 'Press h for help', font='Times 14')
        
    def processRadiobutton(self):
            if self.v1.get() == 'L':
               self.shape = self.canvas.create_line
            elif self.v1.get() == 'O':
                self.shape = self.canvas.create_oval
            elif self.v1.get() == 'R':
                self.shape = self.canvas.create_rectangle
            elif self.v1.get() == 'P':
                self.shape = self.canvas.create_polygon

    def help(self, event):
            messagebox.showinfo("Self, Move, Animate", \
"""
Mouse commands:
 Left = Set starting point for polygon
 Left+Drag = Draw new rubber shape
 Double left = End polygon drawing
 Motion = Draw rubber line in polygon drawing
 Right = Select a shape
 Right+Drag = Drag the selected shape
 Middle = Move the selected shape with animation

Keyboard commands:
 d = Delete the selected shape
 h = Help
""")
                
    def onStart(self, event):
        self.start = event
        if self.v1.get() == 'P':
            self.points.append(event.x)
            self.points.append(event.y)
        self.drawn = None

    def onStart2(self, event):
        self.start2 = event

    # elasticity: delete and redraw
    def onGrow(self, event):                 
        canvas = event.widget
        if self.v1.get() != 'P':
            if self.v1.get() == 'L':
                if self.drawn: canvas.delete(self.drawn)
                objectId = self.shape(self.start.x, self.start.y, event.x, \
                                  event.y, fill=self.fillColor.get())
                self.drawn = objectId
            else:
                if self.drawn: canvas.delete(self.drawn)
                objectId = self.shape(self.start.x, self.start.y, event.x, \
                                  event.y, fill=self.fillColor.get(), \
                                  outline=self.fillColor.get())
                self.drawn = objectId

    # finish the polygon vertices input
    def onEnd(self, event):
        if self.v1.get() == 'P' and len(self.points)>1:
            self.canvas.delete('sides')
            objectId = self.canvas.create_polygon(self.points,fill=self.fillColor.get())
            self.drawn = objectId
            self.points = []

    # elasticity in drawing a polygon
    def onMotion(self, event):
        canvas = event.widget
        if self.v1.get() == 'P' and self.points != []:
            if self.drawn: canvas.delete(self.drawn)
            objectId = canvas.create_line(self.points[-2],self.points[-1],\
                            event.x,event.y, fill=self.fillColor.get(), tags = 'sides')
            self.drawn = objectId


    def onMove(self, event):
        self.drawn = self.canvas.find_closest(event.x, event.y)
        if self.drawn:
            canvas = event.widget
            (x1,y1,x2,y2) = canvas.bbox(self.drawn) # get the bounding box
            xmin = min(x1,x2)
            ymin = min(y1,y2)
            centerx = xmin + abs(x2-x1)/2
            centery = ymin + abs(y2-y1)/2
            diffX, diffY = (event.x - centerx), (event.y - centery)
            canvas.move(self.drawn, diffX, diffY)

    def delete(self, event):
        self.drawn = self.canvas.find_closest(event.x, event.y)
        self.canvas.delete(self.drawn)

    def onAnimation(self, event):
        target_x = event.x
        target_y = event.y
        canvas = event.widget
        (x1, y1, x2, y2) = canvas.bbox(self.drawn)
        center_x = ((x1+x2)/2)
        center_y = ((y1+y2)/2)
        while center_x < target_x:
            canvas.move(self.drawn, 1, 0)
            center_x += 1
            canvas.after(10)
            canvas.update()
        while center_x > target_x:
            canvas.move(self.drawn, -1, 0)
            center_x -= 1
            canvas.after(10)
            canvas.update()
        while center_y < target_y:
            canvas.move(self.drawn, 0, 1)
            center_y += 1
            canvas.after(10)
            canvas.update()
        while center_y > target_y:
            canvas.move(self.drawn, 0, -1)
            center_y -= 1
            canvas.after(10)
            canvas.update()
        
        
if __name__ == '__main__': DrawRubberShapes()
