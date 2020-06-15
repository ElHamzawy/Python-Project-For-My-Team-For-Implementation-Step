import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

mform = tkinter.Tk()
mform.title('FCI - Activities')
mform.geometry('600x400+350+184')
mform.resizable(False,False)
photo=PhotoImage(file='resize-15764595641906547456images6.png')
labelphoto=Label(mform,image=photo).pack()

PB1 = PhotoImage(file='resize-15762732911928669665tela1splash.png')
PB2 = PhotoImage(file='resize-15762728891751514287karate76797386.png')
PB3 = PhotoImage(file='resize-15762736821033503647-images.png')
PB4 = PhotoImage(file='resize-15762741181681521685pingponglogomakero41klu5rha920x6c65fd2qqg4o003jwtfiho7q1zi8.png')
PB5 = PhotoImage(file='resize-1576274396857112158download.png')
PB6 = PhotoImage(file='resize-1576276733819248764IMG20191214WA0000.png')
L1 = ttk.Label(mform,text='Welcome To Our Tournament',font=('impact',20)).pack()
L2 = ttk.Label(mform,text='Pick a Game',font=('impact',20)).place(x=240,y=10)
L3 = ttk.Label(mform,text='ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ').pack()
L4 = ttk.Label(mform,text='ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ').place(x=240,y=40)
def football():
    mform.destroy()
    import Football
def karate():
    mform.destroy()
    import Karate
def chess():
    mform.destroy()
    import Chess
def ping():
    mform.destroy()
    import Ping
def music():
    mform.destroy()
    import Music
B1 = ttk.Button(mform,image=PB1,command=football).place(x=65,y=150)
B2 = ttk.Button(mform,image=PB2,command=karate).place(x=165,y=150)
B3 = ttk.Button(mform,image=PB3,command=chess).place(x=265,y=150)
B4 = ttk.Button(mform,image=PB4,command=ping).place(x=365,y=150)
B5 = ttk.Button(mform,image=PB5,command=music).place(x=465,y=150)
mform.mainloop()