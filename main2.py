from tkinter import*

root=Tk()

root.geometry("500x500")

root.title("Login Me")
root.config(bg="cyan")

btn=Button(root,text="Submit",command=root.destroy).place(x=40,y=130)
user_name=Label(root,text="Username").place(x=40,y=60)
user_name_entry=Entry(root,width=30).place(x=110,y=60)
password=Label(root,text="Password").place(x=40,y=100)
password_entry=Entry(root,show="*",width=30).place(x=110,y=100)

root.mainloop()