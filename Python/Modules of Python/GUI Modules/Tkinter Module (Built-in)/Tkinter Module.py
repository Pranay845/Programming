"""
Tkinkter Module is for Making GUIs.
"""

from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg

root1 = Tk()  # delcartion of window

# Gui logic here
root1.mainloop()  # a loop which runs the gui

# Window making
root2 = Tk()

# Width x Height
root2.geometry("644x434")

# Width, height
root2.minsize(300, 100)

# Width, height
root2.maxsize(1200, 988)

# Topic: Label
"""
label is a display where user cannot interact.
"""

label = Label(text="pranay is a good boy and this is his GUI")
label.pack()  # this is a packing machine

root2.mainloop()

# Topic: Inserting Image in gui
root3 = Tk()

root3.geometry("1255x944")
# photo = PhotoImage(file="1.png")

# For Jpg Images
image = Image.open("Sign.jpg")  # opening the image
photo = ImageTk.PhotoImage(image)  # adding the image

labeling = Label(image=photo)  # making label for image
labeling.pack()

root3.mainloop()

# Topic: Attributes of label,pack
root4 = Tk()
root4.geometry("744x133")
root4.title("My GUI ")

# SubTopic: Important Label Options
"""
text - adds the text
bd - background
fg - foreground
font - sets the font
1. font=("comicsansms", 19, "bold")
2. font="comicsansms 19 bold"

padx - x padding
pady - y padding
relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE
"""
title_label = Label(text="Pranay is a good boy")


# SubTopic: Important Pack options
"""
anchor = nw
side = top, bottom, left, right
fill
padx
pady
"""

title_label.pack(side=BOTTOM, anchor="sw", fill=X)
title_label.pack(side=LEFT, fill=Y, padx=34, pady=34)

root4.mainloop()

# Topic: Frames
"""
Frame is a box in gui.
"""

root5 = Tk()
root5.geometry("655x333")

f1 = Frame(root5, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root5, borderwidth=8, bg="grey", relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l = Label(f1, text="Pycharm")
l.pack(pady=142)

l = Label(f2, text="Welcome to gui", font="Helvetica 16 bold", fg="red", pady=22)
l.pack()

root5.mainloop()

# Topic: Buttons
"""
Button is a trigger a thing to happen like opening.
"""

root6 = Tk()
root6.geometry("655x333")


def hello():
    print("Buttons")


def name():
    print("Name is madhav")


frame = Frame(root6, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, fg="red", text="Print now",
            command=hello)  # this a button and it has a command so should not give ()
b1.pack(side=LEFT, padx=23)

b2 = Button(frame, fg="red", text="Tell me name now", command=name)
b2.pack(side=LEFT, padx=23)

b3 = Button(frame, fg="red", text="Print now")
b3.pack(side=LEFT, padx=23)

b4 = Button(frame, fg="red", text="Print now")
b4.pack(side=LEFT, padx=23)
root6.mainloop()

# Topic: Login System (Grid,Entry Widget)
"""
Entry widget is something like giving values.
"""


def getvals():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")


root7 = Tk()
root7.geometry("655x333")

user = Label(root7, text="Username")
password = Label(root7, text="Password")
user.grid()  # this is a way of packing(in excel)
password.grid(row=1)

# SubTopic: Variable classes in tkinter
"""
BooleanVar, DoubleVar, IntVar, StringVar
"""
uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root7, textvariable=uservalue)
passentry = Entry(root7, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getvals).grid()

root7.mainloop()

# Topic: Travel Form (Checkbutton)
root8 = Tk()


def getvals():
    print("It works!")


