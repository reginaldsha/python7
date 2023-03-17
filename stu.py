from tkinter import*
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

root=Tk()
root.title("test run")
root.geometry("600x600")

def add1():
    a = entry1.get()
    b = entry2.get()
    c = entry3.get()

    if a == "" or b == "" or c == "":
        MessageBox.showinfo("insert status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="school")
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO  school.marks (id,subject,score)values('" + a + "','" + b + "','" + c + "' )")
        con.commit()

        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)

        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()


def add2():
    d = entry4.get()
    e = entry5.get()
    f = entry6.get()
    g = entry7.get()
    if d == "" or e == "" or f == "" or g == "":
        MessageBox.showinfo("insert status", "All fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="school")
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO  school.student (id,name,age,class)values('" + d + "','" + e + "','" + f + "','" + g+"')")
        con.commit()

        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)
        entry7.delete(0, END)

        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()

def show():
    con = mysql.connect(host="localhost", user="root", password="REGSQL45", database="school")
    cursor = con.cursor()
    cursor.execute("SELECT school.student.name,school.marks.subject,school.marks.score FROM school.student JOIN "
                   "school.marks "
                   "ON school.student.id=school.marks.id")

    rows = cursor.fetchall()
    list_1.delete(0,list_1.size())
    for row in rows:
        insertData = str(row[0])+"    "+row[1]+"    "+str(row[2])
        list_1.insert(list_1.size()+1,insertData)

    con.close()




# marks wickget  info
label1=Label(root,text="id",fg="blue",bg="yellow",font="bold")
label1.place(x=100,y=100,height=30,width=80)
entry1=Entry(root)
entry1.place(x=190,y=100,height=30,width=80)

label2=Label(root,text="subject",fg="blue",bg="yellow",font="bold")
label2.place(x=100,y=140,height=30,width=80)
entry2=Entry(root)
entry2.place(x=190,y=140,height=30,width=80)

label3=Label(root,text="score",fg="blue",bg="yellow",font="bold")
label3.place(x=100,y=180,height=30,width=80)
entry3=Entry(root)
entry3.place(x=190,y=180,height=30,width=80)

submit1=Button(root,text="submit",fg="black",bg="yellow",font="bold",command=add1)
submit1.place(x=100,y=220,height=30,width=80)


label4=Label(root,text="id",fg="black",bg="red",font="bold")
label4.place(x=100,y=300,height=30,width=80)
entry4=Entry(root)
entry4.place(x=190,y=300,height=30,width=80)

label5=Label(root,text="name",fg="black",bg="red",font="bold")
label5.place(x=100,y=340,height=30,width=80)
entry5=Entry(root)
entry5.place(x=190,y=340,height=30,width=80)

label6=Label(root,text="age",fg="black",bg="red",font="bold")
label6.place(x=100,y=380,height=30,width=80)
entry6=Entry(root)
entry6.place(x=190,y=380,height=30,width=80)

label7=Label(root,text="class",fg="black",bg="red",font="bold")
label7.place(x=100,y=420,height=30,width=80)
entry7=Entry(root)
entry7.place(x=190,y=420,height=30,width=80)


submit2=Button(root,text="submit",fg="black",bg="yellow",font="bold",command=add2)
submit2.place(x=100,y=460,height=30,width=80)

list_1=Listbox(root)
list_1.place(x=0,y=500,width=900,height=300)

view_all=Button(root,text="View all",font="bold",fg="black",bg="lightyellow",command=show)
view_all.place(x=970,y=500,height=60,width=130)


root.mainloop()



