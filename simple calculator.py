from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=25, borderwidth=5, border=5, )
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#e.insert(0,")
def button_add():
    return

#define buttons
Button_1 = Button(root, text="1", padx=40, pady=20, command=button_add)
Button_2 = Button(root, text="2", padx=40, pady=20, command=button_add)
Button_3 = Button(root, text="3", padx=40, pady=20, command=button_add)
Button_4 = Button(root, text="4", padx=40, pady=20, command=button_add)
Button_5 = Button(root, text="5", padx=40, pady=20, command=button_add)
Button_6 = Button(root, text="6", padx=40, pady=20, command=button_add)
Button_7 = Button(root, text="7", padx=40, pady=20, command=button_add)
Button_8 = Button(root, text="8", padx=40, pady=20, command=button_add)
Button_9 = Button(root, text="9", padx=40, pady=20, command=button_add)
Button_0 = Button(root, text="0", padx=40, pady=20, command=button_add)
button_plus = Button(root, text="+", padx=40, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=40, pady=20, command=button_add)
button_clear = Button(root, text="C", padx=40, pady=8, command=button_add)
button_sub = Button(root, text="-", padx=40, pady=20, command=button_add)
button_dev = Button(root, text="/", padx=40, pady=20, command=button_add)
button_x = Button(root, text="x", padx=40, pady=20, command=button_add)

#put buttons on the screen
Button_1.grid(row=5, column=1)
Button_2.grid(row=5, column=2)
Button_3.grid(row=5, column=3)

Button_4.grid(row=4, column=1)
Button_5.grid(row=4, column=2)
Button_6.grid(row=4, column=3)

Button_7.grid(row=3, column=1)
Button_8.grid(row=3, column=2)
Button_9.grid(row=3, column=3)

Button_0.grid(row=6, column=2)

button_equal.grid(row=6, column=4) #done
button_clear.grid(row=0, column=4) #done
button_plus.grid(row=5, column=4)  #done
button_sub.grid(row=4, column=4)   #done
button_dev.grid(row=3, column=4)   #done
button_x.grid(row=1, column=4)     #done

root.mainloop()