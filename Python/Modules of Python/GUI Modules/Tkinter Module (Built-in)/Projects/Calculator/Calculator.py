"""
Calculator
"""

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def click(event):  # the function to the button
    global scvalue  # to change the variable
    text = event.widget.cget("text")  # to capture the value for showing event to bring the widget
    if text == "=":
        if scvalue.get().isdigit():  # checking for numbers
            value = int(scvalue.get())  # changed to integer
        else:
            try:
                value = eval(screen.get())  # try to show value

            except Exception as e:  # raised exception
                print(e)
                value = "Error"

        scvalue.set(value)  # to stay the same number
        screen.update()

    elif text == "C":  # to clean the entry widget
        scvalue.set("")
        screen.update()

    else:  # entering the value to show
        scvalue.set(scvalue.get() + text)
        screen.update()


def d(*args):  # a function to close the app
    global root
    root.destroy()


root = Tk()
root.geometry("644x700")

root.maxsize(519, 490)

root.title("Calculator")
root.wm_iconbitmap("calculator.ico")  # kept icon

scvalue = StringVar()  # declaring the value of numbers
scvalue.set("")  # setting them to nothing
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")  # made a entry widget for the variable
screen.pack(fill=X, ipadx=8, pady=10, padx=10)  # packed it

f = Frame(root, bg="grey")  # made a frame

b = Button(f, text="9", bg="light blue", padx=28, pady=18, font="lucida 25 bold")  # made a button
b.grid(row=1, column=1)  # packed it
b.bind("<Button-1>", click)  # added a event

b = Button(f, text="8", bg="light blue", padx=28, pady=18, font="lucida 25 bold")
b.grid(row=1, column=2)
b.bind("<Button-1>", click)

b = Button(f, text="7", bg="light blue", padx=28, pady=18, font="lucida 25 bold")
b.grid(row=1, column=3)
b.bind("<Button-1>", click)

b = Button(f, text="+", bg="light green", padx=31, pady=18, font="lucida 25 bold")
b.grid(row=1, column=4)
b.bind("<Button-1>", click)

b = Button(f, text="=", bg="blue", padx=27, pady=18, font="lucida 25 bold")
b.grid(row=1, column=5)
b.bind("<Button-1>", click)

b = Button(f, text="0", bg="light blue", padx=28, pady=18, font="lucida 25 bold")
b.grid(row=5, column=1)
b.bind("<Button-1>", click)

b = Button(f, text="6", bg="light blue", padx=28, pady=18, font="lucida 25 bold")
b.grid(row=2, column=1)
b.bind("<Button-1>", click)

b = Button(f, text="5", bg="light blue", padx=28, pady=18, font="lucida 25 bold")
b.grid(row=2, column=2)
b.bind("<Button-1>", click)

b = Button(f, text="4", bg="light blue", padx=28, pady=18, font="lucida 25 bold")
b.grid(row=2, column=3)
b.bind("<Button-1>", click)

b = Button(f, text="-", bg="light green", padx=35, pady=18, font="lucida 25 bold")
b.grid(row=2, column=4)
b.bind("<Button-1>", click)

b = Button(f, text="%", bg="orange", padx=23, pady=18, font="lucida 25 bold")
b.grid(row=2, column=5)
b.bind("<Button-1>", click)

b = Button(f, text="00", bg="light blue", padx=19, pady=18, font="lucida 25 bold")
b.grid(row=5, column=2)
b.bind("<Button-1>", click)

b = Button(f, text="3", bg="light blue", padx=28, pady=18, font="lucida 25 bold")
b.grid(row=3, column=1)
b.bind("<Button-1>", click)

b = Button(f, text="2", bg="light blue", padx=28, pady=18, font="lucida 25 bold")
b.grid(row=3, column=2)
b.bind("<Button-1>", click)

b = Button(f, text="1", bg="light blue", padx=28, pady=18, font="lucida 25 bold")
b.grid(row=3, column=3)
b.bind("<Button-1>", click)

b = Button(f, text="*", bg="light green", padx=35, pady=18, font="lucida 25 bold")
b.grid(row=3, column=4)
b.bind("<Button-1>", click)

b = Button(f, text="C", bg="yellow", padx=24, pady=18, font="lucida 25 bold")
b.grid(row=3, column=5)
b.bind("<Button-1>", click)

b = Button(f, text="/", bg="light green", padx=37, pady=18, font="lucida 25 bold")
b.grid(row=5, column=4)
b.bind("<Button-1>", click)

b = Button(f, text=".", bg="light green", padx=32, pady=18, font="lucida 25 bold")
b.grid(row=5, column=3)
b.bind("<Button-1>", click)

b = Button(f, text="d", bg="red", padx=25, pady=18, font="lucida 25 bold")
b.grid(row=5, column=5)
b.bind("<Button-1>", d)

f.pack(side=LEFT, anchor="nw")  # packed the frame

root.mainloop()  # ran it
