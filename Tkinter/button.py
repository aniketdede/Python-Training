import tkinter
from tkinter import *
top = tkinter.Tk()
top.geometry("400x400")
top.title("My Window")
top['bg']='#ADD8E6'
btn = Button (top,text= "click here" ).place(x=50,y=50)
top.mainloop()