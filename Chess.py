import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

cform = tkinter.Tk()
cform.title('Chess Tournament')
cform.geometry('600x400+350+184')
cform.resizable(False, False)
photo=PhotoImage(file='resize-1576456812371759139images.png')
labelphoto=Label(cform,image=photo).pack()

PC = PhotoImage(file='resize-15763549672126938837downloada7aaaaaa.png')
LC1 = ttk.Label(cform, text='Intelligence Is Power', font=('impact', 20)).pack()
LC6 = ttk.Label(cform,
                text='ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ').pack()
LC2 = ttk.Label(cform, text='Name', font=('impact', 15)).place(x=165, y=130)
LC4 = ttk.Label(cform, text='Year', font=('impact', 15)).place(x=165, y=170)
TC1 = ttk.Entry(cform, font=('consolas', 15))
C2 = ttk.Combobox(cform, state='readonly', value=('Choose a year', 'First Year', 'Second Year', 'Third Year-CS', 'Third Year-IT', 'Third Year-IS', 'Third Year-SE','Fourth Year-CS', 'Fourth Year-IT', 'Fourth Year-IS', 'Fourth Year-SE'))
C2.current(0)
C2.place(x=260, y=172)
def msg():
    nc = TC1.get()
    if nc != '':
        messagebox.showinfo('Loggedin', 'Succeded,you are in')
        cform.destroy()
    else:
        messagebox.showerror('Error','Path Empty')
TC1.place(x=260, y=130)
BC1 = ttk.Button(cform, image=PC,command=msg).place(x=230, y=290)
cform.mainloop()
