'''
names = ['Bob', 'Michele', 'Alice', 'Tom', 'Fred', 'David']
birth_years = [1990, 1992, 1995, 1996, 1989, 1988]

# 1
names.append('Samantha')
print(names)
# 2
names.insert(0, 'Ted')
print(names)
# 3
names.remove('Fred')
print(names)
# 4
names.index('Michele')
print(names)
# 5
if 'Cindy' in names:
    print('Yes')
else:
    print('No')
# 6
names.reverse()
print(names)
# 7
names.sort()
print(names)
# 8
birth_years.sort(reverse=True)
print(birth_years)
# 9
string = 'Iphone X, Iphone XR, Iphone XS'
list = []
word = string.split(', ')
print(word)
# 10
print(max(birth_years))
print(min(birth_years))
# 11
count = birth_years.count(1990)
print(count)
# 12
new_list = birth_years.clear()
print(new_list)
# 13
marka = input('3 eded marka adi daxil edin: ')
list = marka.split(', ')
print(list)


# Tapsiriq 2
import random
list = []
sum_neg = 0
sum_even = 0
sum_odd = 0
hasil_index3 = 1
hasil = 1
for i in range(20):
    random_numbers = random.randint(-100, 100)
    list.append(random_numbers)
print(list)
for i in list:
    if i < 0:
        sum_neg += i
    if i % 2 == 0:
        sum_even += i
    if i % 2 == 1:
        sum_odd += i
    if list.index(i) % 3 == 0:
        hasil_index3 *= i
print(sum_neg)
print(sum_even)
print(sum_odd)
print(hasil_index3)

minimum = min(list)
maximum = max(list)
for j in list:
    if j > minimum and j < maximum:
        hasil *= j
print(hasil)

first_positive_number = 0
last_positive_number = 0
reversed_list = list.reverse()
sum_pos = 0
for e in list:
    if e > 0:
        first_positive_number = e
        break
for n in reversed_list:
    if n > 0:
        last_positive_number = n
        break
for a in list:
    if a > first_positive_number and a < last_positive_number:
        sum_pos += a
print(sum_pos)
'''
# 1
import random
list = []
for i in range(10):
    random_numbers = random.randint(-100, 100)
    list.append(random_numbers)
print(list)
for el in list:
    for a in str(el):
        if a == '0':
            list.remove(el)
print(list)
# 2
words = input('Sozler elave edin: ')
word_list = words.split(', ')
for i in word_list:
    if i.upper() == i[::-1].upper():
        word_list.remove(i)
print(word_list)
# 3
import random
list = []
for i in range(10):
    random_numbers = random.randint(-100, 100)
    list.append(random_numbers)
print(list)

minimum = list[0]
for j in list:
    if j < minimum:
        minimum = j
list2 = list.remove(minimum)
minimum2 = list2[0]
for a in list2:
    if a < minimum2:
        minimum2 = a
print(minimum + minimum2)
# 4
import random
list = []
dublikat = []
for i in range(10):
    random_numbers = random.randint(-100, 100)
    list.append(random_numbers)
print(list)
for j in list:
    if list.count(j) != 1:
        dublikat.append(j)
print(dublikat)