import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

kform = tkinter.Tk()
kform.title('Karate Tournament')
kform.geometry('600x400+350+184')
kform.resizable(False, False)
photo=PhotoImage(file='resize-157645647920454813312569e50c62ef4c4da351d71a812be141640.png')
labelphoto=Label(kform,image=photo).pack()

PK = PhotoImage(file='resize-15763549672126938837downloada7aaaaaa.png')
LK1 = ttk.Label(kform, text='Fight as a Champion', font=('impact', 20)).pack()
LK6 = ttk.Label(kform,
                text='ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ').pack()
LK2 = ttk.Label(kform, text='Name', font=('impact', 15)).place(x=165, y=120)
LK4 = ttk.Label(kform, text='Year', font=('impact', 15)).place(x=165, y=160)
LK5 = ttk.Label(kform, text='Branch', font=('impact', 15)).place(x=165, y=200)
C1 = ttk.Combobox(kform, state='readonly', value=('Choose a branch','Kata','Komote'))
C1.current(0)
C1.place(x=260, y=202)
TK1 = ttk.Entry(kform, font=('consolas', 15))
C2 = ttk.Combobox(kform, state='readonly', value=('Choose a year', 'First Year', 'Second Year', 'Third Year-CS', 'Third Year-IT', 'Third Year-IS', 'Third Year-SE','Fourth Year-CS', 'Fourth Year-IT', 'Fourth Year-IS', 'Fourth Year-SE'))
C2.current(0)
C2.place(x=260, y=162)
def msg():
    nk = TK1.get()
    if nk != '':
        messagebox.showinfo('Loggedin', 'Succeded,you are in')
        kform.destroy()
        import Project
    else:
        messagebox.showerror('Error','Path Empty')
TK1.place(x=260, y=120)
BK1 = ttk.Button(kform, image=PK,command=msg).place(x=240, y=290)
kform.mainloop()