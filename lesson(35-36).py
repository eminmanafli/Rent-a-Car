# Currying

# Is yeri
# Vezife
# Departament
# Adamin adi
# Tebrik

def tebrik(is_yeri, vezife, depar, ad, tebrik):
    print(f'{is_yeri} {vezife} {depar} {ad} {tebrik}')


tebrik('Google', 'Director', 'Programming', 'John', 'Happy birthday!')


def func1(is_yeri):
    def func2(vezife):
        def func3(depar):
            def func4(ad):
                def func5(tebrik):
                    print(f'{is_yeri} {vezife} {depar} {ad} {tebrik}')
                return func5(tebrik)
            return func4()
        return func3()
    return func2()


google_tebrikler = func1('Google')('Director')('Programming')
google_tebrikler('John')('Happy birthday!')


list = [1, 2, 4, 5, 10, 8]


def linery_search(list, num):
    for i in range(0, len(list)):
        if list[i] == num:
            return i
    return -1


def binary_search(list, num):
    start = 0
    end = len(list)-1
    while start<=end:
        mid = (start+end)//2
        if list[mid] == num:
            return mid
        elif num < list[mid]:
            end = mid-1
        elif num > list[mid]:
            start = mid+1
    return -1


list = [1,2,4,6,7,8,9]

print(binary_search(list, 8))

# kortej
mytuple = (1,2,3,4,5,6,7,8)    # append, pop, remove olmaz
print(mytuple)

list1 = ['John', 'James']
passwords = ['1234', 'qwerty']
print(list(zip(list1, passwords)))

# tapsiriq 1
meyve = ('banana', 'apple', 'bananamango', 'mango', 'strawberry-banana')
user_input = input('Meyve adi daxil edin: ')
count = 0
for i in meyve:
    if i == user_input:
        count += 1
print(count)

# tapsiriq 2
meyve = ('banana', 'apple', 'bananamango', 'mango', 'strawberry-banana')
user_input = input('Meyve adi daxil edin: ')
count = 0
for i in meyve:
    if user_input in i:
        count+=1
print(count)

# tapsiriq 3
cars = ('BMW', 'Mercedes', 'Ford', 'Nissan', 'BMW')
print(cars)
list1 = ['BMW', 'Mercedes', 'Ford', 'Nissan', 'BMW']
old = input('Deyismek istediyiniz adi daxil edin: ')
new = input('Yeni adi daxil edin: ')
for i in range(len(list1)):
    if list1[i]==old:
        list1[i] = new

print(tuple(list1))
