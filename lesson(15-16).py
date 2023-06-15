# Setirlerle is

str1 = 'Python'
str2 = 'Bootcamp'
str3 = str1 + str2
print(str3)

# String ile int
str1 = 'Python'
#str2 = str1 + 5
#print(str2) --> TypeError

# String ile int --> vurma aparmaq olar. Kopyalama emeliyyati icra olunar
str1 = 'Python'
str3 = str1 * 10
print(str3)

# String Slicing
str1 = 'Python Bootcamp 2023'
print(str1[3: 10])
print(str1[:10])
print(str1[3:])
print(str1[:])
print(str1[0: 14: 2])
print(str1[0: len(str1): 2])
# String slicing sintaksisi sonuncu limitden yuksek yazmaq olar
# Arxada isleyen kod:
for i in range(3 , 55):
    print(str1[i])
    if i == len(str1) - 1:
        break

# Setrin tersine cevrilmesi, reverse string
str1 = 'Python Bootcamp 2023'
print(str1[::-1])
'''
# task
'''
eded = input('Eded daxil edin: ')
reverse_eded = eded[::-1]
if eded == reverse_eded:
    print(f'{eded} ededi polindromdur')
else:
    print(f'{eded} ededi polindrom deyil')

# Metodlar. M etod ile funksiyanin ferqi
# Funksiyalar alt proqramlardir hansilar ki, mueyyen emeliyyatlari yerine yetirir ve bize bir cavab qaytarir
# Prosedur alt proqramlardir hansilar ki mueyyen emeliyyatlari yerine yetirir, lakin bir cavab qaytarmir
# Metodlar funkjsiyalar ve prosedurlardir hansilar ki, mueyyen sinfe ve ya sinfin numayendesine aid olur
# Metodlarin cagrilma sintaksisi
# object.methodname(args)

# Daxili metodlar
# Kitabxanalar -> basqa proqramcilar terefinden yazilmis ve funksionalligina gore qruplasdirilmis metodlar toplusudur

import random   # random adli kitabxanani layihemize daxil etmis oluruq
# random kitabxanasi -> tesadufi deyerler kitabxanasidir
print(random.random())   # 0 ile 1 arasinda random deyer qaytarir
print(random.randint(-90, 100))  # randint metodu verilmis diapazonda tesadufi int ededi qaytarir
print(random.uniform(-90, 100))    # uniform verilmis araliqda tesadufi kesr ededi qaytarir
print(random.choice('Hello World'))   # verilmis setirdeki tesadufi simvolu qaytarir

# mesele
import random
boyuk_herfler = 'QWERTYUIOPASDFGHJKLZXCVBNM'
kicik_herfler = 'qwertyuiopasdfghjklzxcvbnm'
ededler = '1234567890'
simvollar = '!@#$%^&*()_+=-.,'
sifre = random.choice(boyuk_herfler) + random.choice(kicik_herfler) + random.choice(ededler) + random.choice(simvollar)
print(sifre)


# String metodlari
str_name = 'lorem ipsum dolor sit amet, consectetur adipiscing elit. cras sed scelerisque enim, eu laoreet magna.'
print(str_name.capitalize())   # setri boyuk herfle basladir
print(str_name.title())        # setrdeki butun sozler boyuk herfle basladir
print(str_name.upper())        # stirdeki butun herfleri boyuk edir
print(str_name.lower())        # setrdeki butun herfleri kicildir

# Setir daxilinde axtaris
print(str_name.find('ipsum'))   # axtarilan elementin indeksini qaytarir
print(str_name.find('sdxfgch'))   # element olmayanda -1 qaytarir
print(str_name.replace('dolor', 'Python'))    # elementleri evez edir
print(str_name.replace('dolor', 'Python', 3))    # ilk 3-nu evez edir

# Stringin metodlari hemin stringin kopyalari uzerinde  isleyir orijinal stringin deyeri deyismir
print(str_name.count('dolor'))
print(str_name.count('s'))

# String Check Methods -> metodun ve stringin mezmununa gore true ve yafalse qaytarir
print(str_name.isupper())
print(str_name.islower())
print(str_name.isnumeric())
print(str_name.isalpha())
print(str_name.isalnum())

print(str_name.isascii())
print(str_name.startswith('lorem'))
print(str_name.endswith('.'))
