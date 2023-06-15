'''
class Car:
    def __init__(self, reng, model):
        self.reng = reng
        self.model = model

    def signal(self):
        print('Beeeep')

    def baqaji_ac(self):
        print('Baqaj acildi!')


car1 = Car('qirmizi', 'Mercedes')

# task
class Insan:
    def __init__(self, ad, yas, cins, boy, ceki):
        self.ad = ad
        self.yas = yas
        self.cins = cins
        self.boy = boy
        self.ceki = ceki

    def qacmaq(self, suret):
        print(f'{self.ad}in sureti {suret}-dir')

    def hoppanmaq(self, hundurluk):
        print(f'{self.ad} {hundurluk} qeder hoppana bilir')

    def pul(self, count):
        print(f'{self.ad} {count}')

# task 2
class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, yatirilan_mebleg):
        self.balance += yatirilan_mebleg

    def withdraw(self, cixarilan_mebleg):
        if self.balance >= cixarilan_mebleg:
            self.balance -= cixarilan_mebleg
        else:
            print('Hesabda kifayet qeder pul yoxdur')

    def get_balance(self):
        print(self.balance)

    def get_info(self):
        print(f'{self.account_number} {self.owner} -> {self.balance}')


emin = BankAccount(123456, 'Emin Manafli', 1500)
emin.deposit(500)
emin.withdraw(300)
emin.get_balance()
emin.get_info()
'''
# task 3
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
        self.renter = None

    def rent(self, renter):
        if self.available == True and self.renter == None:
            self.available = False
            self.renter = renter
        else:
            print('Kitab artiq kiraye verilib')

    def return_book(self):
        if self.available == False and self.renter != None:
            self.available = True
            self.renter = None
        else:
            print('Kitab kirayede deyil!')

    def is_available(self):
        print(self.available)

    def get_info(self):
        print(self.title)
        print(self.author)
        print(self.available)

kitab = Book(title='Qara Zanbaq', author='Aleksandr Duma')
kitab.rent('Emin')
kitab.return_book()
kitab.is_available()
kitab.get_info()