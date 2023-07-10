from tkinter import *
import random
import time
import mysql.connector

g1=""

top=Tk()
top.geometry('1270x712')

top.title('Restaurant Management System created by Kevin')


topFrame=Frame(top,bd=10,relief=RIDGE)
topFrame.pack(side=TOP)

Title=Label(topFrame,text='Restaurant Management System',font=('arial',30,'bold'),fg='black',bd=9,bg='lightblue',width=51)
Title.grid(row=0,column=0)

bill=Entry(topFrame,font=('arial',10,'bold'),width=30,bd=9)
bill.place(x=1000,y=20)


def reset():
    textReceipt.delete(1.0,END)
    e_pizza.set('0')
    e_sandwich.set('0')
    e_burger.set('0')
    e_frenki.set('0')
    e_dhosa.set('0')
    e_chines.set('0')
    e_chat.set('0')
    e_kulche.set('0')
    e_sizzler.set('0')

    e_colddrink.set('0')
    e_cocktails.set('0')
    e_mojitos.set('0')
    e_shots.set('0')
    e_tea.set('0')
    e_cofee.set('0')
    e_softdrink.set('0')
    e_mocktails.set('0')
    e_water.set('0')

    e_cassata.set('0')
    e_blackforest.set('0')
    e_chocolate.set('0')
    e_butterscotch.set('0')
    e_kesarpista.set('0')
    e_vanilla.set('0')
    e_oreo.set('0')
    e_cremecaramel.set('0')
    e_majestic.set('0')

    textPizza.config(state=DISABLED)
    textSandwich.config(state=DISABLED)
    textBurger.config(state=DISABLED)
    textFrenki.config(state=DISABLED)
    textDhosa.config(state=DISABLED)
    textChines.config(state=DISABLED)
    textChat.config(state=DISABLED)
    textKulche.config(state=DISABLED)
    textSizzler.config(state=DISABLED)

    textColddrink.config(state=DISABLED)
    textCocktails.config(state=DISABLED)
    textMojitos.config(state=DISABLED)
    textShots.config(state=DISABLED)
    textTea.config(state=DISABLED)
    textCofee.config(state=DISABLED)
    textSoftdrink.config(state=DISABLED)
    textMocktails.config(state=DISABLED)
    textWater.config(state=DISABLED)

    textCassata.config(state=DISABLED)
    textBlackforest.config(state=DISABLED)
    textChocolate.config(state=DISABLED)
    textButterscotch.config(state=DISABLED)
    textKesarpista.config(state=DISABLED)
    textVanilla.config(state=DISABLED)
    textOreo.config(state=DISABLED)
    textCremecaramel.config(state=DISABLED)
    textMajestic.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    costofdrinksvar.set('')
    costoffoodvar.set('')
    costofcakesvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')
def totalcost():
    
    global priceofFood,priceofDrinks,priceofCakes,subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
        var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
        var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
        var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
        var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or\
        var26.get() != 0 or var27.get() != 0:

        item1=int(e_pizza.get())
        item2=int(e_sandwich.get())
        item3=int(e_burger.get())
        item4 = int(e_frenki.get())
        item5 = int(e_dhosa.get())
        item6 = int(e_chines.get())
        item7 = int(e_chat.get())
        item8 = int(e_kulche.get())
        item9 = int(e_sizzler.get())

        item10 = int(e_colddrink.get())
        item11 = int(e_cocktails.get())
        item12 = int(e_mojitos.get())
        item13 = int(e_shots.get())
        item14 = int(e_tea.get())
        item15 = int(e_cofee.get())
        item16 = int(e_softdrink.get())
        item17 = int(e_mocktails.get())
        item18 = int(e_water.get())

        item19 = int(e_cassata.get())
        item20 = int(e_blackforest.get())
        item21 = int(e_chocolate.get())
        item22 = int(e_butterscotch.get())
        item23 = int(e_kesarpista.get())
        item24 = int(e_vanilla.get())
        item25 = int(e_oreo.get())
        item26 = int(e_cremecaramel.get())
        item27 = int(e_majestic.get())
        
        priceofFood=(item1*800)+(item2*100)+(item3*300)+(item4*100)+ (item5*500) + (item6 * 300) + (item7 * 80) \
                    + (item8 * 200) + (item9 * 600)

        priceofDrinks=(item10*50)+(item11*150)+ (item12 * 150) + (item13 * 80) + (item14 * 20) + (item15 * 50) \
                      + (item16 * 30) + (item17 * 200) + (item18 * 30)

        priceofCakes=(item19*900)+(item20*875)+ (item21 * 850) + (item22 * 700) + (item23 * 900) + (item24 * 600) \
                     + (item25 * 620) + (item26 * 850) + (item27 * 850)

        costoffoodvar.set(str(priceofFood)+ ' Rs')
        costofdrinksvar.set(str(priceofDrinks)+ ' Rs')
        costofcakesvar.set(str(priceofCakes)+ ' Rs')

        subtotalofItems=priceofFood+priceofDrinks+priceofCakes
        subtotalvar.set(str(subtotalofItems)+' Rs')

        servicetaxvar.set('50 Rs')

        tottalcost=subtotalofItems+50
        totalcostvar.set(str(tottalcost)+' Rs')

    else:
        messagebox.showerror('Error','No Item Is selected')

