import tkinter as tk
from tkinter import *
from set import diction
import qrcode

pwds=list(diction.values())
texts=list(diction.keys())
def createWidgets():
    text=Label(root,
        text="Generate a secure QRCode for your text!",
        fg="white",
        bg="SteelBlue3")
    text.grid(row=1,column=1,pady=7, padx=14)

    lab=Label(root,
        text="Enter the password: ",
        fg="white",
        bg="SteelBlue3")
    lab.grid(row=2,column=0,pady=7,padx=30)

    root.entry=Entry(root,
        width=65,
        textvariable=txt)
    root.entry.grid(row=2,column=1,pady=7, padx=14)

    button1=Button(root, text="add items", command=generateQRCodes, width=15)
    button1.grid(row=4, column=0,pady=7)

def generateQRCodes():
    i=0
    for i in range(len(diction)):
        print(i)
        img=qrcode.make(texts[i])
        #img.save("newqrcodes/images/0000"+i+".png")
    
root=tk.Tk()

root.title("QRCode generator")
root.geometry("1000x1000")
root.config(background="yellow")

global txt
txt=StringVar()
createWidgets()
root.mainloop()