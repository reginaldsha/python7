from tkinter import*
from tkinter import ttk

root=Tk()
root.title("hello")
root.geometry("300x300")
ttk.Label(root,text="helo").pack()

ttk.Label(root,text="lo").pack()
r=IntVar()
ttk.Scale(root,from_=0,to=234,orient="vertical",variable=r).pack()

root.mainloop()
