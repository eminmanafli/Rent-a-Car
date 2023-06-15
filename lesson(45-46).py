'''
from tkinter import *
from tkinter import messagebox


def undo():
    editor.edit_undo()

def redo():
    editor.edit_redo()


def add_command():
    editor.insert('1.2', 'john')

root = Tk()
root.title('Program')
root.geometry('1000x800')

editor = Text(undo=True,wrap ='char')
editor.place(width=200, height=200, x=200, y=200)

scrollbarVertical = Scrollbar(orient='vertical', command=editor.yview)
scrollbarVertical.place(x=400, y=200, height=200)

editor['yscrollcommand'] = scrollbarVertical.set

btn1 = Button(text='Add', command=undo)
btn1.place(x=100, y=100)

btn2 = Button(text='Add', command=redo)
btn2.place(x=300, y=100)

btn3 = Button(text='Add', command=lambda : messagebox.showinfo('!', editor.selection_get()))
btn3.place(x=500, y=100)

root.mainloop()
'''
# task
from tkinter import *


def edit_window():

    def save_func():
        global editor1
        editor1['text'] = editor2.get('1.0', 'end')

    def undo():
        editor2.edit_undo()

    def redo():
        editor2.edit_redo()

    def count(event):
        nonlocal symbol_count
        symbol_count['text'] = len(editor2.get('1.0', END)) - 1
        word_count['text'] = len(editor2.get('1.0', END).split(' '))



    window = Toplevel(root)
    window.title('Edit window')
    window.geometry('700x700')

    editor2 = Text(undo=True, master=window, wrap='char')
    editor2.place(width=700, height=400, x=0, y=0)
    editor2.bind('<KeyRelease>', count)

    save_button = Button(master=window, text='Save', font=20, bg='orange', fg='black', width=10, command=save_func)
    save_button.place(x=0, y=600)

    undo_button = Button(master=window, text='Undo', font=20, bg='orange', fg='black', width=10, command=undo)
    undo_button.place(x=200, y=600)

    redo_button = Button(master=window, text='Redo', font=20, bg='orange', fg='black', width=10, command=redo)
    redo_button.place(x=400, y=600)

    symbol_label = Label(master=window, text='Symbol Count:', font=15)
    symbol_label.place(x=0, y=450)
    word_label = Label(master=window, text='Word Count:', font=15)
    word_label.place(x=0, y=480)
    symbol_count = Label(master=window, font=20)
    symbol_count.place(x=200, y=450)
    word_count = Label(master=window, font=20)
    word_count.place(x=200, y=480)

    window.grab_set()
    window.mainloop()


root = Tk()
root.title('Program')
root.geometry('1000x800')


editor1 = Label(text='', font=15, bg='white')
editor1.place(width=600, height=400, x=100, y=100)

edit = Button(text='Edit', font=20, bg='orange', fg='black', width=15, command=edit_window)
edit.place(x=300, y=550)


root.mainloop()