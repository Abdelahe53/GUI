from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=10, border=5)
e.grid(row=1, column=0, columnspan=4, padx=5, pady=5)


def button_click(number):

    e.insert(0, number)

#define buttons
Button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
Button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
Button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
Button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
Button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
Button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
Button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
Button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
Button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
Button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_plus = Button(root, text="+", padx=40, pady=20, command=lambda: button_click())
button_equal = Button(root, text="=", padx=40, pady=20, command=lambda: button_click())
button_clear = Button(root, text="C", padx=40, pady=8, command=lambda: button_click())
button_sub = Button(root, text="-", padx=40, pady=20, command=lambda: button_click())
button_dev = Button(root, text="/", padx=40, pady=20, command=lambda: button_click())
button_x = Button(root, text="x", padx=40, pady=20, command=lambda: button_click())

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
