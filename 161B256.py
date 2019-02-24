from Tkinter import*
from tkMessageBox import *
import random
import sqlite3
import splash



splash.splashscreen()
root=Tk()
root.title("Raghu Rasoi")
root.configure(background="aquamarine3")
Label(root, text=" []>  Raghu Rasoi : The Indian Cuisine <[]", font="times 40", relief="ridge", fg="ivory3", width=40, bg="blue4").grid(row=0, column=0, columnspan=6)
Label(root,text='Enter Name: ',font="times 20", width=40, bg="aquamarine3").grid(row=1,column=1)
en=Entry(root,width=30)
en.grid(row=1, column=2)
Label(root,text='Enter phone no.: ',font="times 20", width=40, bg="aquamarine3").grid(row=2,column=1)
ep=Entry(root,width=30)
ep.grid(row=2, column=2)
Label(root,text='Enter Bill no.: ',font="times 20", width=40, bg="aquamarine3").grid(row=3,column=1)
bno=random.randint(1266,5599)
Label(root,text=bno,font="times 20").grid(row=3,column=2)
Label(root,text='Select your food : ',font="times 20", width=40, bg="aquamarine3").grid(row=4,column=1)
val=0.0





#================================================================Label==================================================================================================================



def veg():
   
    root=Tk()
    root.configure(background="aquamarine3")
    Label(root, text=" []>  Raghu Rasoi : The Indian Cuisine <[]", font="times 30", relief="ridge", fg="ivory3", width=40, bg="blue4").grid(row=0, column=0, columnspan=6)
    Label(root, text="Item", font="times 10 bold", bg="aquamarine3").grid(row=1, column=3)
    Label(root, text="Price per Plate", font="times 10 bold", bg="aquamarine3").grid(row=1, column=4)
    Label(root, text="Quantity", font="times 10 bold", bg="aquamarine3").grid(row=1, column=5)


    Label(root, text="Item", font="times 10 bold", bg="aquamarine3").grid(row=1, column=0)
    Label(root, text="Price per Plate", font="times 10 bold", bg="aquamarine3").grid(row=1, column=1)
    Label(root, text="Quantity", font="times 10 bold", bg="aquamarine3").grid(row=1, column=2)
    

    Label(root, text="BUTTER PANEER", font="times 15", bg="aquamarine3").grid(row=2, column=0)
    Label(root, text="₹ 200", bg="aquamarine3").grid(row=2, column=1)
    e1=Entry(root,width=10)
    e1.grid(row=2,column=2)
    e1.insert(0,'0')

    Label(root,text="STUFFED BABY EGGPLANT", font="times 15", bg="aquamarine3").grid(row=3, column=0)
    Label(root, text="₹ 420", bg="aquamarine3").grid(row=3, column=1)
    e2=Entry(root,width=10)
    e2.grid(row=3, column=2)
    e2.insert(0,'0')
    

    Label(root, text="MUSHROOM KOFTA", font="times 15", bg="aquamarine3").grid(row=4, column=0)
    Label(root, text="₹ 650", bg="aquamarine3").grid(row=4, column=1)
    e3=Entry(root,width=10)
    e3.grid(row=4, column=2)
    e3.insert(0,'0')


    Label(root, text="MASALA MUSHROOM", font="times 15", bg="aquamarine3").grid(row=5, column=0)
    Label(root, text="₹ 540", bg="aquamarine3").grid(row=5, column=1)
    e4=Entry(root,width=10)
    e4.grid(row=5, column=2)
    e4.insert(0,'0')




    Label(root, text="PANEER KABAB", font="times 15", bg="aquamarine3").grid(row=6, column=0)
    Label(root, text="₹ 460", bg="aquamarine3").grid(row=6, column=1)
    e5=Entry(root,width=10)
    e5.grid(row=6, column=2)
    e5.insert(0,'0')


    Label(root, text="PANEER LABABDAAR", font="times 15", bg="aquamarine3").grid(row=2, column=3)
    Label(root, text="₹ 490", bg="aquamarine3").grid(row=2, column=4)
    e6=Entry(root,width=10)
    e6.grid(row=2, column=5)
    e6.insert(0,'0')
   



    Label(root, text="PALAK PANEER", font="times 15", bg="aquamarine3").grid(row=3, column=3)
    Label(root, text="₹ 480", bg="aquamarine3").grid(row=3, column=4)
    e7=Entry(root,width=10)
    e7.grid(row=3, column=5)
    e7.insert(0,'0')
    




    Label(root, text="COST OF MEAL", font="times 15", bg="aquamarine3").grid(row=4, column=3)
    e8=Entry(root,width=10)
    e8.grid(row=4, column=5)
    



    Label(root, text="GST TAX", font="times 15", bg="aquamarine3").grid(row=5, column=3)
    Label(root, text="5%", bg="aquamarine3").grid(row=5, column=4) 

    def calc_total():
        global val
        val = int(e1.get())*200+int(e2.get())*420+int(e3.get())*650+int(e4.get())*540+int(e5.get())*460+int(e6.get())*490+int(e7.get())*480
        val = str(val)
        e8.insert(0,val)
        val=int(val)
        val = val+val*5/100.0
        e10.insert(0,val)

        con=sqlite3.Connection('hrdb')
        cur=con.cursor()
        cur.execute("create table if not exists data(name varchar(20),mob int(12),bill double)")
        db=[(en.get(),ep.get(),val)]
        cur.executemany("insert into data values(?,?,?)",db)
        con.commit()
        cur.execute("Select * from data")
        print cur.fetchall()
 


    Label(root, text="TOTAL COST", font="times 15", bg="aquamarine3").grid(row=6, column=3)
    e10=Entry(root,width=10)
    e10.grid(row=6, column=5)

    
     
    def reset_1():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)

   
    Button(root, text="total", bg="gray",bd=5,command=calc_total).grid(row=7, column=1)
    Button(root, text="reset", bg="gray",command=reset_1,bd=5).grid(row=7, column=2)
    def Leave():
        showinfo('THANKING','Thanks For Visiting')
        root.destroy()
    Button(root, text="Leave", bg="yellow2", fg="red", width=8, command=Leave,bd=5).grid(row=8, column=4)








