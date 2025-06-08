from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry('350x300')
root.title("Number guessing game")

title_font = ("Arial", 10)

l1 = Label(root ,  text="select the range", font=title_font)
l1.grid(column=2,row=0)

ln = Label(root ,  text="select minimum", font=title_font)
ln.grid(column=0,row=1)
txtn = Entry(root,width=5)
txtn.grid(column = 1,row = 1)

lm = Label(root ,  text="select maximum", font=title_font)
lm.grid(column=0,row=2)
txtm = Entry(root,width=5)
txtm.grid(column = 1,row = 2)

def play():
    n = txtn.get()
    m = txtm.get()

    if n == "" or m == "" :
        messagebox.showerror("Invalid Input", "Please enter a number!")
    elif not(n.isdecimal) or not(m.isdecimal) :
        messagebox.showerror("Invalid Input", "Please enter a number!")
    else:
        max = int(m)
        min = int(n)


bts = Button(root,text="Start",command= play )
bts.grid(column=2,row=3)



btq = Button(root ,text="Quit",command=root.destroy)
btq.grid(column=2,row=20)
root.mainloop()
