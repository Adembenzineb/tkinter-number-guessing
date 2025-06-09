from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

root = Tk()
root.geometry('450x300')
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
    elif not((n.isdecimal())) or not(m.isdecimal()) :
        messagebox.showerror("Invalid Input", "Please enter a number!")
    else:
        global num,gs
        max = int(m)
        min = int(n)
        num = randint(min,max)
        gs = 0
    res.config(text="You have {chn} guesses")
    


def guessing():
    global gs,ch
    
    guessc = txtg.get()
    if guessc == "" or not(guessc.isdecimal()):
        messagebox.showerror("Invalid Input", "Please enter a valid number!")

    gs += 1
    guess = int(txtg.get())
    if guess == num :
        ch =  "Correct! The number is {num}. You guessed it in {gs} attempts."
    elif gs >= chn and guess != num :
        ch = "Sorry! The number was {num}. Better luck next time."
    elif guess > num :
        ch = "Too high !"
    elif guess < num :
        ch = "Too low !"

    res.config(text=ch)




bts = Button(root,text="Start",command= play )
bts.grid(column=2,row=3)

l2 = Label(root,)

lg = Label(root ,text="Enter your guess :", font=title_font)
lg.grid(column=0,row=4)
txtg = Entry(root,width=5)
txtg.grid(column=1,row=4)

bte = Button(root,text="Enter",command= guessing)
bte .grid(column=2,row=4)

chn = 7
gs = 0
ch = "you have 7 guesses"
res = Label(root,text=ch, font=title_font)
res.grid(column=2,row=5)


btq = Button(root ,text="Quit",command=root.destroy)
btq.grid(column=2,row=20)
root.mainloop()
