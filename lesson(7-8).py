'''
# try except sintaksis nümune
try:
    amount = int(input('Enter the amount of product: '))
    product_type = input('Enter the type of product: ')
    parts_number = int(input('Enter the number of parts: '))
    parts = amount / parts_number
    print(f'{parts_number}')
    print(f'{parts}')
except ValueError:
    print('The amount should be integer')
except ZeroDivisionError:
    print('0-a bölmek olmaz')
else: # else heç bir except işlemedikde işleyir
    print('Everything worked properly.')
finally: # her zaman işleyir
    print('The problem has solved.')

# raise Exception
try:
    apple = int(input('Enter the number of apples: '))
    if apple < 0:
        raise Exception
    print('the numbe of apples: {apple}')
except Exception:
    print('Alma sayı menfi ola bilmez')

# mesele 1
try:
    saat = int(input("Saati daxil edin: "))
    deqiqe = int(input('Deqiqeni daxil edin: '))
    if saat >= 24 or saat < 0 or deqiqe >= 60 or deqiqe < 0:
        raise Exception
    print(f'Saat {saat}:{deqiqe}-dir')
except Exception:
    print('Zamani duzgun daxil edin')

#mesele 2
try:
    saat = int(input('Saati daxil edin: '))
    if saat >= 0 and saat < 6:
        print('Good Night!')
    elif saat >= 6 and saat < 13:
        print('Good Morning!')
    elif saat >= 13 and saat < 17:
        print('Good Day!')
    elif saat >= 17 and saat < 24:
        print('Good Evening!')
    else:
        raise Exception
except Exception:
    print('Zamani duzgun daxil edin')

# Exceptions ardıcıllıq
try:
    raise ValueError
except ValueError:
    print('Not the correct Value')
except Exception:
    print('Hmm...Something is wrong')

# mesele 3
zaman_saniye = float(input('Gunun baslangicindan kecen vaxti '
                         'saniye ile daxil edin: '))
istifadecinin_secimi = input('saat, deqiqe, yoxsa saniye')

if istifadecinin_secimi == 'saat':
    print(f'Gece yarisina {24  - (zaman_saniye / 3600)} saat qalib')
elif istifadecinin_secimi == 'deqiqe':
    print(f'Gece yarisina {1440 - (zaman_saniye / 60)} deqiqe qalib')
elif istifadecinin_secimi == 'saniye':
    print(f'Gece yarisina {86400 - zaman_saniye} saniye qalib')
else:
    print('Zehmet olmasa, saat, deqiqe, ya da saniye daxil edin')

# mesele 4 23847
eded = int(input('5 reqemli eded daxil edin: '))
digit_1 = eded // 10000
digit_2 = eded // 1000 % 10
digit_3 = eded // 100 % 10
digit_4 = eded // 10 % 10
digit_5 = eded % 10

if digit_1 == digit_5 and digit_2 == digit_4:
    print(f'{eded} ededi polindrom ededdir')
else:
    print(f'{eded} ededi polindrom deyil')

# mesele 5
fayl_olcusu = float(input('Fayl olcusunu gigabaytla daxil edin: ')) * 10 ** 9
internet_sureti = float(input('Internete qosulma suretini bit/saniye ile daxil edin: '))
istifadecinin_secimi = input('saat, deqiqe, yoxsa saniye?: ')

saniye = fayl_olcusu / internet_sureti
deqiqe = saniye / 60
saat = deqiqe / 60

if istifadecinin_secimi == 'saat':
    print(f'Yukleme vaxti {saat} saatdir')
elif istifadecinin_secimi == 'deqiqe':
    print(f'Yukleme vaxti {deqiqe} deqiqedir')
elif istifadecinin_secimi == 'saniye':
    print(f'Yukleme vaxti {saniye} saniyedir')
else:
    print('Zamani duzgun daxil edin')
'''
