from tkinter import*
from PIL import ImageTk,Image

root = Tk()
root.geometry("500x500")
root.title("image")

my_img=ImageTk.PhotoImage(Image.open("regipic.jpg"))
mylabel=Label(image=my_img)
mylabel.pack(side="top")






root.mainloop()
