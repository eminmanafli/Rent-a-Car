from tkinter import *


def calculate():
    try:
        result = str(eval(user_input['text']))
        cavab['text'] = result
    except SyntaxError:
        user_input['text'] = 'Melumatlari duzgun daxil edin! '
    except ZeroDivisionError:
        user_input['text'] = '0-a bolmek olmaz!'


def reqem(sym):
    user_input['text'] += sym


def cl():
    user_input['text'] = ''
    cavab['text'] = ''


root = Tk()
root.title("METANIT.COM")
root.geometry("600x600")

for c in range(4): root.columnconfigure(index=c, weight=1)
for r in range(5): root.rowconfigure(index=r, weight=1)

bir = Button(text='1', font=15, command=lambda : reqem('1'))
bir.grid(column=0, row=1, sticky='nsew')

iki = Button(text='2', font=15, command=lambda : reqem('2'))
iki.grid(column=1, row=1, sticky='nsew')

uc = Button(text='3', font=15, command=lambda : reqem('3'))
uc.grid(column=2, row=1, sticky='nsew')

plus = Button(text='+', font=('arial', 20, 'bold'), bg='orange', fg='black', command=lambda : reqem('+'))
plus.grid(column=3, row=1, sticky='nsew')

dord = Button(text='4', font=15, command=lambda : reqem('4'))
dord.grid(column=0, row=2, sticky='nsew')

bes = Button(text='5', font=15, command=lambda : reqem('5'))
bes.grid(column=1, row=2, sticky='nsew')

alti = Button(text='6', font=15, command=lambda : reqem('6'))
alti.grid(column=2, row=2, sticky='nsew')

minus = Button(text='-', font=('arial', 20, 'bold'), bg='orange', fg='black', command=lambda : reqem('-'))
minus.grid(column=3, row=2, sticky='nsew')

yeddi = Button(text='7', font=15, command=lambda : reqem('7'))
yeddi.grid(column=0, row=3, sticky='nsew')

sekkiz = Button(text='8', font=15, command=lambda : reqem('8'))
sekkiz.grid(column=1, row=3, sticky='nsew')

doqquz = Button(text='9', font=15, command=lambda : reqem('9'))
doqquz.grid(column=2, row=3, sticky='nsew')

multi = Button(text='x', font=('arial', 20, 'bold'), bg='orange', fg='black', command=lambda : reqem('*'))
multi.grid(column=3, row=3, sticky='nsew')

clear = Button(text='C', font=('arial', 20, 'bold'), bg='cyan', fg='black', command=cl)
clear.grid(column=0, row=4, sticky='nsew')

sifir = Button(text='0', font=15, command=lambda : reqem('0'))
sifir.grid(column=1, row=4, sticky='nsew')

equal = Button(text='=', font=('arial', 20, 'bold'), bg='cyan', fg='black', command=calculate)
equal.grid(column=2, row=4, sticky='nsew')

division = Button(text='/', font=('arial', 20, 'bold'), bg='orange', fg='black', command=lambda : reqem('/'))
division.grid(column=3, row=4, sticky='nsew')

user_input = Label(text='', font=20, bg='white')
user_input.grid(column=0, row=0, columnspan=3, sticky='nsew')

cavab = Label(text='', font=20, bg='gray', fg='black')
cavab.grid(column=3, row=0, sticky='nsew')

root.mainloop()