import tkinter
from tkinter import *

root = tkinter.Tk()
menu=Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_separator()
filemenu.add_command(label='exit',command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label = 'help', menu = helpmenu)
helpmenu.add_command(label='about')
mainloop()