root8.geometry("644x344")
# Heading
Label(root8, text="Welcome to penta Travels", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

# Text for our form
name = Label(root8, text="Name")
phone = Label(root8, text="Phone")
gender = Label(root8, text="Gender")
emergency = Label(root8, text="Emergency Contact")
paymentmode = Label(root8, text="Payment Mode")

# Pack text for our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

# Tkinter variable for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

# Entries for our form
nameentry = Entry(root8, textvariable=namevalue)
phoneentry = Entry(root8, textvariable=phonevalue)
genderentry = Entry(root8, textvariable=gendervalue)
emergencyentry = Entry(root8, textvariable=emergencyvalue)
paymentmodeentry = Entry(root8, textvariable=paymentmodevalue)

# Packing the Entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

# Checkbox & Packing it
# Checkbox name refers the meaning
foodservice = Checkbutton(text="Want to prebook your meals?", variable=foodservicevalue)
foodservice.grid(row=6, column=3)

# Button & packing it and assigning it a command
Button(text="Submit to pranay Travels", command=getvals).grid(row=7, column=3)

root8.mainloop()

# Topic: Advanced Travel Form
root9 = Tk()


def getvals():
    print("Submitting form")

    print(
        f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()} ")

    with open("records.txt", "a") as f:
        f.write(
            f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n ")


root9.geometry("644x344")

# Heading
Label(root9, text="Welcome to penta Travels", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

# Text for our form
name = Label(root9, text="Name")
phone = Label(root9, text="Phone")
gender = Label(root9, text="Gender")
emergency = Label(root9, text="Emergency Contact")
paymentmode = Label(root9, text="Payment Mode")

# Pack text for our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

# Tkinter variable for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

# Entries for our form
nameentry = Entry(root9, textvariable=namevalue)
phoneentry = Entry(root9, textvariable=phonevalue)
genderentry = Entry(root9, textvariable=gendervalue)
emergencyentry = Entry(root9, textvariable=emergencyvalue)
paymentmodeentry = Entry(root9, textvariable=paymentmodevalue)

# Packing the Entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

# Checkbox & Packing it
foodservice = Checkbutton(text="Want to prebook your meals?", variable=foodservicevalue)
foodservice.grid(row=6, column=3)

# Button & packing it and assigning it a command
Button(text="Submit to Harry Travels", command=getvals).grid(row=7, column=3)

root9.mainloop()

# Topic: Canvas
"""
Canvas is like a board where we draw or write.
"""

root10 = Tk()

canvas_width = 800
canvas_height = 400

root10.geometry(f"{canvas_width}x{canvas_height}")
root10.title("pranay and madhav GUI")
can_widget = Canvas(root10, width=canvas_width, height=canvas_height)
can_widget.pack()

# The line goes from the point x1, y1 to x2, y2
can_widget.create_line(0, 0, 800, 400, fill="red")
can_widget.create_line(0, 400, 800, 0, fill="red")

# To create a rectangle specify parameters in this order - coors of top left and coors of bottom right
can_widget.create_rectangle(3, 5, 700, 300, fill="blue")

can_widget.create_text(200, 200, text="python")

can_widget.create_oval(344, 233, 244, 355)

root10.mainloop()


# Topic: Events
def good(event):
    print(f"You clicked on the button at {event.x}, {event.y}")


root11 = Tk()
root11.title("Events")
root11.geometry("644x334")

widget = Button(root11, text='Click me please')
widget.pack()

widget.bind('<Button-1>', good)  # bind means waiting for a thing to happen
widget.bind('<Double-1>', quit)

root11.mainloop()

# Topic: Menus and Submenus
root12 = Tk()
root12.geometry("733x566")
root12.title("Pycharm")


def myfunc():
    print("i am a good function")


# Use these to create a non dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)
mainmenu = Menu(root12)

# Making a menu
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()  # a line in between
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
root12.config(menu=mainmenu)  # giving it the right
mainmenu.add_cascade(label="File", menu=m1)

# Another menu
m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)
root12.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

root12.mainloop()

# Topic: Message box
root13 = Tk()
root13.geometry("733x566")
root13.title("Pycharm")


def myfunc():
    print("i am a bad function")


def help():
    print("I will help you")
    tmsg.showinfo("Help", "helping")  # showes info


def rate():
    print("Rate us")
    # Asks question
    value = tmsg.askquestion("Was your experience Good?", "You used this gui.. Was your experience Good?")
    if value == "yes":
        msg = "Great. Rate us on appstore please"
    else:
        msg = "Tell us what went wrong. We will call you soon"
    tmsg.showinfo("Experience", msg)


def madhav():
    # Retry Cancel
    ans = tmsg.askretrycancel("friends", "Sorry")
    if ans:
        print("Retry")

    else:
        print("cancel")


mainmenu = Menu(root13)

m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
root13.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)
root13.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate us", command=rate)
m3.add_command(label="Befriend madhav", command=madhav)
mainmenu.add_cascade(label="Help", menu=m3)
root13.config(menu=mainmenu)
root13.mainloop()

# Topic: Slider
"""
slider is like a zip.
"""

root14 = Tk()
root14.geometry("455x233")
root14.title("Slider")


def getdollar():
    print(f"We have credited {myslider2.get()} dollars to your bank account")
    tmsg.showinfo("Amount Credited!", f"We have credited {myslider2.get()} dollars to your bank account")


# myslider = Scale(root, from_=0, to=100)
# myslider.pack()
Label(root14, text="How many dollars do you want?").pack()

myslider2 = Scale(root14, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
myslider2.set(34)
myslider2.pack()

Button(root14, text="Get dollars!", pady=10, command=getdollar).pack()

root14.mainloop()

# Topic: Radiobutton
"""
Radio button is a button which is inspired by radios.
"""

root15 = Tk()
root15.geometry("455x233")
root15.title("Radiobutton")


def order():
    tmsg.showinfo("Order Received!", f"We have received your order for {var.get()}. Thanks for ordering")


# var = IntVar()
var = StringVar()
var.set("Radio")
# var.set(1)
Label(root15, text="What would you like to have sir?", font="lucida 19 bold",
      justify=LEFT, padx=14).pack()

radio = Radiobutton(root15, text="Dosa", padx=14, variable=var, value="Dosa").pack(anchor="w")
radio = Radiobutton(root15, text="Idly", padx=14, variable=var, value="Idly").pack(anchor="w")
radio = Radiobutton(root15, text="Paratha", padx=14, variable=var, value="Paratha").pack(anchor="w")
radio = Radiobutton(root15, text="Samosa", padx=14, variable=var, value="Samosa").pack(anchor="w")

Button(text="Order Now", command=order).pack()

root15.mainloop()


# Topic: Listbox
def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i += 1


i = 0
root16 = Tk()
root16.geometry("455x233")
root16.title("Listbox")

lbx = Listbox(root16)  # it's a box of elements
lbx.pack()
lbx.insert(END, "First item of our listbox")

Button(root16, text="Add Item", command=add).pack()

root16.mainloop()

# Topic: Scroll Bar
root17 = Tk()
root17.geometry("455x233")
root17.title("Scrollbar ")

# For connecting scrollbar to a widget
# 1. widget(yscrollcommand = scrollbar.set)
# 2 scrollbar.config(command=widget.yview)
scrollbar = Scrollbar(root17)
scrollbar.pack(side=RIGHT, fill=Y)

# listbox = Listbox(root, yscrollcommand = scrollbar.set)
# for i in range(344):
#     listbox.insert(END, f"Item {i}")

# listbox.pack(fill="both",padx=22 )
text = Text(root17, yscrollcommand=scrollbar.set)
text.pack(fill=BOTH)

# scrollbar.config(command=listbox.yview)
scrollbar.config(command=text.yview)

root17.mainloop()

# Topic: Status bar
"""
This is a bar which represents the values.
"""


def upload():
    statusvar.set("Busy..")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready")


root18 = Tk()
root18.geometry("455x233")
root18.title("Status bar")

statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root18, textvariable=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)
Button(root18, text="Upload", command=upload).pack()

root18.mainloop()


# Topic: Classes and Objects
class GUI(Tk):
    # self means root
    def __init__(self):
        __init__ = super().__init__()
        self.geometry("744x377")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvar=self.var, relief=SUNKEN, anchor="w")
        self.statusbar.pack(side=BOTTOM, fill=X)

    @staticmethod
    def click():
        print("Button clicked")

    def createbutton(self, inptext):
        Button(text=inptext, command=self.click).pack()


if __name__ == '__main__':
    window = GUI()
    window.status()
    window.createbutton("Click me")
    window.mainloop()

# Topic: Icons
root19 = Tk()
root19.geometry("655x444")
root19.title("Title Of My GUI")
root19.wm_iconbitmap("notepad.ico")
root19.configure(background="grey")

width = root19.winfo_screenwidth()
height = root19.winfo_screenheight()

print(f"{width}x{height}")

# destroy means close
Button(text="Close", command=root19.destroy).pack()

root19.mainloop()

# Documentation: https://docs.python.org/3/library/tk.html
