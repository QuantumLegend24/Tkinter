from tkinter import *
#Tkinter tool kit - Button, Checkbutton, Entry, Frame, Label, LabelFrame, Menubutton, PanedWindow, Radiobutton, Scale and Scrollbar
from tkinter.ttk import *

root=Tk()
root.title("Menu Demonstration")

#creating menubar
menubar=Menu(root)

#adding file menu and commands
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='New File', command=None)
file.add_command(label='Open...', command=None)
file.add_command(label='Save', command=None)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)



root.config(menu=menubar)
root.mainloop()