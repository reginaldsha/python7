from tkinter import*
from random import randint
root = Tk()
root.title("Random numbers")
root.geometry("400x400")
def show():
    results = randint(1,100)
    text.delete(0.0,END)
    text.insert(END,results)
display = Button(root,text="random num(1-100)",command=show)
text = Text(root)
display.grid(row=0,column=0)
text.grid(row=1,column=0)
root.mainloop()

