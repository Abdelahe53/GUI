from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="green", fg="white", borderwidth=5)
e.pack()
e.get()

def myClick():
    mylable = Label(root, text=e.get())
    mylable.pack()

mybutton = Button(root, text="enter your name", command=myClick)
mybutton.pack()

root.mainloop()