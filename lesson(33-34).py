# tapsiriq 5
def hasil(a, b):
    hasil = 1
    if a < b:
        for i in range(a, b+1):
            hasil *= i
        return hasil
    else:
        a, b = b, a
        for i in range(a, b+1):
            hasil *= i
        return hasil
a = int(input('Baslangic ededi daxil edin: '))
b = int(input('Son ededi daxil edin: '))
print(hasil(a, b))

def func(func1, start, end, mult):
    return func1(start, end) * mult
result = func(hasil, 5, 7, 2)
print(result)

# Lambda function
def fun(a):
    return a*2

function = lambda a, b: a*b
print(function(2,3))

list1 = ["John", 'James', 'Bob']

# task
students = [['Bob22', 70], ['Jane111', 80], ['Bod', 50]]
print(students)
sortedSts = sorted(students, key=lambda x: len(x[0]))
print(sortedSts)

# .map()

def func(num):
    return num*2
list1 = [1, 5, 10, 15]

new_list = list(map(lambda x: x*2, list1))
print(new_list)

# .filter()
list1 = [5, 10, 15, 100]
new_list = []

for i in list1:
    if i < 50:
        new_list.append(i)
print(new_list)

def func(num):
    return num<50


new_list = list(filter(lambda num: num < 50, list1))
print(new_list)

# task
list1 = ['Bob', 'John', 'James']
new_list = list(filter(lambda name: name[1] == 'o', list1))
print(new_list)

# .zip()
userlogin = ['Emin', 'Bob']
userpassword = ['123123', '1903']

print(list(zip(userlogin, userpassword)))
for name, password in zip(userlogin, userpassword):
    print(f'Ad:{name}, Sifre:{password}')

# task 1
list1 = []
num1 = int(input('Eded daxil edin: '))
num2 = int(input('Eded daxil edin: '))
num3 = int(input('Eded daxil edin: '))
list1.append(num1)
list1.append(num2)
list1.append(num3)

def func(num):
    count = 0
    for i in list1:
        if i == num:
            count += 1
    return count
num = int(input('Axtarmaq istediyiniz ededi daxil edin: '))
result = func(num)
print(result)

# task
list1 = []
for j in range(3):
    eded = int(input('Eded daxil edin: '))
    list1.append(eded)

def cem():
    a = 0
    for i in list1:
        a += i
    return f'Ededlerin cemi: {a}'


def ededi_orta():
    b = 0
    for i in list1:
        b += i
    c = b / len(list1)
    return f'Ededi orta: {c}'

print(cem())
print(ededi_orta())

# task
import random
list1 = []

for i in range(10):
    random_number = random.randint(-100, 100)
    list1.append(random_number)
print(list1)

cut_eded = list(filter(lambda x: x % 2 == 0, list1))
print(cut_eded)
tek_eded = list(filter(lambda x: x % 2 == 1, list1))
print(tek_eded)
menfi_eded = list(filter(lambda x: x < 0, list1))
print(menfi_eded)
musbet_eded = list(filter(lambda x: x > 0, list1))
print(musbet_eded)