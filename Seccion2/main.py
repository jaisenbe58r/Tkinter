from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title("Hola mundo")
window.geometry("350x200")

combo = Combobox(window)
combo["values"] = (1, 2, 3, 4, 5, "Text")
combo.current(1)
combo.grid(column=0, row=0)


window.mainloop()