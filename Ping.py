import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

pform = tkinter.Tk()
pform.title('Ping-Pong Tournament')
pform.geometry('600x400+350+184')
pform.resizable(False, False)
photo=PhotoImage(file='resize-1576459460946449023images2.png')
labelphoto=Label(pform,image=photo).pack()

PP = PhotoImage(file='resize-15763549672126938837downloada7aaaaaa.png')
LP1 = ttk.Label(pform, text='Hit Like a Hummer', font=('impact', 20)).pack()
LP6 = ttk.Label(pform,
                text='ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ').pack()
LP2 = ttk.Label(pform, text='Name', font=('impact', 15)).place(x=150, y=100)
LP4 = ttk.Label(pform, text='Year', font=('impact', 15)).place(x=150, y=140)
TP1 = ttk.Entry(pform, font=('consolas', 15))
C2 = ttk.Combobox(pform, state='readonly', value=('Choose a year', 'First Year', 'Second Year', 'Third Year-CS', 'Third Year-IT', 'Third Year-IS', 'Third Year-SE','Fourth Year-CS', 'Fourth Year-IT', 'Fourth Year-IS', 'Fourth Year-SE'))
C2.current(0)
C2.place(x=240, y=145)
def msg():
    np = TP1.get()
    if np != '':
        messagebox.showinfo('Loggedin', 'Succeded,you are in')
        pform.destroy()
    else:
        messagebox.showerror('Error', 'Path Empty')
TP1.place(x=240, y=100)
BP1 = ttk.Button(pform, image=PP,command=msg).place(x=230, y=250)
pform.mainloop()
