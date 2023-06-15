# Serti ifadeler ve mentiqi konstruksiyalar
print("1 == 1:", 1 == 1)
print(" 1 == 2:", 1 == 2)
print("1 != 1:", 1 != 1)
print(" 1 != 2:", 1 != 2)
print("1 > 1:", 1 > 1)
print("1 > 2:", 1 > 2)
print("2 > 1:", 2 > 1)
print("1 < 1:", 1 < 1)
print("1 < 2:", 1 < 2)
print("2 < 1:", 2 < 1)
print("1 >= 1:", 1 >= 1)
print("1 >= 2:", 1 >= 2)
print("2 >= 1:", 2 >= 1)
print("1 <= 1:", 1 <= 1)
print("1 <= 2:", 1 <= 2)
print("2 <= 1:", 2 <= 1)

# Deyerlerin mentiqi tipe (bool tipine) cevrilmesi

print(bool(""))
print(bool(0.0))
print(bool(None))
print(bool("IT Step Academy"))
print(bool(1))

# Mentiqi operatorlar

competent = True
responsible = True
print(competent and responsible)

competent = True
responsible = False
print(competent or responsible)

previously_fired = True
print(not previously_fired)

# Mesele 1

time = int(input("Saati daxil edin: ")) % 24
ticket = False
money = True
luggage = False
print((money or ticket) and not luggage and time > 6)

# if serti konstruksiyasi

car_speed = int(input('Suret daxil edin: '))
if car_speed > 100:
    print("Masin yuksek suretle hereket edir")

# 1-den cox sertin verilmesi

car_speed = 100
if car_speed > 50 and car_speed < 150:
    print('Masinin sureti 50 ile 150 arasindadir')

# Icra bloku anlayisi

if 1 < 4:
    print("bu setir blokun daxilindedir")
    print("bu setir blokun daxilindedir")
    print("bu setir de blokun daxilindedir")
    print("bu setir blokun sonuncu setiridir")
print("bu setir blokun xaricindedir")

# if ... else konstruksiyasi

car_speed = int(input())
if car_speed > 100:
    print('Masin yuksek suretle hereket edir')
else:
    print('Masin asagi suretle hereket edir')

# if...elif...else konstruksiyasi

car_speed = int(input())
if car_speed >= 100:
    print('Masin yuksek suretle hereket edir')

elif car_speed >= 70 and car_speed < 100:
    print('Masin orta suretle hereket edir')

else:
    print('Masin asagi suretle hereket edir')

# mesele 2

eded = int(input('Ededi daxil edin: '))
if eded % 2 == 0:
    print(f'{eded} ededi cut ededdir')
else:
    print(f'{eded} ededi tek ededdir')

# mesele 3

eded = int(input('Eded daxil edin: '))

if eded % 7 == 0:
    print(f'{eded} ededi 7-ye tam bolunur')
else:
    print(f'{eded} ededi 7-ye tam bolunmur')

# mesele 4
eded_1 = int(input('1-ci ededi daxil edin: '))
eded_2 = int(input('2-ci ededi daxil edin: '))

if eded_1 > eded_2:
    print(f'{eded_2} minimumdur')
elif eded_1 < eded_2:
    print(f'{eded_1} minimumdur')
else:
    print('Bu ededler beraberdir')

# mesele 5

eded_1 = float(input('1-ci ededi daxil edin: '))
eded_2 = float(input('2-ci ededi daxil edin: '))

cem = eded_1 + eded_2
ferq = abs(eded_1 - eded_2)
hasil = eded_1 * eded_2
nisbet = eded_1 / eded_2

istifadecinin_secimi = input('Istediyiniz emeli daxil edin: ')
if istifadecinin_secimi == '+':
    print(cem)
elif istifadecinin_secimi == '-':
    print(ferq)
elif istifadecinin_secimi == '*':
    print(hasil)
elif istifadecinin_secimi == '/':
    print(nisbet)
else:
    print('Zehmet olmasa, "+, -, *, /" kimi emeller daxil edin')
