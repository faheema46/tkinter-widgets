from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("new window")
window.geometry("300x300")

def msg():
    messagebox.askyesno("Want to exit?","exit")

    

button=Button(window,text="click me",fg="black",bg="yellow",command=msg)
button.place(x=50,y=35)

window.mainloop()
