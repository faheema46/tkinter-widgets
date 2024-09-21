from tkinter import *

window=Tk()
window.geometry("300x300")
window.title("new window")

def topwin():
    top=Toplevel()
    top.geometry("100x100")
    top.title("subwindow")

    label=Label(top,text="Hello ")
    label.pack()

    top.mainloop()
btn=Button(command=topwin,text="click me")
btn.pack()
window.mainloop()