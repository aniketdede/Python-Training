import tkinter
from tkinter import *
top = tkinter.Tk()
top.geometry("400x300")
top.title("My Window")
top['bg']='#ADD8E6'
uname = Label(top,text="this is new label").place(x=50,y=50)
top.mainloop()