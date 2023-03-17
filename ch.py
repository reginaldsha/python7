import tkinter
root = tkinter.Tk()
root.title("DICTIONARY")
root.geometry("400x400")

def show():
    check = entry_1.get()
    final = check.lower()
    if final in dic:
        result = dic[final]
        label_2.config(text=result)
    else:
        label_2.config(text="synonym not defined")

label_1 = tkinter.Label(root,text="Enter Word",fg="black",bg="yellow",font="bold")
label_1.place(x=0,y=20,height=40,width=100)
entry_1=tkinter.Entry(root)
entry_1.place(x=110,y=20,height=40,width=150)
button=tkinter.Button(root,text="Show Synonym",fg="black",bg="yellow",font="bold",command=show)
button.place(x=0,y=80,height=40,width=150)
label_2=tkinter.Label(root)
label_2.place(x=180,y=80,width=150,height=40)

dic = {"compel":"persuade","conclude":"finalise","gloomy":"sad","blunder":"mistake","durex":"force"}




root.mainloop()