from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar


window = Tk()

window.title("Hola mundo")
window.geometry("350x200")

style = Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='black')

bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')

bar['value'] = 10

bar.grid(column=0, row=0)

window.mainloop()