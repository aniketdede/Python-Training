import tkinter
from tkinter import *
root = tkinter.Tk()
root.title("color options in tkinter")

button=Button(root, text = "click me", activebackground="blue",activeforeground="white")
button.pack()

label=Label(root, text="Hellp Thinker!", bg="lightgray", fg="black")
label.pack()

entry=Entry(root, selectbackground="lightblue",selectforeground="black")
entry.pack()
mainloop()