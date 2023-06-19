def edit():
    nonlocal cars

    def save():
        index_data = cars.index(data_car)
        cars.remove(data_car)
        marka2 = marka_entry.get()
        model2 = model_entry.get()
        il2 = il_entry.get()
        reng2 = reng_entry.get()
        nomre2 = nomre_entry.get()
        new_car = [marka2, model2, il2, reng2, nomre2]
        cars.insert(index_data, new_car)
        cars_var.set(cars)
        root2.destroy()

    root2 = Toplevel(masin)
    root2.title('Edit window')
    root2.geometry('1000x600')
    root2.iconbitmap('car2_icon.ico')
    root2.maxsize(width=1000, height=600)
    root2.minsize(width=1000, height=600)

    data_car = [i for i in cars_listbox.get(cars_listbox.curselection())]

    marka_label2 = Label(master=root2, text='Marka:', font=('Helvetica', 20), fg='black')
    marka_label2.place(x=270, y=205)
    marka_entry2 = Entry(master=root2, width=15, font=20)
    marka_entry2.place(x=360, y=215)
    marka_entry2.insert(0, data_car[0])

    model_label2 = Label(master=root2, text='Model:', font=('Helvetica', 20), fg='black')
    model_label2.place(x=270, y=255)
    model_entry2 = Entry(master=root2, width=15, font=20)
    model_entry2.place(x=360, y=265)

    il_label2 = Label(master=root2, text='Ili:', font=('Helvetica', 20), fg='black')
    il_label2.place(x=270, y=305)
    il_entry2 = Entry(master=root2, width=15, font=20)
    il_entry2.place(x=360, y=315)

    reng_label2 = Label(master=root2, text='Reng:', font=('Helvetica', 20), fg='black')
    reng_label2.place(x=270, y=355)
    reng_entry2 = Entry(master=root2, width=15, font=20)
    reng_entry2.place(x=360, y=365)

    nomre_label2 = Label(master=root2, text='Nomre:', font=('Helvetica', 20), fg='black')
    nomre_label2.place(x=270, y=405)
    nomre_entry2 = Entry(master=root2, width=15, font=20)
    nomre_entry2.place(x=360, y=415)

    save_button2 = Button(master=root2, text='Save', bg='orange', fg='black', font=20, width=10, command=save)
    save_button2.place(x=270, y=465)