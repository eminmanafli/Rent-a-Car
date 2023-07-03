# esas pencere
from tkinter import *
from PIL import Image, ImageTk
import pickle


class Car:
    def __init__(self, marka, model, buraxilis_ili, reng, qiymet):
        self.marka = marka
        self.model = model
        self.buraxilis_ili = buraxilis_ili
        self.reng = reng
        self.qiymet = qiymet
        self.rented = False
        self.renter = None
        self.muddet = None

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
    global cars

    def find():
        found_cars = list(filter(lambda car: find_cars(car, axtaris_entry, axtaris_filtr[axtaris_listbox.curselection()[0]]), cars))
        cars_var.set(found_cars)

    def reset():
        cars_var.set(cars)
        axtaris_entry.delete(0, END)

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
        qiymet_entry.delete(0, END)
        qiymet_entry.insert(0, data_car.qiymet)

    def apply():
        change_car = cars[cars_listbox.curselection()[0]]
        change_car.marka = marka_entry.get()
        marka_entry.delete(0, END)
        change_car.model = model_entry.get()
        model_entry.delete(0, END)
        change_car.buraxilis_ili = il_entry.get()
        il_entry.delete(0, END)
        change_car.reng = reng_entry.get()
        reng_entry.delete(0, END)
        change_car.qiymet = qiymet_entry.get()
        qiymet_entry.delete(0, END)
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
        my_qiymet = qiymet_entry.get()
        qiymet_entry.delete(0, END)
        my_car = Car(my_marka, my_model, my_il, my_reng, my_qiymet)
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

    qiymet_label = Label(master=masin, text='Qiymet:', font=('Helvetica', 20), fg='black')
    qiymet_label.place(x=260, y=405)
    qiymet_entry = Entry(master=masin, width=15, font=20)
    qiymet_entry.place(x=360, y=415)

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

    axtaris_filtr = ['Marka', 'Model', 'Il', 'Reng', 'Qiymet']
    axtaris_filtr_var = Variable(value=axtaris_filtr)

    axtaris_listbox = Listbox(master=masin, listvariable=axtaris_filtr_var, selectmode=SINGLE, fg='black', bg='white', font=20, selectbackground='blue', selectforeground='white')
    axtaris_listbox.place(x=590, y=250, width=100, height=125)

    axtaris_label = Label(master=masin, text='Axtaris filtrleri:', font=('Helvetica', 20), fg='black')
    axtaris_label.place(x=585, y=202)

    axtaris_entry = Entry(master=masin, width=15, font=20)
    axtaris_entry.place(x=790, y=250)

    axtaris_button = Button(master=masin ,text='Axtar', bg='pink', fg='black', font=20, width=10, command=find)
    axtaris_button.place(x=790, y=300)

    reset_button = Button(master=masin, text='Reset', bg='lime', fg='black', font=20, width=10, command=reset)
    reset_button.place(x=790, y=350)

    masin.mainloop()


def musteriler_func():
    global musteriler

    def find():
        found_people = list(filter(lambda musteri: find_musteriler(musteri, axtaris_entry, axtaris_filtr[axtaris_listbox.curselection()[0]]), musteriler))
        musteriler_var.set(found_people)

    def reset():
        musteriler_var.set(musteriler)
        axtaris_entry.delete(0, END)

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
        ad_entry.delete(0, END)
        change_person.model = soyad_entry.get()
        soyad_entry.delete(0, END)
        change_person.unvan = unvan_entry.get()
        unvan_entry.delete(0, END)
        change_person.telefon_nomresi = telefon_nomresi_entry.get()
        telefon_nomresi_entry.delete(0, END)
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
    musteri.iconbitmap('images/person_icon.ico')
    musteri.maxsize(width=1000, height=600)
    musteri.minsize(width=1000, height=600)

    musteriWordPhoto = Image.open(
        'images/musteri_banner.png')
    tk_musteriWordPhoto = ImageTk.PhotoImage(musteriWordPhoto)
    musteriWord = Label(master=musteri, image=tk_musteriWordPhoto)
    musteriWord.place(x=0, y=0)

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

    axtaris_filtr = ['Ad', 'Soyad', 'Unvan', 'Telefon']
    axtaris_filtr_var = Variable(value=axtaris_filtr)

    axtaris_listbox = Listbox(master=musteri, listvariable=axtaris_filtr_var, selectmode=SINGLE, fg='black', bg='white',
                              font=20, selectbackground='blue', selectforeground='white')
    axtaris_listbox.place(x=590, y=250, width=100, height=100)

    axtaris_label = Label(master=musteri, text='Axtaris filtrleri:', font=('Helvetica', 20), fg='black')
    axtaris_label.place(x=585, y=202)

    axtaris_entry = Entry(master=musteri, width=15, font=20)
    axtaris_entry.place(x=790, y=250)

    axtaris_button = Button(master=musteri, text='Axtar', bg='pink', fg='black', font=20, width=10, command=find)
    axtaris_button.place(x=790, y=300)

    reset_button = Button(master=musteri, text='Reset', bg='lime', fg='black', font=20, width=10, command=reset)
    reset_button.place(x=790, y=350)

    musteri.mainloop()


