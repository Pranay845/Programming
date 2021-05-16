"""
Notepad
"""

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newfile():
    global file
    root.title("untitled")  # reseting the file
    file = None
    textarea.delete(1.0, END)  # removed everything


def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])  # given extension
    if file == "":
        file = None  # reseted it
    else:
        global f
        root.title(os.path.basename(file) + "- notepad")  # for showing name
        textarea.delete(1.0, END)  # to show new file
        f = open(file, "r")  # to show file
        textarea.insert(1.0, f.read())  # to read file
        f.close()  # closed it


def savefile():
    global file
    if file is None:  # to save file
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None  # reseting it

        else:
            # Save as a new file
            global f
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()


def quitapp():
    root.destroy()  # to close the the app


def cut():
    textarea.event_generate("<<Cut>>")  # to cut the the text


def copy():
    textarea.event_generate("<<Copy>>")  # to copy the the text


def paste():
    textarea.event_generate("<<Paste>>")  # to paste the the text


def about():
    showinfo("notepad", "a notepad by madhav")  # to show the help box


root = Tk()
root.title("Untitled - Notepad")  # given title for first file
root.wm_iconbitmap("notepad.ico")  # given icon
root.geometry("500x500")  # given window size

textarea = Text(root, font="lucida 12")  # kept a area for writing
file = None  # the file for nothing
textarea.pack(expand=True, fill=BOTH)  # stretching it
Menubar = Menu(root)  # made a menu bar

# File menu
filemenu = Menu(Menubar, tearoff=0)
filemenu.add_command(label="New", command=newfile)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_separator()  # a line
filemenu.add_command(label="Exit", command=quitapp)
Menubar.add_cascade(label="File", menu=filemenu)  # given it to menubar

# Edit menu
editmenu = Menu(Menubar, tearoff=0)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)
Menubar.add_cascade(label="Edit", menu=editmenu)  # given it to menubar

# Help menu
helpmenu = Menu(Menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
Menubar.add_cascade(label="Help", menu=helpmenu)  # given it to menubar

root.config(menu=Menubar)  # given menubar to root

# Scroll bar
scrollbar = Scrollbar(textarea)
scrollbar.pack(side=RIGHT, fill=Y)  # packed it
scrollbar.config(command=textarea.yview)  # given scrollbar to root
textarea.config(yscrollcommand=scrollbar.set)  # set scrollbar to textarea

root.mainloop()  # ran it
