import tkinter as tk

# create a main window
root = tk.Tk()
root.title("Pharmacy Shop Inventory")

# create labels and entry boxes
label1 = tk.Label(root, text="Item Name")
label1.grid(row=0, column=0)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Item Code")
label2.grid(row=1, column=0)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

label3 = tk.Label(root, text="Quantity")
label3.grid(row=2, column=0)

entry3 = tk.Entry(root)
entry3.grid(row=2, column=1)

label4 = tk.Label(root, text="Price")
label4.grid(row=3, column=0)

entry4 = tk.Entry(root)
entry4.grid(row=3, column=1)

# create a listbox to display inventory
listbox = tk.Listbox(root)
listbox.grid(row=4, column=0, columnspan=2)

# create a function to add items to inventory
def add_item():
    item_name = entry1.get()
    item_code = entry2.get()
    quantity = entry3.get()
    price = entry4.get()
    item = f"{item_name} ({item_code}): {quantity} x ${price}"
    listbox.insert(tk.END, item)
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)

# create a button to add items to inventory
button1 = tk.Button(root, text="Add Item", command=add_item)
button1.grid(row=5, column=0)

# create a function to clear the inventory
def clear_inventory():
    listbox.delete(0, tk.END)

# create a button to clear the inventory
button2 = tk.Button(root, text="Clear Inventory", command=clear_inventory)
button2.grid(row=5, column=1)

# start the main loop
root.mainloop()
