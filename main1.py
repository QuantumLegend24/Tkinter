from tkinter import*

root=Tk()

root.geometry("500x500")

btn=Button(root,text="Click Me! ",bd="5",background="cyan",command=root.destroy)
btn.pack(side="bottom")

root.mainloop()