'''
from tkinter import *

root = Tk()
root.title = 'IT STEP'
root.geometry('1000x400')

check = Label(text='', font=10)
check.place(x=50, y=230)

name = Label(text='Name', font=15)
name.place(x= 50, y=50)

entry1 = Entry(width=30)
entry1.place(x=50, y=80)

password = Label(text='Password', font=15)
password.place(x=50, y=110)

entry2 = Entry(width=30,show='*')
entry2.place(x=50, y=140)

def func():
    if entry1.get() == 'john' and entry2.get() == '12345':
        check['text'] = 'Successful'
        check['fg'] = 'green'
    else:
        check['text'] = 'Fail'
        check['fg'] = 'red'


button1 = Button(text='Login', width=10, command=func)
button1.place(x=50, y=200)

root.mainloop()
'''
# calculator
from tkinter import *

root = Tk()
root.title = 'IT STEP'
root.geometry('1000x400')


def add():
    netice = int(entry1.get()) + int(entry2.get())
    cavab['text'] = netice


def minus():
    netice = int(entry1.get()) - int(entry2.get())
    cavab['text'] = netice


def mul():
    netice = int(entry1.get()) * int(entry2.get())
    cavab['text'] = netice


def div():
    netice = int(entry1.get()) / int(entry2.get())
    cavab['text'] = netice


entry1 = Entry(width=30)
entry1.place(x=50, y=70)

entry2 = Entry(width=30)
entry2.place(x=600, y=70)

toplama = Button(text='+', font=20, width=15, command=add)
toplama.place(x=300, y=120)

cixma = Button(text='-', font=20, width=15, command=minus)
cixma.place(x=300, y=170)

vurma = Button(text='x', font=20, width=15, command=mul)
vurma.place(x=300, y=220)

bolme = Button(text='/', font=20, width=15, command=div)
bolme.place(x=300, y=270)

cavab = Label(text='', font=15)
cavab.place(x=600, y=320)

root.mainloop()