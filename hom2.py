from tkinter import *

root=Tk()
root.geometry("700x700")

root.title("Domino's")
root.config(bg="grey")

btn=Button(root,text="Place order!",command=root.destroy).place(x=400,y=650)

pizza_label=Label(root,text="*Choose your pizza: ").place(x=100,y=70)
pizza_entry=Entry(root,width=30).place(x=100,y=100)

name_label=Label(root,text="*Full name: ").place(x=100,y=150)
name_entry=Entry(root,width=30).place(x=100,y=180)

age_label=Label(root,text="*Age: ").place(x=100,y=230)
age_entry=Entry(root,width=30).place(x=100,y=260)

address_label=Label(root,text="*Address: ").place(x=100,y=310)
address_entry=Entry(root,width=30).place(x=100,y=340)

card_label=Label(root,text="*Card no. and Bank: ").place(x=100,y=390)
card_entry=Entry(root,width=30).place(x=100,y=410)

coupon_label=Label(root,text="Coupon no. and further instructions: ").place(x=100,y=470)
coupon_entry=Entry(root,width=30).place(x=100,y=500)

coupon_label=Label(root,text="* is necessary to fill in!").place(x=100,y=600)

root.mainloop()