#=======================================================================================non-veg=============================================================#



    
def non_veg():
    root=Tk()
    root.configure(background="aquamarine3")
    Label(root, text=" []>  Raghu Rasoi : The Indian Cuisine <[]", font="times 30", relief="ridge", fg="ivory3", width=40, bg="blue4").grid(row=0, column=0, columnspan=6)
    Label(root, text="Item", font="times 10 bold", bg="aquamarine3").grid(row=1, column=3)
    Label(root, text="Price per Plate", font="times 10 bold", bg="aquamarine3").grid(row=1, column=4)
    Label(root, text="Quantity", font="times 10 bold", bg="aquamarine3").grid(row=1, column=5)


    Label(root, text="Item", font="times 10 bold", bg="aquamarine3").grid(row=1, column=0)
    Label(root, text="Price per Plate", font="times 10 bold", bg="aquamarine3").grid(row=1, column=1)
    Label(root, text="Quantity", font="times 10 bold", bg="aquamarine3").grid(row=1, column=2)
    

    Label(root, text="Murg Mussallan", font="times 15", bg="aquamarine3").grid(row=2, column=0)
    Label(root, text="₹ 750", bg="aquamarine3").grid(row=2, column=1)
    e1=Entry(root,width=10)
    e1.grid(row=2, column=2)
    e1.insert(0,'0')



    Label(root, text="Mutton Galawati Kabab", font="times 15", bg="aquamarine3").grid(row=3, column=0)
    Label(root, text="₹ 430", bg="aquamarine3").grid(row=3, column=1)
    e2=Entry(root,width=10)
    e2.grid(row=3, column=2)
    e2.insert(0,'0')



    Label(root, text="Kolahapuri Chicken", font="times 15", bg="aquamarine3").grid(row=4, column=0)
    Label(root, text="₹ 650", bg="aquamarine3").grid(row=4, column=1)
    e3=Entry(root,width=10)
    e3.grid(row=4, column=2)
    e3.insert(0,'0')




    Label(root, text="Fish Honey", font="times 15", bg="aquamarine3").grid(row=5, column=0)
    Label(root, text="₹ 500", bg="aquamarine3").grid(row=5, column=1)
    e4=Entry(root,width=10)
    e4.grid(row=5, column=2)
    e4.insert(0,'0')



    Label(root, text="Shami Kabab", font="times 15", bg="aquamarine3").grid(row=6, column=0)
    Label(root, text="₹ 460", bg="aquamarine3").grid(row=6, column=1)
    e5=Entry(root,width=10)
    e5.grid(row=6, column=2)
    e5.insert(0,'0')



    Label(root, text="Tandoori Chicken", font="times 15", bg="aquamarine3").grid(row=2, column=3)
    Label(root, text="₹ 600", bg="aquamarine3").grid(row=2, column=4)
    e6=Entry(root,width=10)
    e6.grid(row=2, column=5)
    e6.insert(0,'0')



    Label(root, text="Tundey Kababi", font="times 15", bg="aquamarine3").grid(row=3, column=3)
    Label(root, text="₹ 400", bg="aquamarine3").grid(row=3, column=4)
    e7=Entry(root,width=10)
    e7.grid(row=3, column=5)
    e7.insert(0,'0')




    Label(root, text="COST OF MEAL", font="times 15", bg="aquamarine3").grid(row=4, column=3)
    e8=Entry(root,width=10)
    e8.grid(row=4, column=5)



    Label(root, text="GST TAX", font="times 15", bg="aquamarine3").grid(row=5, column=3)
    Label(root, text="5%", bg="aquamarine3").grid(row=5, column=4)
    


    def calc_total():
        global val
        val = int(e1.get())*750+int(e2.get())*430+int(e3.get())*650+int(e4.get())*500+int(e5.get())*460+int(e6.get())*600+int(e7.get())*400
        val = str(val)
        e8.insert(0,val)
        val=int(val)
        val = val+val*5/100.0
        e10.insert(0,val)

        con=sqlite3.Connection('hrdb')
        cur=con.cursor()
        cur.execute("create table if not exists data(name varchar(20),mob int(12),bill double)")
        db=[(en.get(),ep.get(),val)]
        cur.executemany("insert into data values(?,?,?)",db)
        con.commit()
        cur.execute("Select * from data")
        print cur.fetchall()



    Label(root, text="TOTAL COST", font="times 15", bg="aquamarine3").grid(row=6, column=3)
    e10=Entry(root,width=10)
    e10.grid(row=6, column=5)


    def reset_1():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
    

    Button(root, text="total", bg="gray",bd=5, command=calc_total).grid(row=7, column=1)
    Button(root, text="reset", bg="gray",command=reset_1,bd=5).grid(row=7, column=2)

    def Leave():
       showinfo('THANKING','Thanks For Visiting')
       root.destroy()
    Button(root, text="Leave", bg="yellow2", fg="red", width=8, command=Leave,bd=5).grid(row=8, column=4)
 

    