def receipt():
    global billnumber,date
    x=random.randint(100,10000)
    billnumber='BILL'+str(x)
    date=time.strftime('%d/%m/%Y')
    bill.insert(END,''+billnumber+'  '+date)
   
    if costoffoodvar.get() != '' or costofcakesvar.get() != '' or costofdrinksvar.get() != '':
        textReceipt.delete(1.0,END)
        textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
        textReceipt.insert(END,'************************************************************************************************************\n')
        textReceipt.insert(END,'Items:\t\t Cost Of Items(Rs)\n')
        textReceipt.insert(END,'******************************************************\n')
        if e_pizza.get()!='0':
            textReceipt.insert(END,f'Pizza\t\t\t{int(e_pizza.get())*800}\n\n')

        if e_sandwich.get()!='0':
            textReceipt.insert(END,f'Sandwich\t\t\t{int(e_sandwich.get())*100}\n\n')

        if e_burger.get()!='0':
            textReceipt.insert(END,f'Burger\t\t\t{int(e_burger.get())*300}\n\n')

        if e_frenki.get() != '0':
            textReceipt.insert(END, f'Frenki:\t\t\t{int(e_frenki.get()) *100}\n\n')

        if e_dhosa.get() != '0':
            textReceipt.insert(END, f'Dhosa:\t\t\t{int(e_dhosa.get()) * 500}\n\n')

        if e_chines.get() != '0':
            textReceipt.insert(END, f'Chines:\t\t\t{int(e_chines.get()) * 300}\n\n')

        if e_chat.get() != '0':
            textReceipt.insert(END, f'Chat:\t\t\t{int(e_chat.get()) * 80}\n\n')

        if e_kulche.get() != '0':
            textReceipt.insert(END, f'Kulche:\t\t\t{int(e_kulche.get()) * 200}\n\n')

        if e_sizzler.get() != '0':
            textReceipt.insert(END, f'Sizzler:\t\t\t{int(e_sizzler.get()) * 600}\n\n')

        if e_colddrink.get() != '0':
            textReceipt.insert(END, f'Colddrink:\t\t\t{int(e_colddrink.get()) * 50}\n\n')

        if e_cocktails.get() != '0':
            textReceipt.insert(END, f'Cocktails:\t\t\t{int(e_cocktails.get()) * 150}\n\n')

        if e_mojitos.get() != '0':
            textReceipt.insert(END, f'Mojitos:\t\t\t{int(e_mojitos.get()) * 150}\n\n')

        if e_shots.get() != '0':
            textReceipt.insert(END, f'Shots:\t\t\t{int(e_shots.get()) * 80}\n\n')

        if e_tea.get() != '0':
            textReceipt.insert(END, f'Tea:\t\t\t{int(e_tea.get()) * 20}\n\n')

        if e_cofee.get() != '0':
            textReceipt.insert(END, f'Cofee:\t\t\t{int(e_cofee.get()) * 50}\n\n')

        if e_softdrink.get() != '0':
            textReceipt.insert(END, f'Softdrink:\t\t\t{int(e_softdrink.get()) * 30}\n\n')

        if e_mocktails.get() != '0':
            textReceipt.insert(END, f'Mocktails:\t\t\t{int(e_mocktails.get()) * 200}\n\n')

        if e_water.get() != '0':
            textReceipt.insert(END, f'Water:\t\t\t{int(e_water.get()) * 30}\n\n')

        if e_cassata.get() != '0':
            textReceipt.insert(END, f'Cassata:\t\t\t{int(e_cassata.get()) * 900}\n\n')

        if e_blackforest.get() != '0':
            textReceipt.insert(END, f'Black Forest:\t\t\t{int(e_blackforest.get()) * 875}\n\n')

        if e_chocolate.get() != '0':
            textReceipt.insert(END, f'Chocolate:\t\t\t{int(e_chocolate.get()) * 850}\n\n')

        if e_butterscotch.get() != '0':
            textReceipt.insert(END, f'Butterscotch:\t\t\t{int(e_butterscotch.get()) * 700}\n\n')

        if e_kesarpista.get() != '0':
            textReceipt.insert(END, f'Kesarpista:\t\t\t{int(e_kesarpista.get()) * 900}\n\n')

        if e_vanilla.get() != '0':
            textReceipt.insert(END, f'Vanilla:\t\t\t{int(e_vanilla.get()) * 600}\n\n')

        if e_oreo.get() != '0':
            textReceipt.insert(END, f'Oreo:\t\t\t{int(e_oreo.get()) * 620}\n\n')

        if e_cremecaramel.get() != '0':
            textReceipt.insert(END, f'Cremecaramel:\t\t\t{int(e_cremecaramel.get()) * 850}\n\n')

        if e_majestic.get() != '0':
            textReceipt.insert(END, f'Majestic:\t\t\t{int(e_majestic.get()) * 850}\n\n')

        textReceipt.insert(END,'******************************************************\n')
        if costoffoodvar.get()!='0 Rs':
            textReceipt.insert(END,f'Cost Of Food\t\t\t{priceofFood}Rs\n\n')
        if costofdrinksvar.get() != '0 Rs':
            textReceipt.insert(END,f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n\n')
        if costofcakesvar.get() != '0 Rs':
            textReceipt.insert(END,f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n\n')

        textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
        textReceipt.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
        textReceipt.insert(END, f'Total Cost\t\t\t{subtotalofItems+50}Rs\n\n')
        textReceipt.insert(END,'******************************************************\n')

    else:
        messagebox.showerror('Error','No Item Is selected')

def insert():
    food=textCostofFood.get()
    drink=textCostofDrinks.get()
    cake=textCostofCakes.get()
    sub=textSubTotal.get()
    tax=textServiceTax.get()
    total=textTotalCost.get()
    finalbill=bill.get()
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="restaurant_management"
        )
    
    mycur=mydb.cursor()

    sql="insert into rest_data(bill_no,cost_of_food,cost_of_drinks,cost_of_cakes,sub_total,service_tax,total_cost)values(%s,%s,%s,%s,%s,%s,%s)"

    values=(finalbill,food,drink,cake,sub,tax,total)

    mycur.execute(sql,values)

    mydb.commit()
    

def pizza():
    if var1.get()==1:
        textPizza.config(state=NORMAL)
        textPizza.delete(0,END)
        textPizza.focus()

    else:
        textPizza.config(state=DISABLED)
        e_pizza.set('0')

def sandwich():
    if var2.get()==1:
        textSandwich.config(state=NORMAL)
        textSandwich.delete(0,END)
        textSandwich.focus()

    else:
        textSandwich.config(state=DISABLED)
        e_sandwich.set('0')

def burger():
    if var3.get()==1:
        textBurger.config(state=NORMAL)
        textBurger.delete(0,END)
        textBurger.focus()

    else:
        textBurger.config(state=DISABLED)
        e_burger.set('0')        

def frenki():
    if var4.get()==1:
        textFrenki.config(state=NORMAL)
        textFrenki.delete(0,END)
        textFrenki.focus()

    else:
        textFrenki.config(state=DISABLED)
        e_frenki.set('0')

def dhosa():
    if var5.get()==1:
        textDhosa.config(state=NORMAL)
        textDhosa.delete(0,END)
        textDhosa.focus()

    else:
        textDhosa.config(state=DISABLED)
        e_dhosa.set('0')

def chines():
    if var6.get()==1:
        textChines.config(state=NORMAL)
        textChines.delete(0,END)
        textChines.focus()

    else:
        textChines.config(state=DISABLED)
        e_chines.set('0')

def chat():
    if var7.get()==1:
        textChat.config(state=NORMAL)
        textChat.delete(0,END)
        textChat.focus()

    else:
        textChat.config(state=DISABLED)
        e_chat.set('0')

def kulche():
    if var8.get()==1:
        textKulche.config(state=NORMAL)
        textKulche.delete(0,END)
        textKulche.focus()

    else:
        textKulche.config(state=DISABLED)
        e_kulche.set('0')
        
def sizzler():
    if var9.get()==1:
        textSizzler.config(state=NORMAL)
        textSizzler.delete(0,END)
        textSizzler.focus()

    else:
        textSizzler.config(state=DISABLED)
        e_sizzler.set('0')

def colddrink():
    if var10.get()==1:
        textColddrink.config(state=NORMAL)
        textColddrink.delete(0,END)
        textColddrink.focus()

    else:
        textPizza.config(state=DISABLED)
        e_pizza.set('0')

def cocktails():
    if var11.get()==1:
        textCocktails.config(state=NORMAL)
        textCocktails.delete(0,END)
        textCocktails.focus()

    else:
        textCocktails.config(state=DISABLED)
        e_cocktails.set('0')

def mojitos():
    if var12.get()==1:
        textMojitos.config(state=NORMAL)
        textMojitos.delete(0,END)
        textMojitos.focus()

    else:
        textMojitos.config(state=DISABLED)
        e_mojitos.set('0')

def shots():
    if var13.get()==1:
        textShots.config(state=NORMAL)
        textShots.delete(0,END)
        textShots.focus()

    else:
        textShots.config(state=DISABLED)
        e_shots.set('0')

def tea():
    if var14.get()==1:
        textTea.config(state=NORMAL)
        textTea.delete(0,END)
        textTea.focus()

    else:
        textTea.config(state=DISABLED)
        e_tea.set('0')

def cofee():
    if var15.get()==1:
        textCofee.config(state=NORMAL)
        textCofee.delete(0,END)
        textCofee.focus()

    else:
        textCofee.config(state=DISABLED)
        e_cofee.set('0')

def softdrink():
    if var16.get()==1:
        textSoftdrink.config(state=NORMAL)
        textSoftdrink.delete(0,END)
        textSoftdrink.focus()

    else:
        textSoftdrink.config(state=DISABLED)
        e_softdrink.set('0')

def mocktails():
    if var17.get()==1:
        textMocktails.config(state=NORMAL)
        textMocktails.delete(0,END)
        textMocktails.focus()

    else:
        textMocktails.config(state=DISABLED)
        e_mocktails.set('0')

def water():
    if var18.get()==1:
        textWater.config(state=NORMAL)
        textWater.delete(0,END)
        textWater.focus()

    else:
        textWater.config(state=DISABLED)
        e_water.set('0')

def cassata():
    if var19.get()==1:
        textCassata.config(state=NORMAL)
        textCassata.delete(0,END)
        textCassata.focus()

    else:
        textCassata.config(state=DISABLED)
        e_cassata.set('0')

def blackforest():
    if var20.get()==1:
        textBlackforest.config(state=NORMAL)
        textBlackforest.delete(0,END)
        textBlackforest.focus()

    else:
        textBlackforest.config(state=DISABLED)
        e_blackforest.set('0')

def chocolate():
    if var21.get()==1:
        textChocolate.config(state=NORMAL)
        textChocolate.delete(0,END)
        textChocolate.focus()

    else:
        textChocolate.config(state=DISABLED)
        e_chocolate.set('0')

def butterscotch():
    if var22.get()==1:
        textButterscotch.config(state=NORMAL)
        textButterscotch.delete(0,END)
        textButterscotch.focus()

    else:
        textButterscotch.config(state=DISABLED)
        e_butterscotch.set('0')

def kesarpista():
    if var23.get()==1:
        textKesarpista.config(state=NORMAL)
        textKesarpista.delete(0,END)
        textKesarpista.focus()

    else:
        textKesarpista.config(state=DISABLED)
        e_kesarpista.set('0')
        
def vanilla():
    if var24.get()==1:
        textVanilla.config(state=NORMAL)
        textVanilla.delete(0,END)
        textVanilla.focus()

    else:
        textVanilla.config(state=DISABLED)
        e_vanilla.set('0')

def oreo():
    if var25.get()==1:
        textOreo.config(state=NORMAL)
        textOreo.delete(0,END)
        textOreo.focus()

    else:
        textOreo.config(state=DISABLED)
        e_oreo.set('0')

def cremecaramel():
    if var26.get()==1:
        textCremecaramel.config(state=NORMAL)
        textCremecaramel.delete(0,END)
        textCremecaramel.focus()

    else:
        textCremecaramel.config(state=DISABLED)
        e_cremecaramel.set('0')

def majestic():
    if var27.get()==1:
        textMajestic.config(state=NORMAL)
        textMajestic.delete(0,END)
        textMajestic.focus()

    else:
        textMajestic.config(state=DISABLED)
        e_majestic.set('0')
        
        
#variable
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()

e_pizza=StringVar()
e_sandwich=StringVar()
e_burger = StringVar()
e_frenki = StringVar()
e_dhosa = StringVar()
e_chines = StringVar()
e_chat = StringVar()
e_kulche = StringVar()
e_sizzler = StringVar()

e_colddrink=StringVar()
e_cocktails = StringVar()
e_mojitos = StringVar()
e_shots = StringVar()
e_tea = StringVar()
e_cofee = StringVar()
e_softdrink = StringVar()
e_mocktails = StringVar()
e_water = StringVar()

e_cassata=StringVar()
e_blackforest = StringVar()
e_chocolate = StringVar()
e_butterscotch = StringVar()
e_kesarpista = StringVar()
e_vanilla = StringVar()
e_oreo = StringVar()
e_cremecaramel = StringVar()
e_majestic = StringVar()

costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()

e_pizza.set('0')
e_sandwich.set('0')
e_burger.set('0')
e_frenki.set('0')
e_dhosa.set('0')
e_chines.set('0')
e_chat.set('0')
e_kulche.set('0')
e_sizzler.set('0')

e_colddrink.set('0')
e_cocktails.set('0')
e_mojitos.set('0')
e_shots.set('0')
e_tea.set('0')
e_cofee.set('0')
e_softdrink.set('0')
e_mocktails.set('0')
e_water.set('0')

e_cassata.set('0')
e_blackforest.set('0')
e_chocolate.set('0')
e_butterscotch.set('0')
e_kesarpista.set('0')
e_vanilla.set('0')
e_oreo.set('0')
e_cremecaramel.set('0')
e_majestic.set('0')




#fream
menuFrame=Frame(top,bd=10,relief=RIDGE)
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='lightblue',pady=10)
costFrame.pack(side=BOTTOM)

