import tkinter
from tkinter import *
from tkinter import ttk
import re
from tkinter import messagebox

lform = tkinter.Tk()
lform.title('Login')
lform.geometry('600x400+350+184')
lform.resizable(False, False)
photo=PhotoImage(file='resize-15764595411719337967images5.png')
labelphoto=Label(lform,image=photo).pack()

PL = PhotoImage(file='resize-15764242081667221693loginbutton.png')
LL1 = ttk.Label(lform, text='Login To Your Account', font=('impact', 20)).pack()
LL6 = ttk.Label(lform,
                text='ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ').pack()
LL2 = ttk.Label(lform, text='Your ID', font=('impact', 15)).place(x=100, y=140)
LL3 = ttk.Label(lform, text='Password', font=('impact', 15)).place(x=100, y=180)
TL1 = ttk.Entry(lform, font=('consolas', 15))
TL2 = ttk.Entry(lform, font=('consolas', 15),show='*')

def project():
    id = TL1.get()
    pas = TL2.get()
    if id != '' and pas != '':
        messagebox.showinfo('Loggedin', 'Succeded')
        lform.destroy()
        import Project
    else:
        messagebox.showerror('Error','Path Empty')
TL1.place(x=230, y=140)
TL2.place(x=230, y=180)
BL1 = ttk.Button(lform, image=PL, command=project).place(x=450, y=340)
lform.mainloop()