#================================================================= BREAKFAST=======================================================================================================
def breakfast():
    root=Tk()
    Label(root, text="5%", bg="aquamarine3").grid(row=5, column=4) 
    root.configure(background="aquamarine3")
    Label(root, text=" []>  Raghu Rasoi : The Indian Cuisine <[]", font="times 30", relief="ridge", fg="ivory3", width=40, bg="blue4").grid(row=0, column=0, columnspan=6)
    Label(root, text="Item", font="times 10 bold", bg="aquamarine3").grid(row=1, column=3)
    Label(root, text="Price per Plate", font="times 10 bold", bg="aquamarine3").grid(row=1, column=4)
    Label(root, text="Quantity", font="times 10 bold", bg="aquamarine3").grid(row=1, column=5)


    Label(root, text="Item", font="times 10 bold", bg="aquamarine3").grid(row=1, column=0)
    Label(root, text="Price per Plate", font="times 10 bold", bg="aquamarine3").grid(row=1, column=1)
    Label(root, text="Quantity", font="times 10 bold", bg="aquamarine3").grid(row=1, column=2)
    

    Label(root, text="IDLI", font="times 15", bg="aquamarine3").grid(row=2, column=0)
    Label(root, text="₹ 150", bg="aquamarine3").grid(row=2, column=1)
    e1=Entry(root,width=10)
    e1.grid(row=2, column=2)
    e1.insert(0,'0')



    Label(root, text="KULCHA", font="times 15", bg="aquamarine3").grid(row=3, column=0)
    Label(root, text="₹ 180", bg="aquamarine3").grid(row=3, column=1)
    e2=Entry(root,width=10)
    e2.grid(row=3, column=2)
    e2.insert(0,'0') 



    Label(root, text="OMELETTE", font="times 15", bg="aquamarine3").grid(row=4, column=0)
    Label(root, text="₹ 60", bg="aquamarine3").grid(row=4, column=1)
    e3=Entry(root,width=10)
    e3.grid(row=4, column=2)
    e3.insert(0,'0')




    Label(root, text="UPMA", font="times 15", bg="aquamarine3").grid(row=5, column=0)
    Label(root, text="₹ 190", bg="aquamarine3").grid(row=5, column=1)
    e4=Entry(root,width=10)
    e4.grid(row=5, column=2)
    e4.insert(0,'0')




    Label(root, text="DOSA", font="times 15", bg="aquamarine3").grid(row=6, column=0)
    Label(root, text="₹ 160", bg="aquamarine3").grid(row=6, column=1)
    e5=Entry(root,width=10)
    e5.grid(row=6, column=2)
    e5.insert(0,'0')




    Label(root, text="CHEESE TOAST", font="times 15", bg="aquamarine3").grid(row=2, column=3)
    Label(root, text="₹ 130", bg="aquamarine3").grid(row=2, column=4)
    e6=Entry(root,width=10)
    e6.grid(row=2, column=5)
    e6.insert(0,'0')



    Label(root, text="ALOO PARATHA", font="times 15", bg="aquamarine3").grid(row=3, column=3)
    Label(root, text="₹ 200", bg="aquamarine3").grid(row=3, column=4)
    e7=Entry(root,width=10)
    e7.grid(row=3, column=5)
    e7.insert(0,'0')




    Label(root, text="COST OF MEAL", font="times 15", bg="aquamarine3").grid(row=4, column=3)
    e8=Entry(root,width=10)
    e8.grid(row=4, column=5)



    Label(root, text="GST TAX", font="times 15", bg="aquamarine3").grid(row=5, column=3)
    Label(root, text="5%", bg="aquamarine3").grid(row=5, column=4)
    
    def calc_total():
        global val
        val = int(e1.get())*150+int(e2.get())*180+int(e3.get())*60+int(e4.get())*190+int(e5.get())*160+int(e6.get())*130+int(e7.get())*200
        val = str(val)
        e8.insert(0,val)
        val=int(val)
        val = val+val*5/100.0
        e10.insert(0,val)

        con=sqlite3.Connection('hrdb')
        cur=con.cursor()
        cur.execute("create table if not exists data(name varchar(20),mob int(12),bill double)")
        db=[(en.get(),ep.get(),val)]
        cur.executemany("insert into data values(?,?,?)",db)
        con.commit()
        cur.execute("Select * from data")
        print cur.fetchall()



    Label(root, text="TOTAL COST", font="times 15", bg="aquamarine3").grid(row=6, column=3)
    e10=Entry(root,width=10)
    e10.grid(row=6, column=5)
    
    
    def reset_1():
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
    

    Button(root, text="total", bg="gray",bd=5,command=calc_total).grid(row=7, column=1)
    Button(root, text="reset", bg="gray",command=reset_1,bd=5).grid(row=7, column=2)

    

    def Leave():
        
        
        showinfo('THANKING','Thanks For Visiting')
        root.destroy()
        
    Button(root, text="Leave", bg="yellow2", fg="red", width=8, command=Leave,bd=5).grid(row=8, column=4)


   

#========================================================================BUTTON===============================================================================================





Button(root, text="Non-veg", bg="gold",command=non_veg, width=20,bd=10).grid(row=7, column=0, columnspan=1)
Button(root, text="veg", bg="gold",command=veg, width=20,bd=10).grid(row=7, column=1, columnspan=2)
Button(root, text="Breakfast", bg="gold",command=breakfast, width=20,bd=10).grid(row=7, column=2, columnspan=4)



def Leave():
    
    showinfo('THANKING','Thanks For Visiting')
    root.destroy()
Button(root, text="Leave", bg="yellow2", fg="red", width=8, command=Leave,bd=10).grid(row=8, column=4)




root.mainloop()
