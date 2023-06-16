# esas pencere
from tkinter import *
from PIL import Image, ImageTk


def masinlar():
    masin = Toplevel(root)
    masin.title('Masin penceresi')
    masin.geometry('1000x600')
    masin.iconbitmap('bd7fcfa27c1621914960f9e2fe538f43.ico')

    carWordPhoto = Image.open('wagon-illustration-on-a-background-premium-quality-symbols-icons-for-concept-and-graphic-design-vector.png')
    tk_carWordPhoto = ImageTk.PhotoImage(carWordPhoto)
    carWord = Label(master=masin, image=tk_carWordPhoto,text='Movcud Masinlar', font=('Helvetica', 20, 'bold'), compound='center')
    carWord.place(x=0, y=0)

    cars = ['Camaro', 'Mercedes', 'Camaro', 'Camaro', 'Camaro', 'Camaro', 'Camaro', 'Camaro', 'Camaro', 'Camaro', 'Camaro', 'Camaro', 'Camaro', 'Camaro', 'Camaro', 'Camaro', 'Camaro', 'Camaro', 'Camaro', 'Camaro']
    cars_var = StringVar(value=cars)
    cars_listbox = Listbox(master=masin, listvariable=cars_var, selectmode=SINGLE, fg='black', bg='white', font=20, selectbackground='blue', selectforeground='white')
    cars_listbox.place(x=0, y=200, width=250, height=400)
    car_scrollbar = Scrollbar(bg='gray', activebackground='black', orient='vertical', command=cars_listbox.yview)
    car_scrollbar.place(x=250, y=200)
    cars_listbox['yscrollcommand'] = car_scrollbar.set


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
masinlar_label = Label(master=root, text='Maşınlar', font=('Helvetica', 20, 'bold'), fg='white', bg='black')
masinlar_label.place(x=200, y=230)

musteri_photo = resize_image('360_F_196873357_Z8LRgbrFSLloSUP1QEqaVAi3OBbVIaWh.png', 500, 400)
musteri_button = Button(master=root, image=musteri_photo)
musteri_button.place(x=500, y=200)
musteri_label = Label(master=root, text='Müştərilər', font=('Helvetica', 20, 'bold'), fg='black', bg='white')
musteri_label.place(x=650, y=230)

root.mainloop()
