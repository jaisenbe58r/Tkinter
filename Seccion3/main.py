from tkinter import *
from tkinter.ttk import *

window = Tk()

window.title("Hola mundo")
window.geometry("350x200")

chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(window, text="Choose", var=chk_state)
chk.grid(column=0, row=0)


window.mainloop()