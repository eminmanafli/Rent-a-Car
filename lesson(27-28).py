'''
# datetime ve time kitabxanalari -> bize tarix ve zaman ile islemeye imkan veren modullardir
# datetime kitabxanasi tarix (date) ve zaman (time) ile islemeye imkan verir
# time kitabxanasi saniyelerle verilmis zamanla isleyir
# aralarindaki ferq deqiqlik seviyyesindedir
# layihenin evvelinde kitabxanalari import etmek lazimdir:
import datetime
import time
print(datetime.datetime.today()) #->cari tarix ve zamani qaytarir
print(datetime.datetime.today().year)
print(datetime.datetime.today().month)
print(datetime.datetime.today().day)

print(datetime.datetime.now())  #->cari tarix ve zamani qaytarir

# time modulu
time.sleep(2)   #->arqument olaraq saniye qebul edir, verilmis saniye qeder proqramin icrasini gecikdirir

# .time() metodu 1970ci il yanvarin 1den baslayaraq bu gune qeder kecen zamani saniyelerle bize qaytarir
print(time.time())

# datetime.date(2021, 4, 17) -> verilmis deyeri tarix deyerine cevirir

# .ctime() metodu -> saniyelerde verilmis deyeri hemin vaxtdaki tarixe cevirir
currentTimeInSeconds = time.time()
print(time.ctime(currentTimeInSeconds))
'''
# Task

import datetime
import time

menu = '''
    [1] --> yeni telebe elave etmek
    [2] --> email seçilmiş telebeni silmek
    [3] --> ada göre telebe axtarışı
    [4] --> email daxil edilmiş telebeye qiymet verilmesi
    [5] --> email daxil edilmiş telebenin qiymetleri
    [6] --> email daxil edilmiş telebenin yaşı
    [7] --> eyni qrupda olan telebelerin siyahısı
    [8] --> bütün telebeler
    [9] --> SHOW MENU
    [10] --> email daxil edilmiş telebenin qiymet ortalaması
    [11] --> email daxil edilmis telebenin melumatlarinin yenilenmesi
    [0] --> EXIT
'''
print(menu)

index_name, index_surname, index_father, index_email, index_birth, index_group, index_grade = 0, 1, 2, 3, 4, 5, 6

#              0        1           2           3               4           5                6
student_1 = ['Leyla', 'Necefli', 'Muxtar', 'leyla@gmail.com', 2000, 'Online_22_Python', [12, 12, 12]]

all_students = [student_1]

