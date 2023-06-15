# Lists-Siyahilar
# Siyahilar-> muxtelif tipli elementler toplusudur (collection).
list_1 = []
list_2 = list()
print(type(list_1))
print(type(list_2))

# List-in doldurulmasi
list_1 = [23, 12, 56 ,78]
list_2 = list('Hello World')   # list() funksiyasi cemi 1 arqument qebul edir ve bu deyer iterable olmalidir.
print(list_1)
print(list_2)

# Siyahilar-> muxtelif tipli elementler toplusudur (collection)
elements = [12, 21, 3.4, 'Bob', 'Alice', True]
print(elements)

# List-lerde indexlenme
        #    0   1   2     3     4        5
elements = [12, 21, 3.4, 'Bob', 'Alice', True]
          # -6  -5  -4   -3      -2      -1
print(elements[4])

# Listlerde elementler ayri-ayri deyisenler arasinda paylana biler.
num1, num2 = [12, 34]
print(num1, ' ', num2)
# QEYD: deyisenlerin ve elementlerin sayi eyni olmalidir

# List Slicing
elements = [12, 21, 3.4, 'Bob', 'Alice', True]
print(elements[::2])
print(elements[::-1])

# List-in elementlerine index-e gore muraciet - 2
elements = [12, 21, 3.4, 'Bob', 'Alice', True]
print(elements[3][1])

# Listin elementlerinin cap olunmasi:
elements = [12, 21, 3.4, 'Bob', 'Alice', True]
for i in elements:
    print(i)

# Task 1
numbers = [12, 23, 34, 45, -47, 123, 3748]
for i in numbers:
    print(i, end=' ')
# Task 2
numbers = [12, 23, 34, 45, -47, 123, 3748]
sum = 0
for i in numbers:
    sum += i
print(sum)
# Task 3
numbers = [12, 23, 34, 45, -47, 123, 3748]
sum = 0
for i in numbers:
    sum += i
print(f'ededi orta = {sum / len(numbers)}')
# Task 4
numbers = [12, 23, 34, 45, -47, 123, 3748]
cem = 0
hasil = 1
for i in numbers:
    if i % 2 == 0:
        cem += i
    else:
        hasil *= i
print(cem)
print(hasil)
# Task 5
numbers = [12, 23, 34, 45, -47, 123, 3748]
hasil = 1
for i in numbers:
    if numbers.index(i) % 2 == 0:
        hasil *= i
print(hasil)

# List uzerinde is: + ve *
list1 = [1, 2, 3]
list2 = [4, 6, 5]
print(list1 + list2)
print(list1 * 6)

# List functions
numbers = [12, 23, 34, 45, -47, 123, 3748]
print(sum(numbers))
print(len(numbers))
print(max(numbers))
print(min((numbers)))

# List methods
# QEYD: listin metodlari listin ustunde isleyir, yeni orjinal list deyisir
# .count() listde elementin nece defe rast gelindiyini sayir
names = ['Bob', 'Alice', 'Tom', 'Bob']
print(names.count('Bob'))

# Listlerde axtaris etmek ucun: .index() ve IN ve NOT IN acar sozleri
names = ['Bob', 'Alice', 'Tom', 'Bob']
print(names.index('Alice'))
print(names.index('Marley'))    # ValueError

if 'Bob' in names:
    print('Yes')
if 'Marley' not in names:
    print('No')

# Elementlerin silinmesi: .pop(), .remove(), .clear(), del acar sozu
# .pop()-> verilmis index-deki elementi silir, arqument verilmedikde sonuncu elementi silir
names = ['Bob', 'Alice', 'Tom', 'Bob']
names.pop()
print(names)
# QEYD: .pop() metodu sildiyi deyeri bize qaytarir
names = ['Bob', 'Alice', 'Tom', 'Bob']
print(names.pop())
print(names)

# .remove() -> verilmis elementi silir
names = ['Bob', 'Alice', 'Tom', 'Bob']
names.remove('Tom')
print(names)
names.remove('Anna') #-> ValueError

# .clear() metodu -> verilmis listi sifirlayir
names = ['Bob', 'Alice', 'Tom', 'Bob']
names.clear()
print(names)

# del acar sozu -> deyiseni ram uzerinden silir
variable = 89
del variable
print(variable) # NameError

# Elementlerin elave olunmasi: .append(), .insert()
# .append() -> listin sonuna verilmis elementi elave edir
names = ['Bob', 'Alice', 'Tom', 'Bob']
names.append('Anna')
print(names)

# .insert()-> verilmis index-e verilmis elementi elave edir
names = ['Bob', 'Alice', 'Tom', 'Bob']
names.insert(0, 'Anna')
print(names)

# Elementleri siralanmasi: .reverse(), .sort(), .sort(reverse = True)
names = ['Bob', 'Alice', 'Tom', 'Bob']
names.reverse()  # elementleri siralanmasini tersine cevirir
print(names)

# .sort() metodu-> elementleri artan qaydada duzur
# QEYD: listin elementleri eyni tipli olmalidir
names = ['Bob', 'Alice', 'Tom', 'Bob']
names.sort()
print(names)

numbers = [12, 23, 34, 45, -47, 123, 3748]
numbers.sort()
print(numbers)

# .sort(reverse = True) -> azalan qaydada elementleri siralayir
numbers = [12, 23, 34, 45, -47, 123, 3748]
numbers.sort(reverse=True)
print(numbers)

# Task
import random
list = []
start_number = int(input('Baslangic ededi daxil edin: '))
end_number = int(input('Son ededi daxil edin: '))

say = int(input('Say daxil edin: '))

for i in range(say):
    random_number = random.randint(start_number, end_number + 1)
    numbers.append(random_number)
print(numbers)

# Task
import random
list = []
start_number = int(input('Baslangic ededi daxil edin: '))
end_number = int(input('Son ededi daxil edin: '))

say = int(input('Say daxil edin: '))

for i in range(say):
    random_number = random.randint(start_number, end_number + 1)
    list.append(random_number)
print(list)

max = list[0]
for i in list:
    if i >= max:
        max = i
print(max)

# task
import random
list = []
start_number = int(input('Baslangic ededi daxil edin: '))
end_number = int(input('Son ededi daxil edin: '))

say = int(input('Say daxil edin: '))

for i in range(say):
    random_number = random.randint(start_number, end_number + 1)
    list.append(random_number)
print(list)

min = list[0]
for i in list:
    if i <= min:
        min = i
print(min)

# task
import random
numbers = []

while len(numbers) < 10:
    random_number = random.randint(0, 1000)
    if random_number % 2 == 0 and random_number % 3 == 0 and random_number % 8 == 0:
        numbers.append(random_number)
print(numbers)