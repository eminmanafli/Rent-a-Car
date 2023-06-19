# esas pencere
from tkinter import *
from PIL import Image, ImageTk
import pickle


class Car:
    def __init__(self, marka, model, buraxilis_ili, reng, nomre):
        self.marka = marka
        self.model = model
        self.buraxilis_ili = buraxilis_ili
        self.reng = reng
        self.nomre = nomre

    def __str__(self):
        return f'{self.marka} {self.model}'


class Musteri:
    def __init__(self, ad, soyad, unvan, telefon_nomresi):
        self.ad = ad
        self.soyad = soyad
        self.unvan = unvan
        self.telefon_nomresi = telefon_nomresi

    def __str__(self):
        return f'{self.ad} {self.soyad}'


def masinlar():
    def find():
        if axtaris_listbox.curselection()[0] == 'Marka':
            cars.filter(marka=axtaris_entry.get())
            cars_var.set(cars)

    def edit():
        data_car = cars[cars_listbox.curselection()[0]]
        marka_entry.delete(0, END)
        marka_entry.insert(0, data_car.marka)
        model_entry.delete(0, END)
        model_entry.insert(0, data_car.model)
        il_entry.delete(0, END)
        il_entry.insert(0, data_car.buraxilis_ili)
        reng_entry.delete(0, END)
        reng_entry.insert(0, data_car.reng)
        nomre_entry.delete(0, END)
        nomre_entry.insert(0, data_car.nomre)

    def apply():
        change_car = cars[cars_listbox.curselection()[0]]
        change_car.marka = marka_entry.get()
        change_car.model = model_entry.get()
        change_car.buraxilis_ili = il_entry.get()
        change_car.reng = reng_entry.get()
        change_car.nomre = nomre_entry.get()
        cars_var.set(cars)

    def delete():
        cars.pop(cars_listbox.curselection()[0])  # (0)
        cars_var.set(cars)

    def add():
        my_marka = marka_entry.get()
        marka_entry.delete(0, END)
        my_model = model_entry.get()
        model_entry.delete(0, END)
        my_il = il_entry.get()
        il_entry.delete(0, END)
        my_reng = reng_entry.get()
        reng_entry.delete(0, END)
        my_nomre = nomre_entry.get()
        nomre_entry.delete(0, END)
        my_car = Car(my_marka, my_model, my_il, my_reng, my_nomre)
        cars.append(my_car)
        cars_var.set(cars)

    def save1():
        try:
            file = open('CarFile.txt', 'wb')
            try:
                pickle.dump(cars, file)
            except Exception as e:
                print(e)
            finally:
                file.close()
        except Exception as ex:
            print(ex)

    masin = Toplevel(root)
    masin.title('Masin penceresi')
    masin.geometry('1000x600')
    masin.iconbitmap('images/car2_icon.ico')
    masin.maxsize(width=1000, height=600)
    masin.minsize(width=1000, height=600)

    carWordPhoto = Image.open('images/car_banner.png')
    tk_carWordPhoto = ImageTk.PhotoImage(carWordPhoto)
    carWord = Label(master=masin, image=tk_carWordPhoto)
    carWord.place(x=0, y=0)

    car1 = Car('Chevrolet', 'Camaro', 2021, 'qara', '99SU236')
    cars = [car1]
    try:
        file = open('CarFile.txt', 'rb')
        try:
            cars = pickle.load(file)
        except Exception as e:
            print(e)
        finally:
            file.close()
    except Exception as ex:
        print(ex)
    cars_var = Variable(value=cars)

    cars_listbox = Listbox(master=masin, listvariable=cars_var, selectmode=SINGLE, fg='black', bg='white', font=20, selectbackground='blue', selectforeground='white')
    cars_listbox.place(x=0, y=200, width=250, height=400)
    car_scrollbar = Scrollbar(master=masin, highlightbackground='gray', highlightcolor='black', bg='gray', activebackground='black', orient='vertical', command=cars_listbox.yview)
    car_scrollbar.place(x=250, y=200, height=400)
    cars_listbox['yscrollcommand'] = car_scrollbar.set

    marka_label = Label(master=masin, text='Marka:', font=('Helvetica', 20), fg='black')
    marka_label.place(x=270, y=205)
    marka_entry = Entry(master=masin, width=15, font=20)
    marka_entry.place(x=360, y=215)

    model_label = Label(master=masin, text='Model:', font=('Helvetica', 20), fg='black')
    model_label.place(x=270, y=255)
    model_entry = Entry(master=masin, width=15, font=20)
    model_entry.place(x=360, y=265)

    il_label = Label(master=masin, text='Ili:', font=('Helvetica', 20), fg='black')
    il_label.place(x=270, y=305)
    il_entry = Entry(master=masin, width=15, font=20)
    il_entry.place(x=360, y=315)

    reng_label = Label(master=masin, text='Reng:', font=('Helvetica', 20), fg='black')
    reng_label.place(x=270, y=355)
    reng_entry = Entry(master=masin, width=15, font=20)
    reng_entry.place(x=360, y=365)

    nomre_label = Label(master=masin, text='Nomre:', font=('Helvetica', 20), fg='black')
    nomre_label.place(x=270, y=405)
    nomre_entry = Entry(master=masin, width=15, font=20)
    nomre_entry.place(x=360, y=415)

    delete_button = Button(master=masin, text='Delete', bg='red', fg='white', font=20, width=10, command=delete)
    delete_button.place(x=400, y=455)

    edit_button = Button(master=masin, text='Edit', bg='cyan', fg='black', font=20, width=10, command=edit)
    edit_button.place(x=270, y=500)

    save_button = Button(master=masin, text='Save', bg='orange', fg='black', font=20, width=20, command=save1)
    save_button.place(x=270, y=550)

    add_button = Button(master=masin, text='Add', bg='green', fg='black', font=20, width=10, command=add)
    add_button.place(x=270, y=455)

    apply_button = Button(master=masin, text='Apply', bg='purple', fg='white', font=20, width=10, command=apply)
    apply_button.place(x=400, y=500)

    marka_filtr = 'Marka'
    model_filtr = 'Model'
    il_filtr = 'Il'
    reng_filtr = 'Reng'
    nomre_filtr = 'Nomre'
    axtaris_filtr = [marka_filtr, model_filtr, il_filtr, reng_filtr, nomre_filtr]
    axtaris_filtr_var = Variable(value=axtaris_filtr)

    axtaris_listbox = Listbox(master=masin, listvariable=axtaris_filtr_var, selectmode=SINGLE, fg='black', bg='white', font=20, selectbackground='blue', selectforeground='white')
    axtaris_listbox.place(x=590, y=250, width=100, height=125)

    axtaris_label = Label(master=masin, text='Axtaris filtrleri:', font=('Helvetica', 20), fg='black')
    axtaris_label.place(x=585, y=202)

    axtaris_entry = Entry(master=masin, width=15, font=20)
    axtaris_entry.place(x=790, y=250)

    axtaris_button = Button(master=masin ,text='Axtar', bg='pink', fg='black', font=20, width=10, command=find)
    axtaris_button.place(x=790, y=300)

    reset_button = Button(master=masin, text='Reset', bg='lime', fg='black', font=20, width=10)
    reset_button.place(x=790, y=350)

    masin.mainloop()


