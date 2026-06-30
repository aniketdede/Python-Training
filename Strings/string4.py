import tkinter as tk 
from tkinter import *
import tkinter.font as font
from tkinter import messagebox
from models.Store import Store
from models.ShoppingCart import ShoppingCart


    
def viewStore():
    
    global storeWindow
    storeLabelFrame = LabelFrame (storeWindow, text = "Store items")
    storeItemsFrame.pack(padx = "10", pady ="5")
    store = store()
    storeItems = store.getStoreItems()
    for item in storeItems :
        itemFrame = Frame (storeItemsFrame, pady="5")
        itemFrame.pack(fill="both",expand="yes")
        
nameLabel = Label (itemFrame,text=item.name,font = ("candera",15),fg = "blue")
priceLabel = Label (itemFrame,text = "$%s"%item.price,font=("candera",13),fg="red")
addToCartbtn = Button ( itemframe,text="add to cart ", cursor="hand2",command=lambda i = item: addItemToCart(i))
btnImage = PhotoImage(file="images/addToCart.png")
addToCartbtn.image = btnImage
addToCartbtn.config(image=btnImage, width="40",height="40")

nameLabel.pack(side="left")
priceLabel.pack(side="left",fill="both",expand="yes")
addToCartbtn.pack(side="right")

btnGoCart = Button(storeWindow,Text = "go to Cart",font=("candera",14),fg="red",bg="white",cursor="hand2",command=viewCart)
btnGoCart.pack(pady="6")

def viewCart():
    cartWindow = Toplevel()
    cartWindow.title ("the cart") 
    cartWindow.grab_set()
    global cart 
    cartItems = cart.getCartItems
    
    
CartItemsLabelFrame = LabelFrame(cartWindow,text="Cart Items")
CartItemsLabelFrame.pack(fill="both",expand="yes",padx="20",pady="10")


CartItemsLabelFrame = Frame (CartItemsLabelFrame,padx=3,pady=3)
cartItemsFrame.pack()
index = 0
for item in cartItems:
       itemFrame = Frame(CartItemsFrame,pady="5")