rightFrame=Frame(bd=15,relief=RIDGE,bg='lightblue')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='lightblue')
calculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='lightblue')
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='lightblue')
buttonFrame.pack()

#food
foodFrame=LabelFrame(menuFrame,text='Food',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='darkblue')
foodFrame.pack(side=LEFT)

Pizza=Checkbutton(foodFrame,text='Pizza',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1,command=pizza)
Pizza.grid(row=0,column=0,sticky=W)

textPizza=Entry(foodFrame,font=('arial',18,'bold'),bd=6,width=5,state=DISABLED,textvariable=e_pizza)
textPizza.grid(row=0,column=1)

Sandwich=Checkbutton(foodFrame,text='Sandwich',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2,command=sandwich)
Sandwich.grid(row=1,column=0,sticky=W)

textSandwich=Entry(foodFrame,font=('arial',18,'bold'),bd=6,width=5,state=DISABLED,textvariable=e_sandwich)
textSandwich.grid(row=1,column=1)

Burger=Checkbutton(foodFrame,text='Burger',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3,command=burger)
Burger.grid(row=2,column=0,sticky=W)

textBurger=Entry(foodFrame,font=('arial',18,'bold'),bd=6,width=5,state=DISABLED,textvariable=e_burger)
textBurger.grid(row=2,column=1)

