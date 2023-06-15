'''# Tapşırıq 1
start = int(input('Eded daxil edin: '))
end = int(input('Eded daxil edin: '))
while start < end:
    print(start)
    start += 1

# Tapşırıq 2
start = int(input('Eded daxil edin: '))
end = int(input('Eded daxil edin: '))
while end > start:
    print(end)
    end = end - 1  # end -= 1

# Tapşırıq 4
start = int(input('Eded daxil edin: '))
end = int(input('Eded daxil edin: '))
sum = 0
while start < end:
    if start % 3 == 0 and start % 5 == 0:
        sum = sum + start
        print(start)
    start = start + 1
print(sum)

#Tapşırıq 5
# Faktorial — 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1
number = int(input('Enter number: ')) # 7
factorial = 1
while number > 0:
    factorial = factorial * number
    number = number - 1
    print(f'Faktorial deyeri: {factorial}')
print('the end')

# task 6
number = int(input('Enter number: '))
count = 0
sum = 0
while number > 0:
    digit = number % 10
    number //= 10
    sum = sum + digit
    count += 1
print(f'Reqemlerin sayi {count}')
print(f'Reqemlerin cemi {sum}')

# task 7
start_number = int(input('Eded daxil edin: '))
end_number = int(input('Eded daxil edin: '))
while start_number < end_number:
    start_number += 1
    if start_number % 2 == 1:
        continue
    print(start_number)

# for dovru
print(list(range(20)))
print(list(range(5, 20)))
print(list(range(5, 20, 3)))
print(list(range(20, 5, -1)))

for element in range(30, 100):
    if element % 2 == 1:
        continue
    print(element)

# task 8
start_number = int(input('Eded daxil edin: '))
end_number = int(input('Eded daxil edin: '))

for number in range(start_number, end_number):
    if number % 7 == 0:
        print(number)
'''
#

for i in range(1, 10):
    for j in range(1, 10):
        if i == j or i + j == 10 or i == 1 or i == 9 or j == 1 or j == 9:
            print(j, end='\t')
        else:
            print(end='\t')
    print()
