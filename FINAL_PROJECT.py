# esas pencere
from tkinter import *
from PIL import Image, ImageTk

def masinlar():
    class Masin(BirinciPencere):
        def __init__(self, master, width, height):
            self.master = master
            self.width = width
            self.height = height
            super().__init__(master, width, height)

    masin = Toplevel(root)
    masin.title('Masin penceresi')
    masin.geometry('1000x600')
    masin.iconbitmap('bd7fcfa27c1621914960f9e2fe538f43.ico')

    carWordPhoto = Image.open('wagon-illustration-on-a-background-premium-quality-symbols-icons-for-concept-and-graphic-design-vector.png')
    tk_carWordPhoto = ImageTk.PhotoImage(carWordPhoto)
    carWord = Label(master=masin, image=tk_carWordPhoto,text='Movcud Masinlar', font=('Helvetica', 20, 'bold'), compound='center')
    carWord.place(x=0, y=0)

    car1_photo = resize_image('57030b9026c906ec3c8c0b71.png', 200, 200)
    car1_button = Button(master=masin, image=car1_photo)
    car1_button.place(x=0, y=200)

    car2_photo = resize_image('f066234325ddb399d1ae5a2b.png', 200, 200)
    car2_button = Button(master=masin, image=car2_photo)
    car2_button.place(x=200, y=200)

    car3_photo = resize_image('1000x620xc.png', 200, 200)
    car3_button = Button(master=masin, image=car3_photo)
    car3_button.place(x=400, y=200)

    masin.mainloop()


def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)


class BirinciPencere:

    def __init__(self, master, width, height):
        self.master = master
        self.width = width
        self.height = height

root = Tk()
root.title("Rent a Car")
root.geometry("1000x600")
root.iconbitmap('5320259.ico')


emrler_photo = resize_image('photo-1585503418537-88331351ad99.png', 1000, 200)
emrler_photo1 = Image.open('photo-1585503418537-88331351ad99.png')
tk_emrler_photo = ImageTk.PhotoImage(emrler_photo1)
emrler = Label(master=root,image=tk_emrler_photo,
               text='Movcud xidmetler:\nMüştəri idarəetmə pəncərəsi\nMaşın idarəetmə pəncərəsi\nKirayə vermə və qaytarma',
               compound='center', font=('Helvetica', 30, 'bold'), fg='orange')
emrler.place(x=0, y=0, width=1000, height=200)

masinlar_photo = resize_image('bd7fcfa27c1621914960f9e2fe538f43.png', 500, 400)
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
