from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext

window = Tk()

window.title("Hola mundo")
window.geometry("350x200")

txt = scrolledtext.ScrolledText(window,width=40,height=10)
txt.insert(INSERT,'You text goes here\n')

txt.grid(column=0,row=0)

window.mainloop()