import tkinter
from tkinter import ttk
root = tkinter.Tk()

root.title("Tab Widget")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)


tabControl.add(tab1, text='Members Data collection')
tabControl.add(tab2, text='Visitors Data Collection ')
tabControl.pack(expand=1, fill="both")

ttk.Label(tab1,
          text="Welcome to \
          GeeksForGeeks",font=('ariel 15 bold')).grid(column=0,
                               row=0,
                               padx=30,
                               pady=30)
ttk.Label(tab2,
          text="Lets dive into the\
          world of computers").grid(column=0,
                                    row=0,
                                    padx=30,
                                    pady=30)


ttk.Button(tab1,text="hit me").grid(row=1,column=0)


root.mainloop()

