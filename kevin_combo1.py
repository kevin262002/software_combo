from tkinter import *

top=Tk()
top.geometry('500x500')

def text():
    l1.config(text="Hello tkinter")

b1=Button(top,text="click",command=text)
b1.place(x=250,y=250)

l1=Label(top,text='')
l1.place(x=235,y=280)

top.mainloop()