def kiraye():
    global musteriler
    global cars
    global rent_list
    current_person = None
    current_car = None

    def rent(car, person):
        selection2 = muddet_secim.curselection()
        if selection2:
            if not car.rented:
                car.rented = True
                car.renter = person.ad
                car.muddet = muddet_list[muddet_secim.curselection()[0]]
                rent_label['text'] = 'Ugurla\nkiralandi'
                rent_label.config(fg='green')
                rent_list.append(car)
            else:
                rent_label['text'] = 'Masin\nartiq\nkiralanib'
                rent_label.config(fg='red')
        else:
            rent_label['text'] = 'Muddet secin'
            rent_label.config(fg='red')

    def save():
        try:
            file = open('RentFile.txt', 'wb')
            try:
                pickle.dump(rent_list, file)
            except Exception as e:
                print(e)
            finally:
                file.close()
        except Exception as ex:
            print(ex)
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

    def qiymet(event):
        nonlocal current_car
        selection = muddet_secim.curselection()
        if selection:
            price = current_car.qiymet
            muddet = muddet_list[selection[0]]
            if muddet == '1 gun':
                qiymet_label4['text'] = str(int(price) * 1)
            elif muddet == '10 gun':
                qiymet_label4['text'] = str(int(price) * 10)
            elif muddet == '1 hefte':
                qiymet_label4['text'] = str(int(price) * 7)
            elif muddet == '2 hefte':
                qiymet_label4['text'] = str(int(price) * 14)
            elif muddet == '1 ay':
                qiymet_label4['text'] = str(int(price) * 30)

    def musteri_show_info(event):
        nonlocal current_person
        selection = musteri_secim.curselection()
        if selection:
            info_person = musteriler[selection[0]]
            current_person = info_person
            ad_label2['text'] = current_person.ad
            soyad_label2['text'] = current_person.soyad
            unvan_label2['text'] = current_person.unvan
            telefon_label2['text'] = current_person.telefon_nomresi

    def masin_show_info(event):
        nonlocal current_car
        selection = masin_secim.curselection()
        if selection:
            info_car = cars[selection[0]]
            current_car = info_car
            marka_label2['text'] = current_car.marka
            model_label2['text'] = current_car.model
            il_label2['text'] = current_car.buraxilis_ili
            reng_label2['text'] = current_car.reng
            qiymet_label2['text'] = current_car.qiymet

    kiraye_window = Toplevel(root)
    kiraye_window.title('Kiraye alib_verme')
    kiraye_window.geometry('1000x600')
    kiraye_window.iconbitmap('images/rent1.ico')
    kiraye_window.maxsize(width=1000, height=600)
    kiraye_window.minsize(width=1000, height=600)

    kiraye_image = resize_image('images/rent4.png', 1000, 200)
    kiraye_label = Label(master=kiraye_window, image=kiraye_image)
    kiraye_label.place(x=0, y=0)

    musteriler2_var = Variable(value=musteriler)
    musteri_secim = Listbox(master=kiraye_window, listvariable=musteriler2_var, selectmode=SINGLE, fg='black', bg='white',
                              font=20, selectbackground='blue', selectforeground='white')
    musteri_secim.place(x=0, y=250, width=200, height=150)
    musteri_secim_scrollbar = Scrollbar(master=kiraye_window, highlightbackground='gray', highlightcolor='black', bg='gray',
                              activebackground='black', orient='vertical', command=musteri_secim.yview)
    musteri_secim_scrollbar.place(x=200, y=250, height=150)
    musteri_secim['yscrollcommand'] = musteri_secim_scrollbar.set
    musteri_secim_label = Label(master=kiraye_window, text='Musteri secin:', font=('Helvetica', 20, 'bold'), fg='black')
    musteri_secim_label.place(x=0, y=205)
    musteri_secim.bind("<<ListboxSelect>>", musteri_show_info)

    masinlar2_var = Variable(value=cars)
    masin_secim = Listbox(master=kiraye_window, listvariable=masinlar2_var, selectmode=SINGLE, fg='black',
                            bg='white',
                            font=20, selectbackground='blue', selectforeground='white')
    masin_secim.place(x=300, y=250, width=200, height=150)
    masin_secim_scrollbar = Scrollbar(master=kiraye_window, highlightbackground='gray', highlightcolor='black',
                                        bg='gray',
                                        activebackground='black', orient='vertical', command=masin_secim.yview)
    masin_secim_scrollbar.place(x=500, y=250, height=150)
    masin_secim['yscrollcommand'] = masin_secim_scrollbar.set
    masin_secim_label = Label(master=kiraye_window, text='Masin secin:', font=('Helvetica', 20, 'bold'), fg='black')
    masin_secim_label.place(x=300, y=205)
    masin_secim.bind("<<ListboxSelect>>", masin_show_info)

    muddet_list = ['1 gun', '10 gun', '1 hefte', '2 hefte', '1 ay']
    muddet_var = Variable(value=muddet_list)
    muddet_secim = Listbox(master=kiraye_window, listvariable=muddet_var, selectmode=SINGLE, fg='black', bg='white',
                              font=20, selectbackground='blue', selectforeground='white')
    muddet_secim.place(x=600, y=250, width=200, height=150)
    muddet_secim_scrollbar = Scrollbar(master=kiraye_window, highlightbackground='gray', highlightcolor='black',
                                        bg='gray',
                                        activebackground='black', orient='vertical', command=muddet_secim.yview)
    muddet_secim_scrollbar.place(x=800, y=250, height=150)
    muddet_secim['yscrollcommand'] = muddet_secim_scrollbar.set
    muddet_secim_label = Label(master=kiraye_window, text='Muddet secin:', font=('Helvetica', 20, 'bold'), fg='black')
    muddet_secim_label.place(x=600, y=205)
    muddet_secim.bind("<<ListboxSelect>>", qiymet)

    ad_label = Label(master=kiraye_window, text='Ad:', font=('Helvetica', 20), fg='green')
    ad_label.place(x=0, y=400)
    ad_label2 = Label(master=kiraye_window, text='', font=('Helvetica', 20), fg='black')
    ad_label2.place(x=100, y=400)

    soyad_label = Label(master=kiraye_window, text='Soyad:', font=('Helvetica', 20), fg='green')
    soyad_label.place(x=0, y=450)
    soyad_label2 = Label(master=kiraye_window, text='', font=('Helvetica', 20), fg='black')
    soyad_label2.place(x=100, y=450)

    unvan_label = Label(master=kiraye_window, text='Unvan:', font=('Helvetica', 20), fg='green')
    unvan_label.place(x=0, y=500)
    unvan_label2 = Label(master=kiraye_window, text='', font=('Helvetica', 20), fg='black')
    unvan_label2.place(x=100, y=500)

    telefon_label = Label(master=kiraye_window, text='Telefon:', font=('Helvetica', 20), fg='green')
    telefon_label.place(x=0, y=550)
    telefon_label2 = Label(master=kiraye_window, text='', font=('Helvetica', 20), fg='black')
    telefon_label2.place(x=100, y=550)

    marka_label = Label(master=kiraye_window, text='Marka:', font=('Helvetica', 20), fg='green')
    marka_label.place(x=300, y=400)
    marka_label2 = Label(master=kiraye_window, text='', font=('Helvetica', 20), fg='black')
    marka_label2.place(x=400, y=400)

    model_label = Label(master=kiraye_window, text='Model:', font=('Helvetica', 20), fg='green')
    model_label.place(x=300, y=435)
    model_label2 = Label(master=kiraye_window, text='', font=('Helvetica', 20), fg='black')
    model_label2.place(x=400, y=435)

    il_label = Label(master=kiraye_window, text='Il:', font=('Helvetica', 20), fg='green')
    il_label.place(x=300, y=470)
    il_label2 = Label(master=kiraye_window, text='', font=('Helvetica', 20), fg='black')
    il_label2.place(x=400, y=470)

    reng_label = Label(master=kiraye_window, text='Reng:', font=('Helvetica', 20), fg='green')
    reng_label.place(x=300, y=505)
    reng_label2 = Label(master=kiraye_window, text='', font=('Helvetica', 20), fg='black')
    reng_label2.place(x=400, y=505)

    qiymet_label = Label(master=kiraye_window, text='Qiymet:', font=('Helvetica', 20), fg='green')
    qiymet_label.place(x=300, y=540)
    qiymet_label2 = Label(master=kiraye_window, text='', font=('Helvetica', 20), fg='black')
    qiymet_label2.place(x=400, y=540)

    qiymet_label3 = Label(master=kiraye_window, text='Umumi qiymet:', font=('Helvetica', 20, 'bold'), fg='dark red')
    qiymet_label3.place(x=600, y=400)
    qiymet_label4 = Label(master=kiraye_window, text='', font=('Helvetica', 20), fg='blue')
    qiymet_label4.place(x=810, y=400)

    rent_button = Button(master=kiraye_window, text='Rent', font=20, bg='tan', fg='black', command=lambda: rent(current_car, current_person))
    rent_button.place(x=600, y=450, width=200)
    rent_label = Label(master=kiraye_window, text='', font=('Helvetica', 20))
    rent_label.place(x=800, y=450)

    save_button = Button(master=kiraye_window, text='Save', font=20, bg='pink', fg='black', command=save)
    save_button.place(x=600, y=500, width=200)

    kiraye_window.mainloop()


