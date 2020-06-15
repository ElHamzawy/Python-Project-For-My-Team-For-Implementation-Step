import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

muform = tkinter.Tk()
muform.title('Music Tournament')
muform.geometry('600x400+350+184')
muform.resizable(False, False)
photo=PhotoImage(file='resize-1576459502808797592images3.png')
labelphoto=Label(muform,image=photo).pack()

PMU = PhotoImage(file='resize-15763549672126938837downloada7aaaaaa.png')
LMU1 = ttk.Label(muform, text='Music Is Soul Power', font=('impact', 20)).pack()
LMU6 = ttk.Label(muform,
                text='ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ').pack()
LMU2 = ttk.Label(muform, text='Name', font=('impact', 15)).place(x=150, y=100)
LMU4 = ttk.Label(muform, text='Year', font=('impact', 15)).place(x=150, y=140)
LMU5 = ttk.Label(muform, text='Instrument', font=('impact', 15)).place(x=150, y=180)
TMU1 = ttk.Entry(muform, font=('consolas', 15))
C2 = ttk.Combobox(muform, state='readonly', value=('Choose a year', 'First Year', 'Second Year', 'Third Year-CS', 'Third Year-IT', 'Third Year-IS', 'Third Year-SE','Fourth Year-CS', 'Fourth Year-IT', 'Fourth Year-IS', 'Fourth Year-SE'))
C2.current(0)
C2.place(x=260, y=142)
C2 = ttk.Combobox(muform, state='readonly', value=('Choose an instruments','Singing','Violin', 'Guitar', 'Biano', 'Kanon', 'Oud', 'Nai', 'Clarenit','Tabla', 'Xelefon'))
C2.current(0)
C2.place(x=260, y=185)

def msg():
    nmu = TMU1.get()
    if nmu != '':
        messagebox.showinfo('Loggedin', 'Succeded,you are in')
        muform.destroy()
    else:
        messagebox.showerror('Error', 'Path Empty')
TMU1.place(x=260, y=100)
BMU1 = ttk.Button(muform, image=PMU,command=msg).place(x=230, y=250)
muform.mainloop()