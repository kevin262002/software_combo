from tkinter import *
from tkinter import messagebox

top=Tk()
top.geometry('250x250')
top.title("Login System")

def login():
    username = t1.get()
    password = t2.get()

    messagebox.showinfo("Login Details", f"Username: {username}\nPassword: {password}")


l1=Label(top,text='User Name :')
l1.grid(row=0,column=0)

t1=Entry(top)
t1.grid(row=0,column=1)

l2=Label(top,text='Password :')
l2.grid(row=1,column=0)

t2=Entry(top,show="*")
t2.grid(row=1,column=1)

b1=Button(top,text='Submit',command=login)
b1.grid(row=2,column=1)

top.mainloop()
