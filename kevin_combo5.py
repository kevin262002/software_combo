from tkinter import *  
import tkinter as tk  
from PIL import ImageTk, Image  
  
window = Tk()  
window.resizable()
window.title('Image Viewer') 
Label(window, text = "Image Viewer App", font = ('bold', 20)).pack()

def Forward():  
    global j   
    j = j + 1  
    try:  
        img_label.config(image = imglst[j])  
    except:  
        j = -1  
        Forward()   
  
 
def Backward():  
    global j   
  
    j = j - 1  
    try:  
        img_label.config(image = imglst[j])  
    except:  
        j = 0  
        Backward() 
   

Frames = Frame(window, width = 230, height = 200, bg = 'white')  
Frames.pack()  
  
 
Button(window, text = 'Back', command = Backward, bg= 'light blue').place(x = 240, y = 50)    
Button(window, text = 'Next', command = Forward, bg = 'light blue').place(x = 1010, y = 50)  
  
  
img1 = ImageTk.PhotoImage(Image.open("image1.jpg"))  
img2 = ImageTk.PhotoImage(Image.open("image2.jpg"))  
img3 = ImageTk.PhotoImage(Image.open("image3.jpg"))  
     
imglst = [img1, img2, img3]  
j = 0  
img_label = Label(Frames, image = imglst[j])   
    
img_label.pack()  
   
window.mainloop()  
