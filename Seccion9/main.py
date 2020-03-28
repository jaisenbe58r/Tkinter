from tkinter import *
from tkinter import Menu

window = Tk()
window.title("Hola Mundo")

menu = Menu(window)

new_item = Menu(menu)
new_item.add_command(label='New')
new_item.add_command(label='View')

menu.add_cascade(label='File', menu=new_item)

new_item1 = Menu(menu)
new_item1.add_command(label='1')
new_item1.add_command(label='2')

menu.add_cascade(label='File1', menu=new_item1)

window.config(menu=menu)
window.mainloop()