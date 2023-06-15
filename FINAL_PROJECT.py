# esas pencere
from tkinter import *
from PIL import Image, ImageTk


def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)


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

masinlar_photo = resize_image('bd7fcfa27c1621914960f9e2fe538f43.png', 300, 400)
masinlar_button = Button(master=root, image=masinlar_photo)
masinlar_button.place(x=0, y=200 ,width=300, height=400)
masinlar_label = Label(master=root, text='Masinlar', font=('Arial', 20), fg='black')
masinlar_label.place(x=50, y=550)

musteri_photo =




root.mainloop()