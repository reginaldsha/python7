from tkinter import*
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


root=Tk()
root.title("Pharm Inventory Management system")
root.geometry("1500x1500")
root.config(bg="light blue")


def add():
    a = prod_entry.get()
    b = prodname_entry.get()
    c = prodqty_entry.get()
    d = unitprice_entry.get()

    if a == "" or b == "" or c == "" or d == "":
        MessageBox.showinfo("insert status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="shop")
        cursor = con.cursor()
        cursor.execute(
            "insert into shop.stocklevel (prod_id,prod_name,quantity,unit_price)values('" + a + "','" + b + "','" + c + "','" + d + "')")
        con.commit()

        prod_entry.delete(0, END)
        prodname_entry.delete(0, END)
        prodqty_entry.delete(0, END)
        unitprice_entry.delete(0, END)

        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()


def sale():
    e = prod_entry1.get()
    f = prodname_entry2.get()
    g = prodqty_entry3.get()

    if e == "" or f == "" or g == "" :
        MessageBox.showinfo("insert status", "All fields are required")
    else:

        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="shop")
        cursor = con.cursor()
        cursor.execute(
            "UPDATE shop.stocklevel  SET quantity = (quantity-'"+g+"') WHERE prod_id = '" + e + "'")
        con.commit()

        prod_entry1.delete(0, END)
        prodname_entry2.delete(0, END)
        prodqty_entry3.delete(0, END)


        MessageBox.showinfo("Sales Status", "Sales Successful")
        con.close()


def sin():

    if levelentry.get() == "":
        MessageBox.showinfo("Search Status", "ID is compulsory for Search")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="shop")
        cursor = con.cursor()
        cursor.execute("SELECT prod_name,quantity FROM  shop.stocklevel WHERE prod_id ='" + levelentry.get() + "'" )
        rows = cursor.fetchall()
        single.delete(0, single.size())
        for row in rows:
            insert_data = str(row[0]) + "                                              " + str(row[1])
            single.insert(single.size() + 1, insert_data)

        con.close()


def crit():
    con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="shop")
    cursor = con.cursor()
    cursor.execute("SELECT prod_name,quantity FROM  shop.stocklevel WHERE quantity < 50 ")
    rows = cursor.fetchall()
    crtbox.delete(0, crtbox.size())
    for row in rows:
        insert_data = str(row[0]) + "                      " + "                                         "+str(row[1])
        crtbox.insert(crtbox.size() + 1, insert_data)
    con.close()



def clear():
    crtbox.delete(0,END)


label_1=LabelFrame(root,text="Add new drug to database",width=500,height=700,font=('ariel 15 bold'),fg="blue")
label_1.place(x=0,y=0)
prod_label=Label(label_1,text="product id",font=('ariel 15 bold'),fg="black")
prod_label.place(x=20,y=20,width=150,height=20)
prod_entry=Entry(label_1,borderwidth=2)
prod_entry.place(x=200,y=20,width=150,height=20)


prodname_label=Label(label_1,text="product name",font=('ariel 15 bold'),fg="black")
prodname_label.place(x=20,y=50,width=150,height=20)
prodname_entry=Entry(label_1,borderwidth=2)
prodname_entry.place(x=200,y=50,width=150,height=20)

prodqty_label=Label(label_1,text="quantity",font=('ariel 15 bold'),fg="black")
prodqty_label.place(x=20,y=80,width=150,height=20)
prodqty_entry=Entry(label_1,borderwidth=2)
prodqty_entry.place(x=200,y=80,width=150,height=20)

unitprice_label=Label(label_1,text="     unit price       £",font=('ariel 15 bold'),fg="black")
unitprice_label.place(x=20,y=110,width=170,height=20)
unitprice_entry=Entry(label_1,borderwidth=2)
unitprice_entry.place(x=200,y=110,width=150,height=20)

