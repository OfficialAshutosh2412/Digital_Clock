# module import
from tkinter import *
from time import *
# window(GUI) creation
root = Tk()
root.title("Digital CLock")
root.geometry("600x300+360+100")
root.config(bg="palegreen1")
clkLabel = Label(root, font=('Ariel', 50), bg="palegreen1")
clkLabel.place(relx=0.5, rely=0.5, anchor=CENTER)

def myTime():
    format = strftime('%I : %M : %S %p')
    clkLabel.config(text=format)
    clkLabel.after(1000, myTime)

myTime()

root.mainloop()
