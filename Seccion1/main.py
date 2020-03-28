from tkinter import *

window = Tk()

window.title("Hola mundo")
window.geometry("350x200")

label = Label(window, text="Hello")
# label = Label(window, text="Hello", font=("ArialBold", 50))
label.grid(column=0, row=0)


txt = Entry(window, width=10)
# txt = Entry(window, width=10, state='disabled')
txt.grid(columns=1, row=1)


def clicked():
    res = "Hola " + txt.get()
    label.configure(text=res)

# boton = Button(window, text="Click Me")
# boton = Button(window, text="Click Me", bg="orange", fg="red")
boton = Button(window, text="Click Me", command=clicked)
boton.grid(column=2, row=0)


window.mainloop()