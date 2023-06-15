'''for i in range(10):
    for j in range(10):
        print(f'{i} * {j}', end='\t')
    print()

for i in range(1, 6):
    for j in range(1, 6):
        print(j % 2, end='\t')
    print()

for i in range(5, 0, -1):
    for j in range(1, 6):
        print(i // 1, end='\t')
    print()

for i in range(65, 70):
    for j in range(1, 6):
        print(chr(i), end='\t')
    print()
'''
for i in range(5):
    for j in range(5):
        if i == j and i + j == 6:
            print('*', end='\t')
        else:
            print(end='\t')
    print()