Frenki=Checkbutton(foodFrame,text='Frenki',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4,command=frenki)
Frenki.grid(row=3,column=0,sticky=W)

textFrenki=Entry(foodFrame,font=('arial',18,'bold'),bd=6,width=5,state=DISABLED,textvariable=e_frenki)
textFrenki.grid(row=3,column=1)

Dhosa=Checkbutton(foodFrame,text='Dhosa',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5,command=dhosa)
Dhosa.grid(row=4,column=0,sticky=W)

textDhosa=Entry(foodFrame,font=('arial',18,'bold'),bd=6,width=5,state=DISABLED,textvariable=e_dhosa)
textDhosa.grid(row=4,column=1)

Chines=Checkbutton(foodFrame,text='Chines',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6,command=chines)
Chines.grid(row=5,column=0,sticky=W)

textChines=Entry(foodFrame,font=('arial',18,'bold'),bd=6,width=5,state=DISABLED,textvariable=e_chines)
textChines.grid(row=5,column=1)

Chat=Checkbutton(foodFrame,text='Chat',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,command=chat)
Chat.grid(row=6,column=0,sticky=W)

textChat=Entry(foodFrame,font=('arial',18,'bold'),bd=6,width=5,state=DISABLED,textvariable=e_chat)
textChat.grid(row=6,column=1)