def hesabat():
    global rent_list
    global cars

    def show_info(event):
        selection = hesabat_masin.curselection()[0]
        if cars[selection].rented:
            available_entry.delete(0, END)
            available_entry.insert(0, 'Movcud deyil!')
            renter_entry.delete(0, END)
            renter_entry.insert(0, cars[selection].renter)
            time_entry.delete(0, END)
            time_entry.insert(0, cars[selection].muddet)
        else:
            available_entry.delete(0, END)
            available_entry.insert(0, 'Movcuddur')
            renter_entry.delete(0, END)
            renter_entry.insert(0, '-')
            time_entry.delete(0, END)
            time_entry.insert(0, '-')

    hesabat_window = Toplevel(root)
    hesabat_window.title('Hesabat penceresi')
    hesabat_window.geometry('1000x600')
    hesabat_window.iconbitmap('images/report_icon.ico')
    hesabat_window.maxsize(width=1000, height=600)
    hesabat_window.minsize(width=1000, height=600)

    image1 = Image.open('images/hesabat_bg.png')
    tk_image1 = ImageTk.PhotoImage(image1)
    window_label = Label(master=hesabat_window, image=tk_image1)
    window_label.place(x=0, y=0, width=1000, height=600)

    hesabat_masin_list_var = Variable(value=cars)
    hesabat_masin = Listbox(master=hesabat_window, listvariable=hesabat_masin_list_var, selectmode=SINGLE, fg='black',
                          bg='cyan',
                          font=20, selectbackground='blue', selectforeground='white')
    hesabat_masin.place(x=50, y=50, width=250, height=400)
    hesabat_masin.bind("<<ListboxSelect>>", show_info)

    available_label = Label(master=hesabat_window, text='Movcud:', font=('Helvetica', 20, 'bold'), bg='cyan', fg='black')
    available_label.place(x=350, y=100)
    available_entry = Entry(master=hesabat_window, width=50, font=20)
    available_entry.place(x=500, y=100)

    renter_label = Label(master=hesabat_window, text='Renter:', font=('Helvetica', 20, 'bold'), bg='cyan', fg='black')
    renter_label.place(x=350, y=200)
    renter_entry = Entry(master=hesabat_window, width=50, font=20)
    renter_entry.place(x=500, y=200)

    time_label = Label(master=hesabat_window, text='Muddet:', font=('Helvetica', 20, 'bold'), bg='cyan', fg='black')
    time_label.place(x=350, y=300)
    time_entry = Entry(master=hesabat_window, width=50, font=20)
    time_entry.place(x=500, y=300)

    hesabat_window.mainloop()


