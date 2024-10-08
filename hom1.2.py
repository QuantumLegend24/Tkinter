from tkinter import *

root=Tk()
root.geometry("500x500")

root.title("Roblit")
root.config(bg="gold")

btn=Button(root,text="Create Repl",command=root.destroy).place(x=250,y=250)
user_name_label=Label(root,text="Pick a Template: ").place(x=100,y=70)
user_name_entry=Entry(root,width=30).place(x=100,y=100)
project_name_label=Label(root,text="Name your project: ").place(x=100,y=150)
project_name_entry=Entry(root,width=30).place(x=100,y=180)


root.mainloop()