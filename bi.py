from tkinter import*
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


root = Tk()
root.title("Great House Revival Church Membership Data Collection")

root.geometry("1800x1800")

def add():
    a = entry_0.get()
    b = entry_1.get()
    c = entry_2.get()
    d = entry_3.get()
    e = entry_4.get()
    f = entry_5.get()
    g = entry_6.get()
    h = entry_7.get()
    if a == "" or b == "" or c == "" or d == "" or e == "" or f == "" or g == "" or h == "":
        MessageBox.showinfo("insert status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="KESSQL31", database="church")
        cursor = con.cursor()
        cursor.execute(
            "insert into church.membership (id,firstname,lastname,date_of_birth,address,postcode,telephone,email)values('" + a + "','" + b + "','" + c + "','" + d + "','" + e + "','" + f +"','" + g +"','" + h +"')")
        con.commit()

        entry_0.delete(0, END)
        entry_1.delete(0, END)
        entry_2.delete(0, END)
        entry_3.delete(0, END)
        entry_4.delete(0, END)
        entry_5.delete(0, END)
        entry_6.delete(0, END)
        entry_7.delete(0, END)

        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()

def delete():
    if(entry_0.get() == ""):
        MessageBox.showinfo("Delete Status", "ID is compulsory for Delete")
    else:
        con = mysql.connect(host="localhost", user="root", password="KESSQL31", database="church")
        cursor = con.cursor()
        cursor.execute("DELETE FROM  church.membership WHERE ID ='" + entry_0.get() + "'" )
        con.commit()

        entry_0.delete(0, END)
        entry_1.delete(0, END)
        entry_2.delete(0, END)
        entry_3.delete(0, END)
        entry_4.delete(0, END)
        entry_5.delete(0, END)
        entry_6.delete(0, END)
        entry_7.delete(0, END)

        MessageBox.showinfo("Delete Status", "Deleted Successfully")
        con.close()

def update():
    a = entry_0.get()
    b = entry_1.get()
    c = entry_2.get()
    d = entry_3.get()
    e = entry_4.get()
    f = entry_5.get()
    g = entry_6.get()
    h = entry_7.get()
    if a == "" or b == "" or c == "" or d == "" or e == "" or f == "" or g == "" or h == "":
        MessageBox.showinfo("Update status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="KESSQL31", database="church")
        cursor = con.cursor()
        cursor.execute(
            "UPDATE church.membership  SET firstname = '" + b + "', lastname ='" + c + "', date_of_birth = '" + d + "',address = '" + e + "', postcode = '" + f + "', telephone = '" + g + "', email = '" + h + "' WHERE id = '" + a + "'")
        con.commit()

        entry_0.delete(0, END)
        entry_1.delete(0, END)
        entry_2.delete(0, END)
        entry_3.delete(0, END)
        entry_4.delete(0, END)
        entry_5.delete(0, END)
        entry_6.delete(0, END)
        entry_7.delete(0, END)

        MessageBox.showinfo("Update Status", "Updated Successfully")
        con.close()

def search():
    if(entry_0.get() == ""):
        MessageBox.showinfo("Search Status", "ID is compulsory for Search")
    else:
        con = mysql.connect(host="localhost", user="root", password="KESSQL31", database="church")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM  church.membership WHERE ID ='" + entry_0.get() + "'" )
        rows=cursor.fetchall()
        for row in rows:
            entry_1.insert(0,row[1])
            entry_2.insert(0, row[2])
            entry_3.insert(0, row[3])
            entry_4.insert(0, row[4])
            entry_5.insert(0, row[5])
            entry_6.insert(0, row[6])
            entry_7.insert(0, row[7])
        con.close()

def clear():
    entry_0.delete(0, END)
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)
    entry_4.delete(0, END)
    entry_5.delete(0, END)
    entry_6.delete(0, END)
    entry_7.delete(0, END)
    list_1.delete(0,END)


def show():
    con = mysql.connect(host="localhost", user="root", password="KESSQL31", database="church")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM  church.membership ")
    rows = cursor.fetchall()
    list_1.delete(0,list_1.size())
    for row in rows:
        insertData = str(row[0])+"    "+row[1]+"    "+row[2]+"    "+row[3]+"    "+row[4]+"    "+row[5]+"    "+row[6]+"    "+row[7]
        list_1.insert(list_1.size()+1,insertData)

    con.close()
label_0=Label(root,text="ID",font="bold",fg="blue")
label_0.place(x=0,y=40,width=150,height=20)
entry_0=Entry(root)
entry_0.place(x=200,y=40,width=200,height=20)

label_1=Label(root,text="First Name",font="bold",fg="blue")
label_1.place(x=0,y=70,width=150,height=20)
entry_1=Entry(root)
entry_1.place(x=200,y=70,width=200,height=20)

label_2=Label(root,text="Last Name",font="bold",fg="blue")
label_2.place(x=0,y=100,width=150,height=20)
entry_2=Entry(root)
entry_2.place(x=200,y=100,width=200,height=20)

label_3=Label(root,text="Date of Birth",font="bold",fg="blue")
label_3.place(x=0,y=130,width=150,height=20)
entry_3=Entry(root)
entry_3.place(x=200,y=130,width=200,height=20)

label_4=Label(root,text="Address",font="bold",fg="blue")
label_4.place(x=0,y=160,width=150,height=20)
entry_4=Entry(root)
entry_4.place(x=200,y=160,width=450,height=20)

label_5=Label(root,text="Postcode",font="bold",fg="blue")
label_5.place(x=0,y=190,width=150,height=20)
entry_5=Entry(root)
entry_5.place(x=200,y=190,width=200,height=20)

label_6=Label(root,text="Telephone",font="bold",fg="blue")
label_6.place(x=0,y=220,width=150,height=20)
entry_6=Entry(root)
entry_6.place(x=200,y=220,width=200,height=20)

label_7=Label(root,text="Email",font="bold",fg="blue")
label_7.place(x=0,y=250,width=150,height=20)
entry_7=Entry(root)
entry_7.place(x=200,y=250,width=200,height=20)

list_1=Listbox(root)
list_1.place(x=0,y=280,width=900,height=400)

sb_1=Scrollbar(root)
sb_1.place(x=880,y=280,height=200,width=20)

list_1.configure(yscrollcommand=sb_1.set)
sb_1.configure(command=list_1.yview)

view_all=Button(root,text="View all",font="bold",fg="black",bg="light yellow",command=show)
view_all.place(x=970,y=280,height=60,width=130)

search=Button(root,text="Search Entry",font="bold",fg="black",bg="light yellow",command=search)
search.place(x=970,y=345,height=60,width=130)

add_entry=Button(root,text="Add Entry",font="bold",fg="black",bg="light yellow",command=add)
add_entry.place(x=970,y=410,height=60,width=130)


update=Button(root,text="Update",font="bold",fg="black",bg="light yellow",command=update)
update.place(x=970,y=475,height=60,width=130)


delete=Button(root,text="Delete",font="bold",fg="black",bg="light yellow",command=delete)
delete.place(x=970,y=540,height=60,width=130)

close=Button(root,text="Close",font="bold",fg="black",bg="light yellow",command=root.quit)
close.place(x=970,y=605,height=60,width=130)

clear=Button(root,text="Clear Entries",font="bold",fg="black",bg="light yellow",command=clear)
clear.place(x=970,y=670,height=60,width=130)


show()
root.mainloop()