def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)


def find_cars(car, entry, selection):
    if selection == 'Marka':
        if entry.get() in car.marka:
            return car
    elif selection == 'Model':
        if entry.get() in car.model:
            return car
    elif selection == 'Il':
        if entry.get() in car.buraxilis_ili:
            return car
    elif selection == 'Reng':
        if entry.get() in car.reng:
            return car
    elif selection == 'Qiymet':
        if entry.get() in car.qiymet:
            return car


def find_musteriler(musteri, entry, selection):
    if selection == 'Ad':
        if entry.get() in musteri.ad:
            return musteri
    elif selection == 'Soyad':
        if entry.get() in musteri.soyad:
            return musteri
    elif selection == 'Unvan':
        if entry.get() in musteri.unvan:
            return musteri
    elif selection == 'Telefon':
        if entry.get() in musteri.telefon_nomresi:
            return musteri


cars = []
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

musteriler = []
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

rent_list = []
try:
    file = open('RentFile.txt', 'rb')
    try:
        rent_list = pickle.load(file)
    except Exception as e:
        print(e)
    finally:
        file.close()
except Exception as ex:
    print(ex)


root = Tk()
root.title("Rent a Car")
root.geometry("1000x600")
root.iconbitmap('images/masin_icon.ico')
root.maxsize(width=1000, height=600)
root.minsize(width=1000, height=600)

