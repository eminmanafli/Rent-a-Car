'''
# w - write
# a- append
# r - read
# b -



# read() -> boyuk string qaytarir
with open('hello.txt', 'r') as somefile:
    text = somefile.read()
    print(text)

# readlines() -> her bir setir listin elementi olur
# readlin() -> her defe cagiranda gelen setri oxuyur

# .txt
# .dat

import pickle

a = 5

# wb
# rb
# .write() -> pickle.dump()
# .read() -> pickle.load()
with open('hello.txt', 'wb') as file:
    pickle.dump(a, file)

with open('hello.txt', 'rb') as file:
    result = pickle.load(file)
    print(result)
'''
from tkinter import *
import pickle

def add():
    my_ad = ad1.get()
    my_soyad = soyad1.get()
    my_age = age1.get()
    my_job = job1.get()
    my_person = Person(my_ad, my_soyad, my_age, my_job)
    people.append(my_person)
    people_var.set(people)

    print("~~~~~~~~~~~")
    print(people)
    for i in people:
        print(i)
    print("~~~~~~~~~~~")

def delete():
    people.pop(languages_listbox.curselection()[0]) # (0)
    people_var.set(people)
    print("+++++++++")
    print(people)
    for i in people:
        print(i)
    print("+++++++++")

def save():
    try:
        file = open('file1.txt', 'wb')
        try:
            pickle.dump(people, file)
        except Exception as e:
            print(e)
        finally:
            file.close()
    except Exception as ex:
        print(ex)


class Person:

    def __init__(self, name, surname, age, job):
        self.name = name
        self.surname = surname
        self.age = age
        self.job = job

    def __str__(self):
        return f'{self.name} {self.surname} {self.age} {self.job}'


root = Tk()
root.title("METANIT.COM")
root.geometry("1000x500")


people = []
try:
    file = open('file1.txt', 'rb')
    try:
        people = pickle.load(file)
    except Exception as e:
        print(e)
    finally:
        file.close()
except Exception as ex:
    print(ex)
people_var = Variable(value=people)


languages_listbox = Listbox(selectmode= SINGLE,listvariable=people_var, fg="red", highlightcolor="green", font=20, highlightthickness=10, selectbackground="blue",selectforeground="yellow")
languages_listbox.place(width=400, height=300, x=20)

ad1 = Entry(master=root, bg="pink", fg='black', font=25)
ad1.place(x=500, y=20)

soyad1 = Entry(master=root, bg="pink", fg='black', font=25)
soyad1.place(x=500, y=60)

age1 = Entry(master=root, bg="pink", fg='black', font=25)
age1.place(x=500, y=100)

job1 = Entry(master=root, bg="pink", fg='black', font=25)
job1.place(x=500, y=140)

ad2 = Label(master=root, text='Name', bg="pink", fg='black', font=10)
ad2.place(x=750, y=20)

soyad2 = Label(master=root, text='Surname', bg="pink", fg='black', font=10)
soyad2.place(x=750, y=60)

age2 = Label(master=root, text='Age', bg="pink", fg='black', font=10)
age2.place(x=750, y=100)

job2 = Label(master=root, text='Job', bg="pink", fg='black', font=10)
job2.place(x=750, y=140)

delete = Button(master=root, text="Delete", bg='red', fg='black', font=13, command=delete)
delete.place(x=30, y=310, width=80, height=40)

add = Button(master=root, text="Add", bg='red', fg='black', font=13, command=add)
add.place(x=500, y=200, width=80, height=40)

save_button = Button(master=root, text="Save", bg='red', fg='black', font=13, command=save)
save_button.place(x=130, y=310, width=80, height=40)

root.mainloop()