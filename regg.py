from tkinter import*
from tkinter import ttk
root = Tk()
root.title("regi")
root.geometry("1200x1200")
frame=LabelFrame(root,text="hello",width=400,height=400)
frame.place(x=50,y=50)

label=Label(frame,text="enter",fg="red")
label.place(x=10,y=10,height=80,width=80)

root.mainloop()



