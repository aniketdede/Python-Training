import tkinter
from tkinter import messagebox
from tkinter import *
top = tkinter.Tk()
top.geometry("300x200")
top.title("My Window")
top['bg']='#ADD8E6'

def myfun():
    messagebox.showinfo("Information","This is a popup message")
    
    
    
btn1 = Button (top,text= "click here" ,command=myfun).pack()

top.mainloop()    
    