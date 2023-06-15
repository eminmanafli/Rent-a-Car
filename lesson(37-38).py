'''
# Coxluq
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.intersection(B))

# bos coxluq yaratmaq ucun
a = set()

a = {}  # avtomatik dictionary olur

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.intersection(B))        # .intersection() -> kesisme -> &
B.add(7)
print(B)
# Eyni elementler elave etmek olmaz

set1 = {1, 2, 3, 4}
set2 = {3, 4, 10, 11}
print(set1.union(set2))     # .union() -> birlesme -> |
print(set1.difference(set2))    # .difference() -> ferq -> -

A.remove(2)     # Olmayan eded daxil edende error verecek
print(A)
A.discard(2)    # Olmayan eded daxil edende error vermeyecek
A.update(B)     # Birlesdirir. Update orijinal coxlugu deyisdirir, union ise deyisdirmir.

# A.update(B) -> A = A.union(B)

print(len(A))
print(min(A))
print(max(A))
print(sum(A))

for index, element in enumerate(A):
    print(f'{index} - {element}')

# frozen set
A = frozenset({1, 2, 3, 4, 5, 6})
print(type(A))

# dictionary
dict1 = {}
dict2 = dict()

dict1 = {'name': 'John', 'surname': 'Ivanov', 'age': 30, 'cars': ['BMW', 'Mercedes']}
dict1['name'] = dict1.get('name)    # .get() -> error vermir
dict1['phone'] = 'Iphone 14 pro max'
del dict1['age'] == dict1.pop('name')
# dict1.clear()
dict2 = {'home': 'Port Baku', 'watch': 'Rolex'}
dict1.update(dict2)
print(dict1)

# value type: int, float, boolean
# reference type: string, list, tuple
# int-> 4 bayt
# float -> 8 bayt
# 'a' -> 1 bayt
# reference type elave yer tutmasin deye var
dict1 = {'name': 'John', 'surname': 'Ivanov', 'age': 30, 'cars': ['BMW', 'Mercedes']}
dict2 = dict1.copy()    # copy eleyende dict2-de deyissek dict1-de deyismeyecek

# task 1
olkeler = {'Azerbaycan', 'Turkiye', 'Pakistan', 'ABS'}
# 1: olkenin elave edilmesi
new = input('Daxil etmek istediyiniz olke adini daxil edin: ')
olkeler.add(new)
print(olkeler)
# 2: olkenin silinmesi
delete = input('Silmek istediyiniz olke adini daxil edin: ')
olkeler.discard(delete)
print(olkeler)
# 3: simvollar uzre axtaris
user_input = input('Simvol daxile edin: ')
for i in olkeler:
    if user_input in i:
        print(i)
# 4: olkenin movcud olub-olmadiginin yoxlanmasi
olke = input('Axtarmaq istediyiniz olke adini daxil edin: ')
for i in olkeler:
    if i == olke:
        print('Daxil etdiyiniz olke coxluqda var')
    else:
        print('Coxluqda bele bir olke adi yoxdur')

# task 2
set1 = {'Baki', 'Xirdalan', 'Istanbul'}
set2 = {'Ankara', 'Izmir', 'New York'}
set3 = set1.union(set2)
print(set3)

# task 3
set1 = {'Baki', 'New York', 'Istanbul'}
set2 = {'Ankara', 'Baki', 'New York'}
set3 = set1 - set2
print(set3)
'''
# task 4
countries = {"Azerbaycan":"Baki"}
while True:
   option = input("1) Elave et\n2) Sil\n3) Deyisdir\n4) Tap\n5) Goster\n6) Cix\nSecin: ")
   if option == "1":
      yeni_olke = input("Enter country: ")
      yeni_paytaxt = input("Enter capital: ")
      countries[yeni_olke] = yeni_paytaxt
   elif option == '2':
       delete = input('Silmek istediyiniz olkeni daxil edin: ')
       del countries[delete]
   elif option == '3':
       old_country = input('Deyismek istediyiniz olke adini daxil edin: ')
       new_country = input('Yeni olke adini daxil edin: ')
       new_capital = input('Yeni paytaxt daxil edin: ')
       del countries[old_country]
       countries[new_country] = new_capital
   elif option == '4':
       find = input('Axtarmaq istediyiniz olke adini daxil edin: ')
       if find in countries:
           print('Olke tapildi')
       else:
           print('Bele bir olke tapilmadi')
   elif option == '5':
       print(countries)
   elif option == "6":
      break