while True:
    user_input = input('Menyudan secim daxil edin: ')
    if user_input == '1':
        print()

        # Adin daxil edilmesi
        while True:
            input_name = input('Ad daxil edin: ').upper()
            if input_name.isalpha() and len(input_name) >= 3:
                break
            else:
                print('Duzgun ad daxil edin!!!')
        # Soyadin daxil edilmesi
        while True:
            input_surname = input('Soyad daxil edin: ').upper()
            if input_surname.isalpha() and len(input_surname) >= 3:
                break
            else:
                print('Duzgun soyad daxil edin!!!')
        # Ata adinin daxil edilmesi
        while True:
            input_father_name = input('Ata adi daxil edin: ').upper()
            if input_father_name.isalpha() and len(input_father_name) >= 3:
                break
            else:
                print('Duzgun ata adi daxil edin!!!')
        # Email daxil edilmesi -> email unvani unikal olmalidir
        while True:
            input_email = input('Email unvani daxil edin: ')
            if input_email .endswith('gmail.com') or input_email.endswith('mail.ru') and input_email.count('@') == 1 and len(input_email) >= 12:
                check = True
                for student in all_students:
                    if student[index_email] == input_email:
                        print('Bele email unvani sistemde movcuddur!!!')
                        check = False
                        break
                if check:
                    break
            else:
                print('Duzgun email unvani daxil edin!!!')
        # Dogum ilinin daxil edilmesi
        while True:
            input_birth = int(input('Dogum ilini daxil edin: '))
            if input_birth >= datetime.datetime.today().year - 40 and input_birth <= datetime.datetime.today().year - 15:
                break
            else:
                print(f'Dogum ili {datetime.datetime.today().year - 40} ile {datetime.datetime.today().year - 15} arasinda ola biler!!! ')
        # Qrupun daxil edilmesi
        while True:
            input_group = input('Qrupu daxil edin: ').upper()
            if input_group.isprintable() and len(input_group) >= 1:
                break
            else:
                print('Duzgun qrup adi daxil edin!!!')
        # Qeydiyyat
        new_student = [input_name, input_surname, input_father_name, input_email, input_birth, input_group, []]
        all_students.append(new_student)
        print('Telebe ugurla elave edilmisdir')
        time.sleep(1)

    elif user_input == '2':
        print()
        input_email = input('Telebenin emailini daxil edin: ')
        check = False
        for student in all_students:
            if student[index_email] == input_email:
                all_students.remove(student)
                check = True
                break
        if check:
            print('Telebe ugurla sistemden silinmisdir')
        else:
            print('Bu email unvani ile telebe movcud deyil!!!')

    elif user_input == '3':
        print()
        input_name = input('Telebenin adini daxil edin: ')
        count = 1
        for student in all_students:
            if student[index_name] == input_name:
                print(f'{count}) {student[index_name]} {student[index_surname]} {student[index_father]} {student[index_email]} {student[index_birth]} {student[index_group]} {student[index_grade]}')
                count += 1
        if count == 1:
            print('Daxil edilmis adda telebe movcud deyil!!!')
    elif user_input == '4':
        print()
        input_email = input('Telebenin email unvanini daxil edin: ')
        check = True
        for student in all_students:
            if student[index_email] == input_email:
                check = False
                input_grade = input('Qiymet daxil edin(1-12): ')
                if input_grade.isnumeric():
                    input_grade = int(input_grade)
                    if input_grade >= 1 and input_grade <= 12:
                        student[index_grade].append(input_grade)
                    else:
                        print('Qiymet 1 ve 12 arasinda ola biler!!!')
                else:
                    print('Qiymet ededi olmalidir!!!')
            if check:
                print('Bu emailde telebe movcud deyil!!!')
    elif user_input == '5':
        print()
        input_email = input('Telebenin email unvanini daxil edin: ')
        check = False
        for student in all_students:
            if student[index_email] == input_email:
                check = True
                print('Verilmis telebenin qiymetler siyahisi: ', end=' ')
                for grade in student[index_grade]:
                    print(grade, end=', ')
            if not check:
                print('Bu emailde telebe movcud deyil!!!')
    elif user_input == '6':
        print()
        input_email = input('Telebenin email unvanini daxil edin: ')
        check = False
        for student in all_students:
            if student[index_email] == input_email:
                check = True
                print(f'{index_name} {index_surname} {index_father} yasi: ', end=' ')
                print(f'{datetime.date.today().year - student[index_birth]}')
            if check:
                print('Bu emailde telebe movcud deyil!!!')
    elif user_input == '7':
        print()
        input_group = input('Axtarilan qrup adini daxil edin: ')
        count = 1
        check = False

        for student in all_students:
            if student[index_group] == input_group:
                check = True
                print(f'{count}) {student[index_name]} {student[index_surname]} {student[index_father]} {student[index_email]} {student[index_grade]}')
                count += 1
            else:
                print('Bu adda qrup movcud deyil!!!')
    elif user_input == '8':
        print()
        count = 1
        for students in all_students:
            print(f'{count}) {students[index_name]} {students[index_surname]} {students[index_father]} {students[index_email]} {students[index_birth]} {students[index_group]} {students[index_grade]}')
            count += 1
    elif user_input == '9':
        print()
        print(menu)
        print()
    elif user_input == '10':
        print()
        input_email = input('Telebenin email unvanini daxil edin: ')
        check = False
        grade_sum = 0
        count = 0
        for student in all_students:
            if student[index_email] == input_email:
                check = True
                grade_sum = sum(student[index_grade])
                count = len(student[index_grade])
                if len(student[index_grade]) == 0:
                    print('Telebenin helelik qiymeti yoxdur')
                else:
                    print(f'Qiymet ortalamasi: {grade_sum / count}')
            if not check:
                print('Bu emailde telebe movcud deyil!!!')
    elif user_input == '11':
        print()
        input_email = input('Telebenin email unvanini daxil edin: ')
        check = False
        for student in all_students:
            if student[index_email] == input_email:
                check = True
               # Adin daxil edilmesi
                while True:
                    input_name = input('Yeni Ad daxil edin: ').upper()
                    if input_name.isalpha() and len(input_name) >= 3:
                        student[index_name] = input_name
                        break
                    else:
                        print('Duzgun ad daxil edin!!!')
                # Soyadin daxil edilmesi
                while True:
                    input_surname = input('Yeni Soyad daxil edin: ').upper()
                    if input_surname.isalpha() and len(input_surname) >= 3:
                        student[index_surname] = input_surname
                        break
                    else:
                        print('Duzgun soyad daxil edin!!!')
                # Ata adinin daxil edilmesi
                while True:
                    input_father_name = input('Yeni Ata adi daxil edin: ').upper()
                    if input_father_name.isalpha() and len(input_father_name) >= 3:
                        student[index_father] = input_father_name
                        break
                    else:
                        print('Duzgun ata adi daxil edin!!!')
                # Email daxil edilmesi -> email unvani unikal olmalidir
                student[index_email] = input('Yeni email unvani daxil edin: ')
                if input_email.endswith('gmail.com') or input_email.endswith('mail.ru') and input_email.count(
                        '@') == 1 and len(input_email) >= 12:
                    print('Email deyisdirildi')
                else:
                    print('Duzgun email daxil edin!!!')
                # Dogum ilinin daxil edilmesi
                while True:
                    input_birth = int(input('Yeni Dogum ilini daxil edin: '))
                    if input_birth >= datetime.datetime.today().year - 40 and input_birth <= datetime.datetime.today().year - 15:
                        student[index_birth] = input_birth
                        break
                    else:
                        print(
                            f'Dogum ili {datetime.datetime.today().year - 40} ile {datetime.datetime.today().year - 15} arasinda ola biler!!! ')
                # Qrupun daxil edilmesi
                while True:
                    input_group = input('Yeni Qrupu daxil edin: ').upper()
                    if input_group.isprintable() and len(input_group) >= 1:
                        student[index_group] = input_group
                        break
                    else:
                        print('Duzgun qrup adi daxil edin!!!')
                # Qeydiyyat
                updated_student = [[input_name], [input_surname], [input_father_name], [input_email], [input_birth], [input_group], student[index_grade]]
                all_students.remove(student)
                all_students.append(updated_student)
                print('Melumatlar ugurla yenilenmisdir!')
                time.sleep(1)

            if not check:
                print('Bu emailde telebe movcud deyil!!!')

    elif user_input == '0':
        print()
        print('Bye.')
        time.sleep(1)
        print('Bye..')
        time.sleep(1)
        print('Bye...')
        break
    else:
        print('Secim yanlisdir!!!')








































