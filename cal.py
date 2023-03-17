from tkinter import*
root=Tk()
root.geometry("300x300")
root.title("calculator")


def clickme(number):

    res=number+200
    entry.insert(0,str(res))

    entry.insert(0,str(current)+str(number))

def plus():
   first_number=entry.get()
   global fnum
   fnum=int(first_number)
   entry.delete(0,END)


def equal():
    secon=entry.get()
    entry.delete(0,END)

    entry.insert(0,fnum+int(secon))




entry=Entry(root,width=50,borderwidth=5,state=None)
entry.grid(row=0,column=0,columnspan=3,padx=50,pady=20)
b9=Button(root,text="9",fg="blue",padx=50,pady=20,command=lambda :clickme(100))
b9.grid(row=1,column=0)

b8=Button(root,text="8",fg="blue",padx=50,pady=20,command=lambda :clickme(8))
b8.grid(row=1,column=1)

b7=Button(root,text="7",fg="blue",padx=50,pady=20,command=lambda :clickme(7))
b7.grid(row=1,column=2)






#b6=Button(root,text="6",fg="blue")
#b5=Button(root,text="5",fg="blue")
#b4=Button(root,text="4",fg="blue")
#b3=Button(root,text="3",fg="blue")
#b2=Button(root,text="2",fg="blue")
#b1=Button(root,text="1",fg="blue")
#b0=Button(root,text="0",fg="blue")
#clear=Button(root,text="9",fg="blue")
add=Button(root,text="+",fg="blue",padx=50,pady=20,command=plus)
add.grid(row=2,column=0)
equal=Button(root,text="=",fg="blue",padx=50,pady=20,command=equal)
equal.grid(row=2,column=1)


root.mainloop()

