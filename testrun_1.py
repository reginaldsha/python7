from tkinter import*
import tkinter.messagebox as MessageBox
import mysql.connector as mysql


root=Tk()
root.title("STUDENT RECORDS")
root.geometry("500x500")
def add():
    a=name_entry.get()
    b=gender_entry.get()
    c=contact_entry.get()
    d=salary_entry.get()
    e=years_entry.get()
    if a == "" or b == "" or c == "" or d == "" or e == "":
        MessageBox.showinfo("insert status","All fields are required")
    else:
        con=mysql.connect(host="localhost",user="root",password="REGSQL45",database="companyhr")
        cursor=con.cursor()
        cursor.execute("insert into companyhr.employees (em_name,gender,contact_number,salary,years_in_company)values('"+a+"','"+b+"','"+c+"','"+d+"','"+e+"')")
        con.commit()

    name_entry.delete(0, END)
    gender_entry.delete(0, END)
    contact_entry.delete(0, END)
    salary_entry.delete(0, END)
    years_entry.delete(0, END)

student_label=Label(root,text="STUDENT DETAILS",fg="black",font="bold")
student_label.grid(row=1,column=0,columnspan=6)

name_label=Label(root,text="Name",fg="black",font="bold")
name_entry=Entry(root)
name_label.grid(row=3,column=0,columnspan=3)
name_entry.grid(row=3,column=3,columnspan=10)

gender_label=Label(root,text="gender",fg="black",font="bold")
gender_entry=Entry(root)
gender_label.grid(row=4,column=0,columnspan=3)
gender_entry.grid(row=4,column=3,columnspan=10)

contact_label=Label(root,text="contact number",fg="black",font="bold")
contact_entry=Entry(root)
contact_label.grid(row=5,column=0,columnspan=3)
contact_entry.grid(row=5,column=3,columnspan=10)

salary_label=Label(root,text="salary",fg="black",font="bold")
salary_entry=Entry(root)
salary_label.grid(row=6,column=0,columnspan=3)
salary_entry.grid(row=6,column=3,columnspan=10)
years_label=Label(root,text="years in company",fg="black",font="bold")
years_entry=Entry(root)
years_label.grid(row=7,column=0,columnspan=3)
years_entry.grid(row=7,column=3,columnspan=10)
print_but=Button(root,text="print",command=add)
print_but.grid(row=9,column=0)
root.mainloop()

