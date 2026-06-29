import tkinter 
from tkinter import *
top = tkinter.Tk()

top.geometry("400x400")
top.title("Listbox Example")

lb= Listbox(top)

lb.insert(1,"python")
lb.insert(2,"java")
lb.insert(3,"c++")
lb.insert(4,"c#")


lb.pack()

mainloop()

  