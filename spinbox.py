from tkinter import *

root=Tk()
root.title("Spinning")
w=Spinbox(root,from_=0,to=100)
w.pack()

root.mainloop()