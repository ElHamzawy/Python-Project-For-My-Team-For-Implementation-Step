import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

fform = tkinter.Tk()
fform.title('Football Tournament')
fform.geometry('600x400+350+184')
fform.resizable(False, False)
#photo
photo=PhotoImage(file='cr7.png')
labelphoto=Label(fform,image=photo).pack()

PF = PhotoImage(file='resize-15763549672126938837downloada7aaaaaa.png')
LF1 = ttk.Label(fform, text='Work Hard Play Hard', font=('impact', 20)).pack()
LF6 = ttk.Label(fform,
                text='ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ').pack()
LF2 = ttk.Label(fform, text='Team Name', font=('impact', 15)).place(x=110, y=80)
LF3 = ttk.Label(fform, text='Kit Color', font=('impact', 15)).place(x=110, y=120)
LF4 = ttk.Label(fform, text='Year', font=('impact', 15)).place(x=110, y=160)
LF5 = ttk.Label(fform, text='Team Leader', font=('impact', 15)).place(x=110, y=200)
TF1 = ttk.Entry(fform, font=('consolas', 15))
TF2 = ttk.Entry(fform, font=('consolas', 15))
TF4 = ttk.Entry(fform, font=('consolas', 15))
C1 = ttk.Combobox(fform, state='readonly', value=('Choose a year', 'First Year', 'Second Year', 'Third Year-CS', 'Third Year-IT', 'Third Year-IS', 'Third Year-SE','Fourth Year-CS', 'Fourth Year-IT', 'Fourth Year-IS', 'Fourth Year-SE'))
C1.current(0)
C1.place(x=365, y=160)
def msg():
    tn = TF1.get()
    kc = TF2.get()
    tl = TF4.get()
    if tn != '' and kc != '' and tl !='':
        messagebox.showinfo('Loggedin', 'Succeded,you are in')
        fform.destroy()
        import Project
    else:
        messagebox.showerror('Error','Path Empty')
TF1.place(x=365, y=80)
TF2.place(x=365, y=120)
TF4.place(x=365, y=200)
BF1 = ttk.Button(fform, image=PF,command=msg).place(x=230, y=300)
fform.mainloop()