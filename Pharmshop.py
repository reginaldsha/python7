from tkinter import*

def yep(number):
    d.insert(END,number)








root = Tk()
root.geometry("500x500")
vertical = Scale(root,from_=0,to=500)
vertical.pack()
b = Button(root,text="adjust",command=lambda:yep(vertical.get()))
b.pack()
label=Label(root,text="")
label.pack()
d=Text(root,width=100,height=50)
d.pack()
root.mainloop()


