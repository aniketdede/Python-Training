import tkinter
from tkinter import *

# ===================== WINDOW SETUP =====================
# (same as your new0.py / button.py)
top = tkinter.Tk()
top.geometry("320x480")
top.title("Calculator")
top.resizable(False, False)
top['bg'] = '#1e1e2e'

# ===================== STATE VARIABLE =====================
# StringVar is a special Tkinter variable - when it changes,
# the Label that's linked to it updates AUTOMATICALLY
expression = ""
display_var = StringVar()
display_var.set("0")

# ===================== LOGIC FUNCTIONS =====================

def press(value):
    """Called when any number or operator button is clicked"""
    global expression
    expression += str(value)
    display_var.set(expression)

def calculate():
    """Called when = is pressed"""
    global expression
    try:
        result = str(eval(expression))   # eval() runs the math string
        display_var.set(result)
        expression = result              # so you can keep calculating from result
    except:
        display_var.set("Error")
        expression = ""

def clear():
    """Called when C is pressed"""
    global expression
    expression = ""
    display_var.set("0")

def backspace():
    """Called when ⌫ is pressed - removes last character"""
    global expression
    expression = expression[:-1]        # slice off the last character
    display_var.set(expression if expression else "0")

# ===================== DISPLAY (like your label.py) =====================
# This Label is linked to display_var - it auto-updates when display_var changes
display = Label(
    top,
    textvariable=display_var,  # linked to our StringVar
    font=("Arial", 28, "bold"),
    bg="#2a2a3e",
    fg="white",
    anchor="e",                # right-align the text
    padx=10,
    width=15,
    height=2
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# ===================== BUTTON FACTORY =====================
# Instead of writing Button(...) 20 times, we make a function
# This is the key concept - functions to avoid repetition

def make_button(text, row, col, cmd, color="#3a3a5e", fg="white", colspan=1):
    btn = Button(
        top,
        text=text,
        font=("Arial", 16, "bold"),
        bg=color,
        fg=fg,
        activebackground="#555577",
        relief=FLAT,
        width=5,
        height=2,
        command=cmd            # command is the function to call on click (like your button.py)
    )
    btn.grid(row=row, column=col, columnspan=colspan, padx=4, pady=4, sticky="nsew")
    return btn

# ===================== LAYOUT THE BUTTONS =====================
# Row 1 - Clear, Backspace, operators
make_button("C",   1, 0, clear,               color="#e06c75", fg="white")
make_button("⌫",   1, 1, backspace,            color="#e06c75", fg="white")
make_button("%",   1, 2, lambda: press("%"),   color="#61afef", fg="white")
make_button("/",   1, 3, lambda: press("/"),   color="#61afef", fg="white")

# Row 2 - Numbers 7 8 9 and multiply
make_button("7",   2, 0, lambda: press("7"))
make_button("8",   2, 1, lambda: press("8"))
make_button("9",   2, 2, lambda: press("9"))
make_button("*",   2, 3, lambda: press("*"),   color="#61afef", fg="white")

# Row 3 - Numbers 4 5 6 and minus
make_button("4",   3, 0, lambda: press("4"))
make_button("5",   3, 1, lambda: press("5"))
make_button("6",   3, 2, lambda: press("6"))
make_button("-",   3, 3, lambda: press("-"),   color="#61afef", fg="white")

# Row 4 - Numbers 1 2 3 and plus
make_button("1",   4, 0, lambda: press("1"))
make_button("2",   4, 1, lambda: press("2"))
make_button("3",   4, 2, lambda: press("3"))
make_button("+",   4, 3, lambda: press("+"),   color="#61afef", fg="white")

# Row 5 - 00, 0, decimal, equals
make_button("00",  5, 0, lambda: press("00"))
make_button("0",   5, 1, lambda: press("0"))
make_button(".",   5, 2, lambda: press("."))
make_button("=",   5, 3, calculate,            color="#98c379", fg="white")

# Make columns/rows resize evenly
for i in range(4):
    top.columnconfigure(i, weight=1)
for i in range(6):
    top.rowconfigure(i, weight=1)

# ===================== START THE APP =====================
# (same top.mainloop() you've been using in all files)
top.mainloop()