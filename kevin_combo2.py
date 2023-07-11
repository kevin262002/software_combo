from tkinter import *

ans=""

top=Tk()
top.geometry('230x175')

top.configure(background="light gray")

def press(num):
    global ans

    ans=ans+str(num)

    text1.set(ans)

def equal():
     try:
        global ans

        total = str(eval(ans))
 
        text1.set(total)
        ans = ""
        
     except:
        text1.set(" Error ")
        ans = ""


text1 = StringVar()    

t1=Entry(top,textvariable=text1)
t1.grid(columnspan=4,ipadx=65)

b1=Button(top,text="1",height=1,width=7,bg="white",fg="blue",font="Times 9 italic bold",command=lambda: press(1))
b1.grid(row=2,column=0)

b2=Button(top,text="2",height=1,width=7,bg="white",fg="blue",font="Times 9 italic bold",command=lambda: press(2))
b2.grid(row=2,column=1)

b3=Button(top,text="3",height=1,width=7,bg="white",fg="blue",font="Times 9 italic bold",command=lambda: press(3))
b3.grid(row=2,column=2)

b4=Button(top,text="4",height=1,width=7,bg="white",fg="blue",font="Times 9 italic bold",command=lambda: press(4))
b4.grid(row=3,column=0)

b4=Button(top,text="5",height=1,width=7,bg="white",fg="blue",font="Times 9 italic bold",command=lambda: press(5))
b4.grid(row=3,column=1)

b4=Button(top,text="6",height=1,width=7,bg="white",fg="blue",font="Times 9 italic bold",command=lambda: press(6))
b4.grid(row=3,column=2)

b4=Button(top,text="7",height=1,width=7,bg="white",fg="blue",font="Times 9 italic bold",command=lambda: press(7))
b4.grid(row=4,column=0)

b4=Button(top,text="8",height=1,width=7,bg="white",fg="blue",font="Times 9 italic bold",command=lambda: press(8))
b4.grid(row=4,column=1)

b4=Button(top,text="9",height=1,width=7,bg="white",fg="blue",font="Times 9 italic bold",command=lambda: press(9))
b4.grid(row=4,column=2)

b4=Button(top,text="+",height=1,width=7,command=lambda: press("+"))
b4.grid(row=5,column=0)

b4=Button(top,text="0",height=1,width=7,bg="white",fg="blue",font="Times 9 italic bold",command=lambda: press(0))
b4.grid(row=5,column=1)

b4=Button(top,text="-",height=1,width=7,command=lambda: press("-"))
b4.grid(row=5,column=2)

b4=Button(top,text="*",height=1,width=7,command=lambda: press("*"))
b4.grid(row=6,column=0)

b4=Button(top,text="/",height=1,width=7,command=lambda: press("/"))
b4.grid(row=6,column=1)

b4=Button(top,text="%",height=1,width=7,command=lambda: press("%"))
b4.grid(row=6,column=2)

b4=Button(top,text="=",height=1,width=7,command=equal)
b4.grid(row=7,column=0)




top.mainloop()
