# mesele 1
'''
wallet = float(input('Pulu daxil edin: '))
request = float(input('Elde etmek istediyiniz meblegi daxil edin: '))

if request <= wallet:
    print(f'Pul verildi. Hesabinizda {wallet - request} manat qaldi')
else:
    print('Hesabinizda kifayet qeder mebleg yoxdur')

# mesele 2
wallet = float(input('Pulu daxil edin: '))
request = float(input('Elde etmek istediyiniz meblegi daxil edin: '))

while request <= wallet:
    wallet = wallet - request
    print(f'Hesabinizda {wallet} manat qaldi')
    if wallet == 0 or request > wallet:
        break
'''
# mesele 4
project_menu = """
            Valyuta =>      1
            Kalkluyator =>  2
            Mile to km =>   3
            Cixis =>        0
"""
valyuta_menu = """
            AZN to USD =>  1
            AZN to EUR =>  2
            AZN to RUB =>  3
            Cixis =>       0
"""
while True:
    print(project_menu)
    choice = input('Secim daxil edin: ')
    if choice == '1':
        azn_balans = float(input('Mebleg daxil edin: '))
        print(valyuta_menu)
        while True:
            valyuta = input('Valyuta secimi daxil edin: ')
            if valyuta == '1':
                print(f'{azn_balans} AZN = {azn_balans / 1.7} USD')
            elif valyuta == '2':
                print(f'{azn_balans} AZN = {azn_balans / 1.9} EUR')
            elif valyuta == '3':
                print(f'{azn_balans} AZN = {azn_balans / 0.026} RUB')
            elif valyuta == '0':
                print('Valyuta proqramindan cixis...')
                break
            else:
                print('Valyuta secimini duzgun daxil edin')
    elif choice == '2':
        num1 = float(input('Birinci ededi daxil edin: '))
        num2 = float(input('Ikinci ededi daxil edin: '))
        while True:
            op = input('Emeliyyat daxil edin (+, -, *, /):')
            if op == '+' or op == '-' or op == '*' or op == '/':
                break
        if op == '+':
            print(f'{num1} + {num2} = ', num1 + num2)
            break
        elif op == '-':
            print(f'{num1} - {num2} = ', num1 - num2)
            break
        elif op == '*':
            print(f'{num1} * {num2} = ', num1 * num2)
            break
        else:
            print(f'{num1} / {num2} = ', num1 / num2)
            break
    elif choice == '3':
        mile = float(input('Mil daxil edin: '))
        print(f'{mile} mil = {mile * 1.609} km')
    elif choice == '0':
        print('Proqramdan cixis...')
        break
    else:
        print('Secim dogru deyil')