Kulche=Checkbutton(foodFrame,text='Kulche',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8,command=kulche)
Kulche.grid(row=7,column=0,sticky=W)

textKulche=Entry(foodFrame,font=('arial',18,'bold'),bd=6,width=5,state=DISABLED,textvariable=e_kulche)
textKulche.grid(row=7,column=1)

Sizzler=Checkbutton(foodFrame,text='Sizzler',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9,command=sizzler)
Sizzler.grid(row=8,column=0,sticky=W)

textSizzler=Entry(foodFrame,font=('arial',18,'bold'),bd=6,width=5,state=DISABLED,textvariable=e_sizzler)
textSizzler.grid(row=8,column=1)

#drink
drinksFrame=LabelFrame(menuFrame,text='Drinks',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='darkblue')
drinksFrame.pack(side=LEFT)

Colddrink=Checkbutton(drinksFrame,text='ColdDrink',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10,command=colddrink)
Colddrink.grid(row=0,column=0,sticky=W)

textColddrink = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=6, width=5, state=DISABLED,textvariable=e_colddrink)
textColddrink.grid(row=0, column=1)

Cocktails=Checkbutton(drinksFrame,text='CockTails',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11,command=cocktails)
Cocktails.grid(row=1,column=0,sticky=W)

textCocktails = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=6, width=5, state=DISABLED,textvariable=e_cocktails)
textCocktails.grid(row=1, column=1)

