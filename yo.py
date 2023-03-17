from tkinter import*
root=Tk()
root.title("STUDENT RECORDS")
root.geometry("500x500")
def show():

    a=name_entry.get()
    b=age_entry.get()
    c=address_entry.get()
    d=phonenumb_entry.get()
    e=marriagestatus_entry.get()
    f=sex_entry.get()
    results=a+"\n"+b+"\n"+c+"\n"+d+"\n"+e+"\n"+f
    tex.delete(0.0,END)

    tex.insert(END,results)

    name_entry.delete(0, END)
    age_entry.delete(0, END)
    address_entry.delete(0, END)
    phonenumb_entry.delete(0, END)
    marriagestatus_entry.delete(0, END)
    sex_entry.delete(0, END)






student_label=Label(root,text="STUDENT DETAILS",fg="black",font="bold")
student_label.grid(row=1,column=0,columnspan=6)

name_label=Label(root,text="Name",fg="black",font="bold")
name_entry=Entry(root)
name_label.grid(row=3,column=0,columnspan=3)
name_entry.grid(row=3,column=3,columnspan=10)

age_label=Label(root,text="Age",fg="black",font="bold")
age_entry=Entry(root)
age_label.grid(row=4,column=0,columnspan=3)
age_entry.grid(row=4,column=3,columnspan=10)

address_label=Label(root,text="Address",fg="black",font="bold")
address_entry=Entry(root)
address_label.grid(row=5,column=0,columnspan=3)
address_entry.grid(row=5,column=3,columnspan=10)

phonenumb_label=Label(root,text="Contact number",fg="black",font="bold")
phonenumb_entry=Entry(root)
phonenumb_label.grid(row=6,column=0,columnspan=3)
phonenumb_entry.grid(row=6,column=3,columnspan=10)


marriagestatus_label=Label(root,text="Marriage status",fg="black",font="bold")
marriagestatus_entry=Entry(root)
marriagestatus_label.grid(row=7,column=0,columnspan=3)
marriagestatus_entry.grid(row=7,column=3,columnspan=10)

sex_label=Label(root,text="Sex",fg="black",font="bold")
sex_entry=Entry(root,text="Sex",fg="black",font="bold")
sex_label.grid(row=8,column=0,columnspan=3)
sex_entry.grid(row=8,column=3,columnspan=7)
print_but=Button(root,text="print",command=show)
print_but.grid(row=9,column=0)
tex=Text(root)
tex.grid(row=10,column=0,rowspan=6,columnspan=4)




root.mainloop()


