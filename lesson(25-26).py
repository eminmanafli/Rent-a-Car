# random kitabxanasinin .shuffle() metodu  -> arqument olaraq list qebul edir, listin ozunu deyisir
# ve neticede qarisdirilmis list elde edirik
import random
original_list = []
for i in range(10):
    random_number = random.randint(1, 101)
    original_list.append(random_number)
print(original_list)

random.shuffle(original_list)
print(original_list)

# List daxilindeki elementin deyerinin deyisdirilmesi
numbers = [12, 32, 21, 202, 40, 50, 32, 32, 32]

for index in range(len(numbers)):
    if numbers[index] == 32:
        numbers[index] = 11
print(numbers)

# listin mezmununun doldurulmasi
# variant 3
numbers = [i for i in range(5)]
print(numbers)

numbers2 = [i*i for i in range(5, 10)]
print(numbers)

# variant 4
# Listin daxilinde input() funksiyasini cagira bilerik
names = [input('Ad1 daxil edin: '), input('Ad2 daxil edin: '), input('Ad3 daxil edin: ')]

# Nested lists
total_list = [1, 42, 54, [45, 465, 83]]
print(total_list[3])
print(total_list[3][1])

# Tebii ki, butun list metodlari daxili listlere tetbiq oluna biler
nested_list = [[372, 281, 27], [8238, 82, 53], [64, 93, 27]]
nested_list[1].insert(1, 24)
print(nested_list)

# .clear() metodu
nested_list[2].clear()
print(nested_list)

# Ic-ice listlerin yaradilmasi ve mezmunun doldurulmasi
student1 = ['Ad1', 'Soyad1']
student2 = ['Ad2', 'Soyad2']

all_students = []
all_students.append(student1)
all_students.append(student2)
print(all_students)

# 3x2 olculu random nested list
import random
outer_list = []

for i in range(3):
    inner_list = []
    for j in range(2):
        random_number = random.randint(0, 10)
        inner_list.append(random_number)
    outer_list.append(inner_list)
print(outer_list)

# Tapsiriq
outer_list = []

for i in range(2):
    inner_list = []
    for j in range(3):
        user_input = input('Element daxil edin: ')
        inner_list.append(user_input)
    outer_list.append(inner_list)
print(outer_list)

# Ic - ice listin elementlerinin cap olunmasi:
# Elementlerle cap
for inner_list in outer_list:
    for element in inner_list:
        print(element)

# Indexlerle cap
for i in range(len(outer_list)):
    for j in range(len(outer_list[i])):
        print(outer_list[i][j])

# Tapsiriq
names = [['Bob', 'Michele'], ['Alice', 'Tom'], ['Fred', 'David']]

#1
inner_list = ['Samantha', 'Frank']
names.append(inner_list)
print(names)
# 2
names[0].append('Ted')
print(names)
# 3
names[1].insert(0, 'Mary')
print(names)
# 4
names[2].remove('Fred')
print(names)
# 5
for i in names:
    if 'Cindy' in i:
        print('Cindy listin elementidir')
    if 'Samantha' in i:
        print('Samantha listin elementidir')
# 6
for j in names:
    j = j.reverse()
print(names)
# 7
for j in names:
    j = j.sort()
print(names)

# Tapsiriq
import random
outer_list = []

for i in range(3):
    inner_list = []
    for j in range(3):
        random_number = random.randint(0, 101)
        inner_list.append(random_number)
    outer_list.append(inner_list)
print(outer_list)

for inner_list in outer_list:
    for i in inner_list:
        print(i, end=' ')
    print()