from tkinter import*
root = Tk()
root.title("Conversion Table")
root.geometry("400x400")
def convert():
    result = entry.get()
    if result == "":
        label.config(text="value required")
    else:
        con = float(result)
        con1 = (con*0.01)
        con2=round(con1,2)
        results = str(con2)
        label.config(text=results)

entry = Entry(root)
entry.place(x=100,y=50)
label_cm = Label(root,text="cm",fg="blue",font="bold")
label_cm.place(x=200,y=50)
label = Label(root)
label.place(x=100,y=100)
label_m = Label(root,text="metres",fg="blue",font="bold")
label_m.place(x=200,y=100)
button = Button(root,text="Convert",fg="blue",font="bold",command=convert)
button.place(x=100,y=210)

root.mainloop()