def musteriler():
    def edit():
        data_car = musteriler[musteriler_listbox.curselection()[0]]
        ad_entry.delete(0, END)
        ad_entry.insert(0, data_car.ad)
        soyad_entry.delete(0, END)
        soyad_entry.insert(0, data_car.soyad)
        unvan_entry.delete(0, END)
        unvan_entry.insert(0, data_car.unvan)
        telefon_nomresi_entry.delete(0, END)
        telefon_nomresi_entry.insert(0, data_car.telefon_nomresi)

    def apply():
        change_person = musteriler[musteriler_listbox.curselection()[0]]
        change_person.ad = ad_entry.get()
        change_person.model = soyad_entry.get()
        change_person.unvan = unvan_entry.get()
        change_person.telefon_nomresi = telefon_nomresi_entry.get()
        musteriler_var.set(musteriler)

    def delete():
        musteriler.pop(musteriler_listbox.curselection()[0])  # (0)
        musteriler_var.set(musteriler)

    def add():
        my_ad = ad_entry.get()
        ad_entry.delete(0, END)
        my_soyad = soyad_entry.get()
        soyad_entry.delete(0, END)
        my_unvan = unvan_entry.get()
        unvan_entry.delete(0, END)
        my_telefon = telefon_nomresi_entry.get()
        telefon_nomresi_entry.delete(0, END)
        my_musteri = Musteri(my_ad, my_soyad, my_unvan, my_telefon)
        musteriler.append(my_musteri)
        musteriler_var.set(musteriler)

    def save1():
        try:
            file = open('MusteriFile.txt', 'wb')
            try:
                pickle.dump(musteriler, file)
            except Exception as e:
                print(e)
            finally:
                file.close()
        except Exception as ex:
            print(ex)

    musteri = Toplevel(root)
    musteri.title('Musteri penceresi')
    musteri.geometry('1000x600')
    musteri.iconbitmap('images/car2_icon.ico')
    musteri.maxsize(width=1000, height=600)
    musteri.minsize(width=1000, height=600)

    musteriWordPhoto = Image.open(
        'images/musteri_banner.png')
    tk_musteriWordPhoto = ImageTk.PhotoImage(musteriWordPhoto)
    musteriWord = Label(master=musteri, image=tk_musteriWordPhoto)
    musteriWord.place(x=0, y=0)

    musteri1 = Musteri('Peter', 'Parker', 'USA', 1234567890)
    musteriler = [musteri1]
    try:
        file = open('MusteriFile.txt', 'rb')
        try:
            musteriler = pickle.load(file)
        except Exception as e:
            print(e)
        finally:
            file.close()
    except Exception as ex:
        print(ex)
    musteriler_var = Variable(value=musteriler)

    musteriler_listbox = Listbox(master=musteri, listvariable=musteriler_var, selectmode=SINGLE, fg='black', bg='white', font=20,
                           selectbackground='blue', selectforeground='white')
    musteriler_listbox.place(x=0, y=200, width=250, height=400)
    musteriler_scrollbar = Scrollbar(master=musteri, highlightbackground='gray', highlightcolor='black', bg='gray',
                              activebackground='black', orient='vertical', command=musteriler_listbox.yview)
    musteriler_scrollbar.place(x=250, y=200, height=400)
    musteriler_listbox['yscrollcommand'] = musteriler_scrollbar.set

    ad_label = Label(master=musteri, text='Ad:', font=('Helvetica', 20), fg='black')
    ad_label.place(x=270, y=205)
    ad_entry = Entry(master=musteri, width=15, font=20)
    ad_entry.place(x=370, y=215)

    soyad_label = Label(master=musteri, text='Soyad:', font=('Helvetica', 20), fg='black')
    soyad_label.place(x=270, y=255)
    soyad_entry = Entry(master=musteri, width=15, font=20)
    soyad_entry.place(x=370, y=265)

    unvan_label = Label(master=musteri, text='Unvan:', font=('Helvetica', 20), fg='black')
    unvan_label.place(x=270, y=305)
    unvan_entry = Entry(master=musteri, width=15, font=20)
    unvan_entry.place(x=370, y=315)

    telefon_nomresi_label = Label(master=musteri, text='Telefon:', font=('Helvetica', 20), fg='black')
    telefon_nomresi_label.place(x=270, y=355)
    telefon_nomresi_entry = Entry(master=musteri, width=15, font=20)
    telefon_nomresi_entry.place(x=370, y=365)

    delete_button = Button(master=musteri, text='Delete', bg='red', fg='white', font=20, width=10, command=delete)
    delete_button.place(x=400, y=455)

    edit_button = Button(master=musteri, text='Edit', bg='cyan', fg='black', font=20, width=10, command=edit)
    edit_button.place(x=270, y=500)

    save_button = Button(master=musteri, text='Save', bg='orange', fg='black', font=20, width=20, command=save1)
    save_button.place(x=270, y=550)

    add_button = Button(master=musteri, text='Add', bg='green', fg='black', font=20, width=10, command=add)
    add_button.place(x=270, y=455)

    apply_button = Button(master=musteri, text='Apply', bg='purple', fg='white', font=20, width=10, command=apply)
    apply_button.place(x=400, y=500)

    musteri.mainloop()


