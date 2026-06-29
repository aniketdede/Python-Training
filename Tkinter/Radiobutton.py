import tkinter
from tkinter import *
root = tkinter.Tk()
root.geometry("900x600")
root.title("My Window")

v = IntVar()

radiobutton1 = Radiobutton(root, text="Option 1", variable=v, value=1).pack(anchor=W)
radiobutton2 = Radiobutton(root, text="Option 2", variable=v, value=2).pack(anchor=W)

mainloop() 