Mojitos=Checkbutton(drinksFrame,text='Mojitos',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12,command=mojitos)
Mojitos.grid(row=2,column=0,sticky=W)

textMojitos = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=6, width=5, state=DISABLED,textvariable=e_mojitos)
textMojitos.grid(row=2, column=1)

Shots=Checkbutton(drinksFrame,text='Shots',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13,command=shots)
Shots.grid(row=3,column=0,sticky=W)

textShots = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=6, width=5, state=DISABLED,textvariable=e_shots)
textShots.grid(row=3, column=1)

Tea=Checkbutton(drinksFrame,text='Tea',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14,command=tea)
Tea.grid(row=4,column=0,sticky=W)

textTea = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=6, width=5, state=DISABLED,textvariable=e_tea)
textTea.grid(row=4, column=1)

Cofee=Checkbutton(drinksFrame,text='Cofee',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15,command=cofee)
Cofee.grid(row=5,column=0,sticky=W)

textCofee = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=6, width=5, state=DISABLED,textvariable=e_cofee)
textCofee.grid(row=5, column=1)

Softdrink=Checkbutton(drinksFrame,text='SoftDrink',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16,command=softdrink)
Softdrink.grid(row=6,column=0,sticky=W)

textSoftdrink = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=6, width=5, state=DISABLED,textvariable=e_softdrink)
textSoftdrink.grid(row=6, column=1)

