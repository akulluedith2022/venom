#import pyqrcode
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import set
from set import diction
from set import init
from set import *

init()
diction={}
global i
i=0

#start function
def onClick():
    if(root.entry1.index("end")!=0 and root.entry2.index("end")!=0):
        diction[pd.get()]=txt.get()
        items=iter(diction)
        print(diction)
        #print(next(items))
    else:
        print("field null")
def nextWindow():
    os.system("newWindow.py")
    
def createWidgets():
    text1=Label(
        root,
        text="Generate a secure QRCode for your text!",
        fg="white",
        bg="SteelBlue3")
    text1.grid(row=1,column=1,pady=7, padx=14)

    label1=Label(root,
        text="Enter your text: ",
        fg="white",
        bg="SteelBlue3")
    label1.grid(row=2,column=0,pady=7,padx=30)

    root.entry1=Entry(root,width=65,textvariable=txt)
    root.entry1.grid(row=2,column=1,pady=7, padx=14)

    label2=Label(root,
        text="Password: ",
        fg="white",
        bg="SteelBlue3")
    label2.grid(row=3,column=0,pady=7,padx=30)

    root.entry2=Entry(root,width=65,textvariable=pd)
    root.entry2.grid(row=3,column=1,pady=7, padx=14)

    button1=Button(root, 
        text="add items", 
        command=onClick, 
        width=15)
    button1.grid(row=4, column=0,pady=7)

    button2=Button(root, 
        text="generate QRCodes", 
        command=nextWindow, 
        width=15)
    button2.grid(row=4, column=1,pady=7)

root=tk.Tk()

root.title("QRCode generator")
root.geometry("1000x1000")
root.config(background="SteelBlue3")

global txt
txt=StringVar()
global pd
pd=StringVar()

createWidgets()
root.mainloop()