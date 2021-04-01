#it's work
from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()

root.title('Digital Clock')
def clock():
    tick = strftime('%H:%M:%S %p')
    Label.config(text = tick)
    Label.after(1000, clock)
Label = Label(root,font=('sans',80),background='red',foreground='black')
Label.pack(anchor='center')
clock()
mainloop()