Mocktails=Checkbutton(drinksFrame,text='MockTails',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17,command=mocktails)
Mocktails.grid(row=7,column=0,sticky=W)

textMocktails = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=6, width=5, state=DISABLED,textvariable=e_mocktails)
textMocktails.grid(row=7, column=1)

Water=Checkbutton(drinksFrame,text='Water',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18,command=water)
Water.grid(row=8,column=0,sticky=W)

textWater = Entry(drinksFrame, font=('arial', 18, 'bold'), bd=6, width=5, state=DISABLED,textvariable=e_water)
textWater.grid(row=8, column=1)

#cake
cakeFrame=LabelFrame(menuFrame,text='Cake',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='darkblue')
cakeFrame.pack(side=LEFT)

Cassata=Checkbutton(cakeFrame,text='Cassata',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19,command=cassata)
Cassata.grid(row=0,column=0,sticky=W)

textCassata = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=6, width=5, state=DISABLED,textvariable=e_cassata)
textCassata.grid(row=0, column=1)

Blackforest=Checkbutton(cakeFrame,text='BlackForest',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20,command=blackforest)
Blackforest.grid(row=1,column=0,sticky=W)

textBlackforest = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=6, width=5, state=DISABLED,textvariable=e_blackforest)
textBlackforest.grid(row=1, column=1)

Chocolate=Checkbutton(cakeFrame,text='Chocolate',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21,command=chocolate)
Chocolate.grid(row=2,column=0,sticky=W)

textChocolate = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=6, width=5, state=DISABLED,textvariable=e_chocolate)
textChocolate.grid(row=2, column=1)

Butterscotch=Checkbutton(cakeFrame,text='ButterScotch',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22,command=butterscotch)
Butterscotch.grid(row=3,column=0,sticky=W)

textButterscotch = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=6, width=5, state=DISABLED,textvariable=e_butterscotch)
textButterscotch.grid(row=3, column=1)

Kesarpista=Checkbutton(cakeFrame,text='KesarPista',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23,command=kesarpista)
Kesarpista.grid(row=4,column=0,sticky=W)

textKesarpista = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=6, width=5, state=DISABLED,textvariable=e_kesarpista)
textKesarpista.grid(row=4, column=1)

Vanilla=Checkbutton(cakeFrame,text='Vanilla',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24,command=vanilla)
Vanilla.grid(row=5,column=0,sticky=W)

textVanilla = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=6, width=5, state=DISABLED,textvariable=e_vanilla)
textVanilla.grid(row=5, column=1)

Oreo=Checkbutton(cakeFrame,text='Oreo',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25,command=oreo)
Oreo.grid(row=6,column=0,sticky=W)

textOreo = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=6, width=5, state=DISABLED,textvariable=e_oreo)
textOreo.grid(row=6, column=1)

Cremecaramel=Checkbutton(cakeFrame,text='CremeCaramel',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26,command=cremecaramel)
Cremecaramel.grid(row=7,column=0,sticky=W)

textCremecaramel = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=6, width=5, state=DISABLED,textvariable=e_cremecaramel)
textCremecaramel.grid(row=7, column=1)

Majestic=Checkbutton(cakeFrame,text='Majestic',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27,command=majestic)
Majestic.grid(row=8,column=0,sticky=W)

textMajestic = Entry(cakeFrame, font=('arial', 18, 'bold'), bd=6, width=5, state=DISABLED,textvariable=e_majestic)
textMajestic.grid(row=8, column=1)

#cost
labelCostofFood=Label(costFrame,text='Cost of Food',font=('arial',16,'bold'),bg='lightblue',fg='dark slate gray')
labelCostofFood.grid(row=0,column=0,sticky=W)

textCostofFood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textCostofFood.grid(row=0,column=1,padx=41,sticky=W)

