from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.title("mywindow")
root.geometry("400x400")

upload=Image.open("img.jpeg")
image=ImageTk.PhotoImage(upload)
label=Label(root,image=image,width=300,height=400)
label.place(x=50,y=0)

label1=Label(text="This is how we add an image",fg="black",bg="white")
label1.place(x=50,y=300)
root.mainloop()