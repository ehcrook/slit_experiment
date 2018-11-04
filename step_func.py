#code for the step functionality
#showing the particles being added one by one
#basically a simulation of the slit experiment

from tkinter import *

class MyApp(object):    #coding a class makes coding for buttons easier
    def __init__(self, parent):
        self.parent = parent
        self.main_frame = Frame(self.parent)        ##root is the parent of main_frame
        self.main_frame.pack()               ##won't be visible unless packed
        
        self.top_frame = Frame(self.main_frame)
        self.top_frame.pack(side = TOP)
        self.bottom_frame = Frame(self.main_frame)
        self.bottom_frame.pack(side = BOTTOM)
        
        self.canvas = Canvas(self.top_frame, height = 400, width = 400)
        self.canvas.pack()
        
        self.button1 = Button(self.bottom_frame, text = '+1 Particle', command = self.p1)
        self.button1.pack(side = LEFT)
        
        self.button2 = Button(self.bottom_frame, text = '+100 Particles', command = self.-100)
        self.button2.pack(side = RIGHT)
        
    def terminate(self):
        self.parent.destroy() #may he rest in pieces
        
    def p1(self):
        continue
        
    def p100(self):
        x = 0
        while(x < 100):
            self.p1
            x += 1

def step():
    continue


if __name__ == "__main__":
    root = Tk()
    myapp = MyApp(root)
    
    root.mainloop()