emrler_photo = resize_image('images/pencere1_banner.png', 600, 200)
emrler_photo1 = Image.open('images/pencere1_banner.png')
tk_emrler_photo = ImageTk.PhotoImage(emrler_photo1)
emrler = Label(master=root, image=tk_emrler_photo,
               text='RENT A CAR',
               compound='center', font=('Courier New', 50, 'bold'), fg='red')
emrler.place(x=0, y=0, width=600, height=200)

masinlar_photo = resize_image('images/car1.png', 350, 400)
masinlar_button = Button(master=root, image=masinlar_photo, command=masinlar)
masinlar_button.place(x=0, y=200)
masinlar_label = Label(master=root, text='Maşınlar', font=('Helvetica', 20, 'bold'), fg='black', bg='#e1e1d7')
masinlar_label.place(x=125, y=230)

musteri_photo = resize_image('images/musteri_pencere.png', 350, 400)
musteri_button = Button(master=root, image=musteri_photo, command=musteriler_func)
musteri_button.place(x=350, y=200)
musteri_label = Label(master=root, text='Müştərilər', font=('Helvetica', 20, 'bold'), fg='black', bg='white')
musteri_label.place(x=450, y=230)

kiraye_photo = resize_image('images/rent.png', 300, 400)
kiraye_button = Button(master=root, image=kiraye_photo, command=kiraye)
kiraye_button.place(x=700, y=200)
kiraye_label = Label(master=root, text='Kiraye\nalib-verme', font=('Helvetica', 20, 'bold'), fg='black', bg='#008B8B')
kiraye_label.place(x=705, y=205)

hesabat_photo = resize_image('images/hesabat.png', 400, 200)
hesabat_button = Button(master=root, image=hesabat_photo, command=hesabat)
hesabat_button.place(x=600, y=0, width=400, height=200)
hesabat_label = Label(master=root, text='Hesabat', font=('Helvetica', 20, 'bold'), fg='black', bg='white')
hesabat_label.place(x=880, y=5)

root.mainloop()
