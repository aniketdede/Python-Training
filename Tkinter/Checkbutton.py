import tkinter
from tkinter import *
master = tkinter.Tk()
master.geometry("300x250")
master.title("My Window")
master['bg'] = "#BEEFFF"  

var1 =IntVar()

checkbutton1 = Checkbutton(master, text="Python", variable=var1).grid(row=1, sticky=W)

var2 =IntVar()

checkbutton2 = Checkbutton(master, text="Java", variable=var2).grid(row=5, sticky=W)

mainloop()
