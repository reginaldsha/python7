
from tkinter import*
window=Tk()
window.title("Membership form")
window.geometry("900x500")
window.configure(background="yellow")
def show_1():
    entry1.delete(0,END)
    entry1.insert(END,"GO HOME")







text1=Label(window,text="name")
button1=Button(window,text="submit",command=show_1)
entry1=Entry(window)
entry1.grid(row=0,column=4,columnspan=100,sticky="EW")
text1.grid(row=0,column=0,columnspan=14,sticky="EW")
button1.grid(row=2,column=0,columnspan=14,sticky="EW")
window.mainloop()
