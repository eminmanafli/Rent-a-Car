# Funksiyalar
# Funksiya nedir? -> mueyyen bir isi yerine yetiren ve tekrar tekrar
# istifade oluna bilen kod bloklaridir. Funksiyalar umumi proqram kodunu daha
# kicik hisselere ayirmaqla, modullara bolme imkani verir, bu ise proqramin
# oxunarligini daha asan edir

# Function decleration -> def acar sozu ile teyin olunur
'''
def function_name():
    function_body
'''
def say_hi():

    """
    bu funksiya salamlama isini gorur
    """
    print('Hi, World!')


say_hi()
# print(say_hi) - > bele yazi bize funksiyanin unvanini verir
adress_variable = say_hi
adress_variable()

# Elbette ki, funksiyani elan etmeden evvel funksiyani cagirmaq olmaz!!!
# Adeten funksiyalarin hamisi proqramin evvelinde yazilir
# Funksiya yaratmagin qaydalari var
# Ideal funksiyalar bele olur:
#1) Funksiyanin adi onun gorduyu ise uygun olmalidir ve her bir funksiya tek
# bir is yerine yetire biler
# 2) Funksiyanin ne is gorduyu barede comment-i olmalidir
# 3) Funksiyanin adinin kicik herfle baslanmasi tovsiye olunur
# 4) Eyni adda tek bir funksiya olmalidir. Bir nece eyni adda funksiya
# olarsa, bunlardan en axirincisi icra olunar

# Funksiya istifade etmeyin ustunlukleri:
# 1) umumi proqram kodu modullara ayrilmaqla strukturlasir, isimiz asanlasir
# 2) kod yigcam olur
# 3) kod tekrarinin qarsisi alinir.
# DRY prinsipi -> Don't Repeat Yourself

# tapsiriq
def sentence():
    print('''
    "Don't let the noise of others' opinions
    drown out your own inner voice."
                                Steve Jobs
    ''')
sentence()

# Funnksiyanin parametrleri
#sum(arguments) -> oturduyumuz deyerler arqument adlanir,
#funksiya ucun ise bunlar parametr adlanir

#def function_name(param1, param2, ..., paramN):
#    function body

def sum_(number1, number2):
    print(number1 + number2)
a = 16
b = 35
sum_(a, b)

# global acar sozu -> funksiyanin daxilinde funksiyanin xaricinde olan
# deyiseni cagirmaq ucundur

def sum_():
    global a
    global b
    print(a + b)
a = 41
b = 52
sum_()
# Visibility scope -> gorunurluk sahesi

# Tapsiriqlar
# 1
def tek_ededler(num1, num2):
    for i in range(num1, num2 + 1):
        if i % 2 == 1:
            print(i, end=' ')
tek_ededler(int(input('Eded daxil edin: ')), int(input('Eded daxil edin: ')))

# 2


def line(a, b, c):
    if b == 'saquli':
        for i in range(a):
            print(c, end='')
    else:
        for i in range(a):
            print(c, end='\n')


a = int(input('Eded daxil edin: '))
c = input('Simvol daxil edin: ')
b = input('Saquli yoxsa horizontal?: ').lower()
line(a, b, c)


# Funksiyalar 2 cur olur:
# 1) mueyyen isi icra eden
# 2) mueyyen isi icra etdikden sonra bir deyer qaytaran

# QEYD: capa vermek deyer qaytarmaq demek deyil!!!
# Funksiyada deyerin qaytarilmasi return operatoru ile heyata kecirilir


def say_Hi():
    string = 'Hello World'
    return string
returned_string = say_hi()
print(returned_string)

def say_Hi():
    return True
print(say_Hi())
# QEYD: return setrinde hansi tipde deyer qeyd olunubsa, o tipde deyer
# funksiyanin cagrildigi yere qayidir


def say_Hello(name):
    return f'Hello, {name}'
print(say_Hello('Emin').upper())

# QEYD: return operatoru her bir funksiya ucun 1 defe icra oluna biler
# Funksiya daxilinde return operatoru icra olunduqda, bize muvafiq deyer
# qayidir, proqramin isi dayanir, ve artiq return sozunden sonraki kodlar
# var olsalar bele oxunmur yeni icra olunmur

# tapsiriq 1
def factorial(num):
    hasil = 1
    for i in range(1, num+1):
        hasil *= i
    return hasil
num = int(input('Eded daxil edin: '))
print(factorial(num))

# tapsiriq 2
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            return True
num = int(input('Eded daxil edin: '))
print(is_prime(num))
