from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="green", fg="white", borderwidth=5)
e.pack()
e.insert(0, "Write something: ")
def myClick():
    hello = "This is what you typed: " + e.get()
    mylable = Label(root, text=hello)
    mylable.pack()

mybutton = Button(root, text="Click!", command=myClick)
mybutton.pack()

root.mainloop()