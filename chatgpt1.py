import tkinter as tk

# create a main window
root = tk.Tk()
root.title("Four Menu Bars")

# create four menu bars
menu1 = tk.Menu(root)
menu2 = tk.Menu(root)
menu3 = tk.Menu(root)
menu4 = tk.Menu(root)

# add menu items to menu1
menu1.add_command(label="File")
menu1.add_command(label="Edit")
menu1.add_command(label="View")

# add menu items to menu2
menu2.add_command(label="Copy")
menu2.add_command(label="Paste")

# add menu items to menu3
menu3.add_command(label="Undo")
menu3.add_command(label="Redo")

# add menu items to menu4
menu4.add_command(label="Help")
menu4.add_command(label="About")

# create a menu bar and add menus to it
menubar = tk.Menu(root)
menubar.add_cascade(label="Menu 0", menu=menu1)
menubar.add_cascade(label="Menu 2", menu=menu2)
menubar.add_cascade(label="Menu 3", menu=menu3)
menubar.add_cascade(label="Menu 4", menu=menu4)

# configure the root window to use the menu bar
root.config(menu=menubar)

# start the main loop
root.mainloop()