def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)


root = Tk()
root.title("Rent a Car")
root.geometry("1000x600")
root.iconbitmap('images/masin_icon.ico')
root.maxsize(width=1000, height=600)
root.minsize(width=1000, height=600)

emrler_photo = resize_image('images/pencere1_banner.png', 1000, 200)
emrler_photo1 = Image.open('images/pencere1_banner.png')
tk_emrler_photo = ImageTk.PhotoImage(emrler_photo1)
emrler = Label(master=root, image=tk_emrler_photo,
               text='Movcud xidmetler:\nMüştəri idarəetmə pəncərəsi\nMaşın idarəetmə pəncərəsi\nKirayə vermə və qaytarma',
               compound='center', font=('Helvetica', 30, 'bold'), fg='orange')
emrler.place(x=0, y=0, width=1000, height=200)

masinlar_photo = resize_image('images/car1.png', 500, 400)
masinlar_button = Button(master=root, image=masinlar_photo, command=masinlar)
masinlar_button.place(x=0, y=200)
masinlar_label = Label(master=root, text='Maşınlar', font=('Helvetica', 20, 'bold'), fg='black', bg='#e1e1d7')
masinlar_label.place(x=200, y=230)

musteri_photo = resize_image('images/musteri_pencere.png', 500, 400)
musteri_button = Button(master=root, image=musteri_photo, command=musteriler)
musteri_button.place(x=500, y=200)
musteri_label = Label(master=root, text='Müştərilər', font=('Helvetica', 20, 'bold'), fg='black', bg='white')
musteri_label.place(x=680, y=230)

root.mainloop()
