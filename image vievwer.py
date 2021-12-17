# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 16:44:36 2021

@author: DELL
"""

from tkinter import *

from tkinter import filedialog
from PIL import ImageTk, Image
import os

root = Tk()
root.minsize(650,650)
root.maxsize(10000,10000)
label_image=Label(root, bg="white", highlightthickness=5)
label_image.place(relx=0.5, rely=0.5, anchor=CENTER)

text_file = ""
def openFile():
    global text_file
    text_file = filedialog.askopenfilename(title=" Open Text File", filetypes=[("Image Files","*.jpg *.gif *.jpg *.png *.jpeg")])
    print(text_file)
    im=Image.open(text_file)
    img=ImageTk.PhotoImage(im)
    label_image['image']=img
    img.close()

def rotate():
    global text_file
    im=Image.open(text_file)
    img=ImageTk.PhotoImage(im.rotate(180))
    label_image['image']=img
    img.close()

    
open_button=Button(root,text="Open File", command=openFile)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)
rotate_button=Button(root,text="Rotate Image", command=rotate)
rotate_button.place(relx=0.5,rely=0.03,anchor=CENTER)

root.mainloop()