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

def masinlar():
    def delete():
        cars.pop(cars_listbox.curselection()[0])  # (0)
        cars_var.set(cars)

    def add():
        my_marka = marka_entry.get()
        my_model = model_entry.get()
        my_il = il_entry.get()
        my_reng = reng_entry.get()
        my_nomre = nomre_entry.get()
        my_car = Car(my_marka, my_model, my_il, my_reng, my_nomre)
        cars.append(my_car)
        cars_var.set(cars)

    def save():
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
    masin.iconbitmap('bd7fcfa27c1621914960f9e2fe538f43.ico')
    masin.maxsize(width=1000, height=600)
    masin.minsize(width=1000, height=600)

    carWordPhoto = Image.open('wagon-illustration-on-a-background-premium-quality-symbols-icons-for-concept-and-graphic-design-vector.png')
    tk_carWordPhoto = ImageTk.PhotoImage(carWordPhoto)
    carWord = Label(master=masin, image=tk_carWordPhoto,text='Movcud Masinlar', font=('Helvetica', 20, 'bold'), compound='center')
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
    delete_button.place(x=400, y=500)

    edit_button = Button(master=masin, text='Edit', bg='cyan', fg='black', font=20, width=10)
    edit_button.place(x=270, y=500)

    save_button = Button(master=masin, text='Save', bg='orange', fg='black', font=20, width=10, command=save)
    save_button.place(x=270, y=455)

    add_button = Button(master=masin, text='Add', bg='green', fg='black', font=20, width=10, command=add)
    add_button.place(x=400, y=455)

    masin.mainloop()


def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)


root = Tk()
root.title("Rent a Car")
root.geometry("1000x600")
root.iconbitmap('5320259.ico')
root.maxsize(width=1000, height=600)
root.minsize(width=1000, height=600)

emrler_photo = resize_image('photo-1585503418537-88331351ad99.png', 1000, 200)
emrler_photo1 = Image.open('photo-1585503418537-88331351ad99.png')
tk_emrler_photo = ImageTk.PhotoImage(emrler_photo1)
emrler = Label(master=root,image=tk_emrler_photo,
               text='Movcud xidmetler:\nMüştəri idarəetmə pəncərəsi\nMaşın idarəetmə pəncərəsi\nKirayə vermə və qaytarma',
               compound='center', font=('Helvetica', 30, 'bold'), fg='orange')
emrler.place(x=0, y=0, width=1000, height=200)

masinlar_photo = resize_image('car1.png', 500, 400)
masinlar_button = Button(master=root, image=masinlar_photo, command=masinlar)
masinlar_button.place(x=0, y=200)
masinlar_label = Label(master=root, text='Maşınlar', font=('Helvetica', 20, 'bold'), fg='black', bg='#e1e1d7')
masinlar_label.place(x=200, y=230)

musteri_photo = resize_image('360_F_196873357_Z8LRgbrFSLloSUP1QEqaVAi3OBbVIaWh.png', 500, 400)
musteri_button = Button(master=root, image=musteri_photo)
musteri_button.place(x=500, y=200)
musteri_label = Label(master=root, text='Müştərilər', font=('Helvetica', 20, 'bold'), fg='black', bg='white')
musteri_label.place(x=650, y=230)

root.mainloop()