add_button=Button(label_1,text="Add",font=('ariel 15 bold'),fg="purple",borderwidth=5,bg="yellow",command=add)
add_button.place(x=40,y=140,width=130,height=40)


label_2=LabelFrame(root,text="Issues to customer",width=500,height=700,font=('ariel 15 bold'),fg="orange")
label_2.place(x=500,y=0)


prod_label1=Label(label_2,text="product id",font=('ariel 15 bold'),fg="black")
prod_label1.place(x=20,y=20,width=150,height=20)
prod_entry1=Entry(label_2,borderwidth=2)
prod_entry1.place(x=200,y=20,width=150,height=20)


prodname_label2=Label(label_2,text="product name",font=('ariel 15 bold'),fg="black")
prodname_label2.place(x=20,y=50,width=150,height=20)
prodname_entry2=Entry(label_2,borderwidth=2)
prodname_entry2.place(x=200,y=50,width=150,height=20)

prodqty_label3=Label(label_2,text="Sale quantity",font=('ariel 15 bold'),fg="black")
prodqty_label3.place(x=20,y=80,width=150,height=20)
prodqty_entry3=Entry(label_2,borderwidth=2)
prodqty_entry3.place(x=200,y=80,width=150,height=20)

unitprice_label4=Label(label_2,text="     unit price       £",font=('ariel 15 bold'),fg="black")
unitprice_label4.place(x=20,y=110,width=170,height=20)
unitprice_entry4=Entry(label_2,borderwidth=2)
unitprice_entry4.place(x=200,y=110,width=150,height=20)

add_button5=Button(label_2,text="Sale",font=('ariel 15 bold'),fg="yellow",borderwidth=5,bg="blue",command=sale)
add_button5.place(x=40,y=140,width=130,height=40)



single = Listbox(root)
single.place(x=1001,y=120,width=300,height=60)
stocklabel=Label(root,text="Product StockLevel Check",font=('ariel 14 bold'),fg="purple",bg="yellow")
stocklabel.place(x=1001,y=1,width=300,height=20)
search_label=Label(root,text="ID Search",font=('ariel 12 bold'),fg="blue",bg="yellow")
search_label.place(x=1001,y=30,width=80,height=20)
levelentry=Entry(root)
levelentry.place(x=1090,y=30,width=80,height=20)

clickbutton=Button(root,text="Click Here",fg="blue",bg="yellow",font=('ariel 8 bold'),command=sin)
clickbutton.place(x=1090,y=60,width=80,height=20)

probutton=Button(root,text="Product",fg="blue",bg="yellow",font=('ariel 8 bold'),command=sin,state="disabled")
probutton.place(x=1001,y=100,width=150,height=20)

stbutton=Button(root,text="Stock level",fg="blue",bg="yellow",font=('ariel 8 bold'),command=sin,state="disabled")
stbutton.place(x=1151,y=100,width=150,height=20)

# Stock level check below 50
critical=Label(root,text="Critical StockLevel below 50",font=('ariel 14 bold'),fg="red",bg="yellow")
critical.place(x=1001,y=200,width=300,height=20)

crbutton=Button(root,text="Search",fg="blue",bg="yellow",font=('ariel 8 bold'),command=crit)
crbutton.place(x=1303,y=200,width=100,height=20)

clr=Button(root,text="clear",fg="blue",bg="yellow",font=('ariel 8 bold'),command=clear)
clr.place(x=1303,y=221,width=100,height=30)


tton=Button(root,text="Product",fg="blue",bg="yellow",font=('ariel 8 bold'),command=sin,state="disabled")
tton.place(x=1001,y=222,width=150,height=20)

ton=Button(root,text="Stock level",fg="blue",bg="yellow",font=('ariel 8 bold'),command=sin,state="disabled")
ton.place(x=1151,y=222,width=150,height=20)


crtbox = Listbox(root)
crtbox.place(x=1001,y=240,width=300,height=200)





root.mainloop()