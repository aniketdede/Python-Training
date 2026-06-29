import tkinter
from tkinter import *
top= tkinter.Tk()
top.geometry("400x300")

top['bg']='#ADD8E6'
Label(top,text="Hello World",width="20")
ent = Entry(top).place(x=50,y=50)
top.mainloop()