labelCostofDrinks=Label(costFrame,text='Cost of Drinks',font=('arial',16,'bold'),bg='lightblue',fg='dark slate gray')
labelCostofDrinks.grid(row=1,column=0,sticky=W)

textCostofDrinks=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1,column=1,padx=41,sticky=W)

labelCostofCakes=Label(costFrame,text='Cost of Cakes',font=('arial',16,'bold'),bg='lightblue',fg='dark slate gray')
labelCostofCakes.grid(row=2,column=0,sticky=W)

textCostofCakes=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofcakesvar)
textCostofCakes.grid(row=2,column=1,padx=41,sticky=W)

buttonTotal=Button(costFrame,text='Insert',font=('arial',14,'bold'),width=14,fg='mistyrose',bg='deepskyblue4',bd=3,padx=5,command=insert)
buttonTotal.grid(row=3,column=1)

labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),bg='lightblue',fg='dark slate gray')
labelSubTotal.grid(row=0,column=2,sticky=W)

textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41,sticky=W)

labelServiceTax=Label(costFrame,text='Service Tax',font=('arial',16,'bold'),bg='lightblue',fg='dark slate gray')
labelServiceTax.grid(row=1,column=2,sticky=W)

textServiceTax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3,padx=41,sticky=W)

labelTotalCost=Label(costFrame,text='Total Cost',font=('arial',16,'bold'),bg='lightblue',fg='dark slate gray')
labelTotalCost.grid(row=2,column=2,sticky=W)

textTotalCost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3,padx=41,sticky=W)

buttonTotal=Button(costFrame,text='Print',font=('arial',14,'bold'),width=14,fg='mistyrose',bg='deepskyblue4',bd=3,padx=5)
buttonTotal.grid(row=3,column=3)

#calculator
def press(num):
    global g1

    g1=g1+str(num)

    text1.set(g1)

def ans():
     try:
        global g1

        total = str(eval(g1))
 
        text1.set(total)
        g1 = ""
        
     except:
        text1.set(" Error ")
        g1 = ""

def clear():
    global g1
    g1 = ""
    text1.set("")

text1 = StringVar()
calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4,textvariable=text1)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='darkblue',bg='lightblue',bd=6,width=6,command=lambda: press(7))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='darkblue',bg='lightblue',bd=6,width=6,command=lambda: press(8))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='darkblue',bg='lightblue',bd=6,width=6,command=lambda: press(9))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='darkblue',bg='lightblue',bd=6,width=6,command=lambda: press("+"))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='darkblue',bg='lightblue',bd=6,width=6,command=lambda: press(4))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='mistyrose',bg='deepskyblue4',bd=6,width=6,command=lambda: press(5))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='mistyrose',bg='deepskyblue4',bd=6,width=6,command=lambda: press(6))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='darkblue',bg='lightblue',bd=6,width=6,command=lambda: press("-"))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='darkblue',bg='lightblue',bd=6,width=6,command=lambda: press(1))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='mistyrose',bg='deepskyblue4',bd=6,width=6,command=lambda: press(2))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='mistyrose',bg='deepskyblue4',bd=6,width=6,command=lambda: press(3))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='darkblue',bg='lightblue',bd=6,width=6,command=lambda: press("*"))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='darkblue',bg='lightblue',bd=6,width=6,command=ans)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='darkblue',bg='lightblue',bd=6,width=6,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='darkblue',bg='lightblue',bd=6,width=6,command=lambda: press(0))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='darkblue',bg='lightblue',bd=6,width=6,command=lambda: press("/"))
buttonDiv.grid(row=4,column=3)

#resipt
textReceipt=Text(recieptFrame,font=('arial',13,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

#button
buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),width=6,fg='mistyrose',bg='deepskyblue4',bd=4,padx=5,command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),width=7,fg='mistyrose',bg='deepskyblue4',bd=4,padx=5,command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),width=6,fg='mistyrose',bg='deepskyblue4',bd=4,padx=5)
buttonSave.grid(row=0,column=2)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),width=6,fg='mistyrose',bg='deepskyblue4',bd=4,padx=5,command=reset)
buttonReset.grid(row=0,column=4)



top.mainloop()
